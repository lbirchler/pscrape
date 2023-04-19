from __future__ import annotations

import argparse
import sys
from collections import namedtuple
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import bs4
import requests


Proxy = namedtuple(
    'Proxy', [
        'ip_address',
        'port',
        'code',  # ISO Code
        'country',
        'anonymity',  # anonymous, elite proxy, transparent
        'google',  # yes, no
        'https',  # yes, no
        'last_checked',
    ],
)


class Proxies:
  """Scrape and validate proxies from free-proxy-list.net.

  Args:
      country (None | str, optional): Country ISO Code. Defaults to None.
      anon (None | str, optional): Anonymity level. Defaults to None.
          anonymous, elite, or transparent.
      https (bool, optional): Https only. Defaults to False.
      debug (bool, optional): Display scraped and validated proxies. Defaults to False.

  """

  def __init__(
          self,
          country: None | str = None,
          anon: None | str = None,
          https: bool = False,
          debug: bool = False,
  ):
    self.country = country
    self.anon = anon
    self.https = https
    self.debug = debug

  def _fetch(self):
    r = requests.get('https://free-proxy-list.net')
    if r.status_code != 200:
      print('Error scraping proxies: %d - %s' % r.status_code, r.reason)
      return
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    body = soup.find('tbody')
    rows = body.find_all('tr')
    proxies = []
    for row in rows:
      proxy = Proxy(*[x.text.strip() for x in row.find_all('td')])
      if (
          self.country and proxy.code != self.country
      ) or (
          self.anon and self.anon not in proxy.anonymity
      ) or (
          self.https and proxy.https == 'no'
      ):
        continue
      proxies.append(proxy)
    if self.debug:
      print('+ Total scraped proxies:  %d' % len(proxies))
    return proxies

  @staticmethod
  def _check_one(proxy: Proxy):
    ip_port = f'{proxy.ip_address}:{proxy.port}'
    r = requests.get(
        'https://httpbin.org/ip',
        proxies={'http': ip_port, 'https': ip_port},
        timeout=2,
    )
    return (proxy, r.status_code)

  def _check_all(self, proxies: list[str]):
    working = []
    with ThreadPoolExecutor() as executor:
      futures = [
          executor.submit(self._check_one, proxy)
          for proxy in proxies
      ]
      for future in as_completed(futures):
        try:
          proxy, status_code = future.result()
          if status_code == 200:
            if self.debug:
              type = 'https' if proxy.https == 'yes' else 'http'
              addr = f'{proxy.ip_address}:{proxy.port}'
              print(
                  '> %-22s | %-3s | %-12s | %s' %
                  (addr, proxy.code, proxy.anonymity, type),
              )
            working.append(f'{proxy.ip_address}:{proxy.port}')
        except BaseException:
          continue
    if self.debug:
      print('+ Total validated proxies: %d' % len(working))
    return working

  def scrape(self):
    proxies = self._fetch()
    working = self._check_all(proxies)
    return working


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-c',
      '--country',
      help='Country ISO Code',
  )
  parser.add_argument(
      '-a',
      '--anon',
      choices=['anonymous', 'elite', 'transparent'],
      help='Anonymity level',
  )
  parser.add_argument(
      '--https',
      action='store_true',
      default=False,
      help='Https only',
  )
  parser.add_argument(
      '-o',
      '--output_file',
      type=lambda p: Path(p).absolute(),
      help='Save list of proxies to file.',
  )

  if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)

  args = parser.parse_args()

  proxies = Proxies(
      country=args.country,
      anon=args.anon,
      https=args.https,
      debug=True,
  ).scrape()

  if args.output_file:
    with open(args.output_file, 'w') as f:
      for proxy in proxies:
        f.write(proxy + '\n')
    print('+ Saved proxy list to: %s' % args.output_file)

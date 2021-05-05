#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import pandas as pd
from tabulate import tabulate
import argparse


def get_proxies(anon_level, https_only):
    """
    gather proxies from free-proxy-list.net
    """
    
    url = "https://free-proxy-list.net/"
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')

    ip_port = []
    country = []
    anonymity = []
    https = []
    for row in rows:
        cols = row.find_all('td')
        try:
            ip_strip = cols[0].text.strip()
            port_strip = cols[1].text.strip()
            country_strip = cols[3].text.strip()
            anonymity_strip = cols[4].text.strip()
            https_strip = cols[6].text.strip()

            ip_port.append(f'{ip_strip}:{port_strip}')
            country.append(country_strip)
            anonymity.append(anonymity_strip)
            https.append(https_strip)
        except IndexError:
            continue

    df = pd.DataFrame(
        {'ip_port': ip_port,
         'country': country,
         'anonymity': anonymity,
         'https': https}
    )

    if anon_level == 1:
        anon_filt = ['elite proxy']
    if anon_level == 2:
        anon_filt = ['elite proxy', 'anonymous']
    if anon_level == 3:
        anon_filt = ['elite proxy', 'anonymous', 'transparent']

    if not https_only:
        https_filt = ['no', 'yes']
    if https_only:
        https_filt = ['yes']

    df = df[(df['anonymity'].isin(anon_filt)) & (df['https'].isin(https_filt))]

    return df


def get_working(df):
    """
    find working proxies
    """
    
    proxy_list = proxy_df['ip_port'].to_list()
    
    working = []
    def check_proxy(proxy_list):
        url = "https://httpbin.org/ip"
        try:
            r = requests.get(url, proxies={'http': proxy_list, 'https': proxy_list}, timeout=2)
            working.append(proxy_list)
        except:
            pass
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(check_proxy, proxy_list) 
    
    # filter out non working proxies
    df = proxy_df[proxy_df['ip_port'].isin(working)]
    
    # add working column
    df = df.reset_index()
    df['working'] = ['yes' for x in range(len(df))]
    df = df[['ip_port', 'country', 'anonymity', 'https', 'working']]
    
    return df


def console_print(df, ip_port=None):
    if ip_port:
        for i in df['ip_port'].to_list():
            print(i)
    else:
        print('')
        print(tabulate(df, headers='keys', tablefmt='basic', showindex=False))
        print('')

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--anonlevel', help='specify minimum proxy anonymity level (default = 2)', default = 2, type=int)
    parser.add_argument('-s', '--https', action='store_true', help='only select proxies that support https')
    parser.add_argument('-p', '--ip_port', action='store_true', help='only print list of working ip addresses and ports')

    args = parser.parse_args()
    anonlevel = args.anonlevel
    https_ssl = args.https
    ip_port = args.ip_port

    print('\n[+] Scraping proxies from https://free-proxy-list.net/....')

    proxy_df = get_proxies(anon_level = anonlevel, https_only = https_ssl)
    
    print(f"[+] Gathered {len(proxy_df['ip_port'])} unique proxies")


    print(f'\n[+] Checking each proxy at https://httpbin.org/ip....')

    working_proxies_df = get_working(df=proxy_df)

    print(f'[+] Found {len(working_proxies_df)} working proxies')


    print('\n[+] Working Proxies')

    console_print(df = working_proxies_df, ip_port=ip_port)

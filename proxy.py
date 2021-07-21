from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import argparse
import pandas as pd
import requests
import sys
import tabulate


def scrape_proxies(level, https) -> list:
    """Scrape proxy list from https://free-proxy-list.net/
    :level: minimum anonymity level (1 = transparent, 2 = anonymous, 3 = elite)
    :https: only select proxies that support https (True or False)
    :returns: list of dictionaries
    """
    proxy_list = []  # to store scraped ips and proxies
    # filters
    anon_filt = {
        1: ["elite proxy"],
        2: ["elite proxy", "anonymous"],
        3: ["elite proxy", "anonymous", "transparent"],
    }
    https_filt = {0: ["yes", "no"], 1: ["yes"]}
    country_blacklist = ["HK", "RU", "IR", "KP"]

    # scrape table
    url = "https://free-proxy-list.net/"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"[!] error scraping proxies: {r.status_code}")
        sys.exit(1)
    else:
        # parse proxies
        soup = BeautifulSoup(r.content, "html.parser")
        tbl_body = soup.find("tbody")
        tbl_rows = tbl_body.find_all("tr")

        for row in tbl_rows:
            cols = row.find_all("td")
            try:
                # extract values from table
                d = {
                    "ip_port": f"{cols[0].text.strip()}:{cols[1].text.strip()}",
                    "anon": cols[4].text.strip(),
                    "https": cols[6].text.strip(),
                    "country_code": cols[2].text.strip()
                }
                # apply filters
                if d["anon"] in anon_filt[level] and d["https"] in https_filt[https] and d["country_code"] not in country_blacklist:
                    proxy_list.append(d)
            except IndexError:
                continue

    return proxy_list


def console_print(proxy):
    """Console print format
    """
    print(
        f'[-] {proxy["ip_port"]}\t{proxy["anon"]}\t{proxy["https"]}\t{proxy["country_code"]}'.expandtabs(15))


def check_one(proxy) -> dict:
    """Check if proxy is working
    :proxy: dictionary {ip_port:x, anon:x, https:x, country_code:x} 
    """
    url = "https://httpbin.org/ip"
    r = requests.get(
        url, proxies={"http": proxy["ip_port"], "https": proxy["ip_port"]}, timeout=2)
    if r.status_code == 200:
        console_print(proxy)
        return proxy


def check_all(proxy_list) -> list:
    """Create thread pool to check all proxies
    :proxy_list: list of proxy dictionaries generated from scrape_proxies function
    """
    futures = []
    working = []

    with ThreadPoolExecutor() as executor:
        for proxy in proxy_list:
            future = executor.submit(check_one, proxy)
            futures.append(future)

        for future in futures:
            try:
                result = future.result()
                working.append(result)
            except:
                pass

    return working


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--https", action="count", default=0,
                        help="only select proxies that support https")
    parser.add_argument("-l", "--level", type=int, default=2,
                        help="minimum anonymity level - specify level (1 = transparent, 2 = anonymous, 3 = elite)", metavar='')
    parser.add_argument("-o", "--output", type=str,
                        help="save list of working proxies to txt file - specify path", metavar='')
    args = parser.parse_args()

    # scrape proxies
    scraped_proxies = scrape_proxies(level=args.level, https=args.https)

    # find working
    print(f"[+] total scraped proxies: {len(scraped_proxies)}")
    print("\n--- working proxies ---")
    print("                              anon level     https          country")
    working_proxies = check_all(scraped_proxies)

    # output list to file
    if args.output:
        with open(args.output, "w") as f:
            for proxy in working_proxies:
                f.write(str(proxy["ip_port"]) + '\n')
        print(f"\n[+] proxy list saved to: {args.output}")

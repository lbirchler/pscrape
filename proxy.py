#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import concurrent.futures

def get_proxies():
    """
    Gather level 1 and level 2 proxies from free-proxy-list.net
    """
    url = "https://free-proxy-list.net/"
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    
    proxies = []
    for row in rows:
        cols = row.find_all('td')
        try:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            anonymity = cols[4].text.strip()
            # only select level 1 and level 2 proxies
            if 'transparent' not in anonymity and 'level3' not in anonymity:
                proxies.append(f'{ip}:{port}')
        except IndexError:
            continue
        
    return proxies


def get_working(proxylist, limit=100):
    """
    Find working proxies
    """
    working = []
    def check_proxy(proxylist):
        url = "https://httpbin.org/ip"
        try:
            r = requests.get(url, proxies={'http': proxylist, 'https': proxylist}, timeout=2)
            working.append(proxylist)
        except:
            pass
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(check_proxy, proxylist[:limit]) 
    
    return working

working_proxy_list = get_working(get_proxies())

print(working_proxy_list)
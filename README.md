# proxy-scraper

script to generate a list of free and working proxies

---

## Installation

```bash
pip3 install -r requirements.txt
```

---

## Usage

```bash
usage: proxy.py [-h] [-l ANONLEVEL] [-s] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -l ANONLEVEL, --anonlevel ANONLEVEL
                        specify minimum proxy anonymity level (default = 2)
  -s, --https           only select proxies that support https
  -p, --ip_port         only print list of working ip addresses and ports
```

### Proxy Anonymity Levels

+ Transparent proxies (level 3)
    + Does not hide originating client IP Address
    + Headers sent to destination server
        + REMOTE_ADDR: proxy IP address
        + HTTP_VIA: proxy IP address
        + HTTP_X_FORWARDER_FOR: client IP address

+ Anonymous proxies (level 2)
    + Does not provide destination server with originating client IP address but does reveal that you are using a proxy server
    + Headers sent to destination server
        + REMOTE_ADDR: proxy IP address
        + HTTP_VIA: proxy IP address
        + HTTP_X_FORWARDER_FOR: proxy/random IP address

+ Elite proxies (level 1)
    + Hides originating client IP address and does not reveal to the destination server that you are using a proxy server
    + Headers sent to destination server
        + REMOTE_ADDR: proxy IP address (displaying as the client)
        + HTTP_VIA: null
        + HTTP_X_FORWARDER_FOR: null

---

## Examples


### All working proxies

```bash
$ python proxy.py 

[+] Scraping proxies from https://free-proxy-list.net/....
[+] Gathered 240 unique proxies

[+] Checking each proxy at https://httpbin.org/ip....
[+] Found 15 working proxies

[+] Working Proxies

ip_port               country       anonymity    https    working
--------------------  ------------  -----------  -------  ---------
202.61.51.204:3128    Pakistan      elite proxy  yes      yes
20.195.17.90:3128     Singapore     anonymous    yes      yes
193.56.157.39:8080    France        anonymous    yes      yes
180.128.1.83:8080     Thailand      anonymous    yes      yes
186.167.20.211:3128   Venezuela     anonymous    yes      yes
162.55.37.186:10071   Germany       anonymous    yes      yes
125.167.237.184:8080  Indonesia     anonymous    yes      yes
169.57.1.84:8123      Mexico        elite proxy  yes      yes
124.244.186.246:8080  Hong Kong     elite proxy  yes      yes
103.227.254.59:80     Indonesia     anonymous    no       yes
3.35.77.45:8080       Korea         elite proxy  no       yes
169.57.1.85:80        Mexico        elite proxy  yes      yes
8.210.71.64:3128      Hong Kong     anonymous    yes      yes
160.19.232.85:3128    South Africa  anonymous    yes      yes
193.168.153.165:8080  Turkey        elite proxy  yes      yes
```

### Level 1/HTTPS proxies

```bash
$ python proxy.py -l 1 -s

[+] Scraping proxies from https://free-proxy-list.net/....
[+] Gathered 69 unique proxies

[+] Checking each proxy at https://httpbin.org/ip....
[+] Found 6 working proxies

[+] Working Proxies

ip_port               country      anonymity    https    working
--------------------  -----------  -----------  -------  ---------
36.81.69.38:3128      Indonesia    elite proxy  yes      yes
169.57.1.84:8123      Mexico       elite proxy  yes      yes
124.244.186.246:8080  Hong Kong    elite proxy  yes      yes
194.5.206.148:3128    Netherlands  elite proxy  yes      yes
169.57.1.85:80        Mexico       elite proxy  yes      yes
41.217.219.53:31398   Malawi       elite proxy  yes      yes

```

### Print ip:port only

```bash
$ python proxy.py -l 1 -s -p

[+] Scraping proxies from https://free-proxy-list.net/....
[+] Gathered 75 unique proxies

[+] Checking each proxy at https://httpbin.org/ip....
[+] Found 16 working proxies

[+] Working Proxies

169.57.1.84:8123
198.50.163.192:3129
24.248.207.7:55443
186.159.3.41:30334
169.57.1.85:80
118.173.232.5:34413
144.217.101.245:3129
110.78.168.225:18960
51.222.67.208:32768
101.109.255.18:50538
59.94.176.111:3128
181.129.43.3:8080
51.222.67.214:32768
132.248.196.2:8080
51.222.67.220:32768
69.65.65.178:58389
```

---

### References
+ https://free-proxy-list.net/
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers


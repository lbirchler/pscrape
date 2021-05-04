# proxy-scraper

Python script that scrapes free proxies from the web, and makes use of concurrent futures to quickly check and generate a list of working proxies

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
[+] Gathered 273 unique proxies

[+] Checking each proxy at https://httpbin.org/ip....
[+] Found 23 working proxies

[+] Working Proxies

|    | ip_port              | country       | anonymity   | https   | working   |
|----|----------------------|---------------|-------------|---------|-----------|
|  0 | 194.5.206.148:3128   | Netherlands   | elite proxy | yes     | yes       |
|  1 | 202.61.51.204:3128   | Pakistan      | elite proxy | yes     | yes       |
|  2 | 169.57.1.84:8123     | Mexico        | elite proxy | yes     | yes       |
|  3 | 198.50.163.192:3129  | Canada        | elite proxy | yes     | yes       |
|  4 | 168.119.137.56:3128  | Germany       | elite proxy | yes     | yes       |
|  5 | 103.227.254.59:80    | Indonesia     | anonymous   | no      | yes       |
|  6 | 103.11.106.69:8181   | Indonesia     | anonymous   | no      | yes       |
|  7 | 24.248.207.7:55443   | United States | elite proxy | yes     | yes       |
|  8 | 183.88.186.101:8213  | Thailand      | anonymous   | no      | yes       |
|  9 | 3.35.77.45:8080      | Korea         | elite proxy | no      | yes       |
| 10 | 168.228.150.5:47507  | Brazil        | elite proxy | no      | yes       |
| 11 | 169.57.1.85:80       | Mexico        | elite proxy | yes     | yes       |
| 12 | 185.74.37.60:41258   | Italy         | elite proxy | yes     | yes       |
| 13 | 59.153.17.186:53281  | Bangladesh    | elite proxy | yes     | yes       |
| 14 | 36.81.69.38:3128     | Indonesia     | elite proxy | no      | yes       |
| 15 | 162.55.37.186:10071  | Germany       | anonymous   | yes     | yes       |
| 16 | 54.179.202.80:3128   | Singapore     | anonymous   | yes     | yes       |
| 17 | 193.56.157.39:8080   | France        | anonymous   | yes     | yes       |
| 18 | 59.94.176.111:3128   | India         | elite proxy | yes     | yes       |
| 19 | 80.211.179.30:3128   | Italy         | anonymous   | no      | yes       |
| 20 | 51.222.67.214:32768  | Canada        | elite proxy | yes     | yes       |
| 21 | 132.248.196.2:8080   | Mexico        | elite proxy | yes     | yes       |
| 22 | 116.90.229.186:35561 | Nepal         | elite proxy | no      | yes       |

```

### Level 1/HTTPS Proxies

```bash
$ python proxy.py -l 1 -s

[+] Scraping proxies from https://free-proxy-list.net/....
[+] Gathered 75 unique proxies

[+] Checking each proxy at https://httpbin.org/ip....
[+] Found 13 working proxies

[+] Working Proxies

|    | ip_port              | country              | anonymity   | https   | working   |
|----|----------------------|----------------------|-------------|---------|-----------|
|  0 | 202.61.51.204:3128   | Pakistan             | elite proxy | yes     | yes       |
|  1 | 169.57.1.84:8123     | Mexico               | elite proxy | yes     | yes       |
|  2 | 168.119.137.56:3128  | Germany              | elite proxy | yes     | yes       |
|  3 | 169.57.1.85:80       | Mexico               | elite proxy | yes     | yes       |
|  4 | 144.217.101.245:3129 | Canada               | elite proxy | yes     | yes       |
|  5 | 189.199.126.94:8080  | Mexico               | elite proxy | yes     | yes       |
|  6 | 110.78.168.225:18960 | Thailand             | elite proxy | yes     | yes       |
|  7 | 51.222.67.213:32768  | Canada               | elite proxy | yes     | yes       |
|  8 | 93.117.72.27:43631   | Moldova, Republic of | elite proxy | yes     | yes       |
|  9 | 188.0.138.11:8080    | Kazakhstan           | elite proxy | yes     | yes       |
| 10 | 210.48.204.134:46669 | Malaysia             | elite proxy | yes     | yes       |
| 11 | 132.248.196.2:8080   | Mexico               | elite proxy | yes     | yes       |
| 12 | 117.6.161.118:53281  | Vietnam              | elite proxy | yes     | yes       |

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

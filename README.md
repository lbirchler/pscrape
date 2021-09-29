# proxy-scraper

quickly generate a list of free and working proxies

---

## installation

```bash
pip install -r requirements.txt
```

---

## usage

```bash
usage: proxy.py [-h] [-s] [-l] [-o]

optional arguments:
  -h, --help      show this help message and exit
  -s, --https     only select proxies that support https
  -l , --level    minimum anonymity level - specify level (1 = transparent, 2 = anonymous, 3 = elite)
  -o , --output   save list of working proxies to txt file - specify path
```

### proxy anonymity levels

- transparent proxies (level 3)
    + headers sent to destination server
        + REMOTE_ADDR: proxy IP address
        + HTTP_VIA: proxy IP address
        + HTTP_X_FORWARDER_FOR: client IP address
        
- anonymous proxies (level 2)
    + headers sent to destination server
        + REMOTE_ADDR: proxy IP address
        + HTTP_VIA: proxy IP address
        + HTTP_X_FORWARDER_FOR: proxy/random IP address

- elite proxies (level 1)
    + headers sent to destination server
        + REMOTE_ADDR: proxy IP address (displaying as the client)
        + HTTP_VIA: null
        + HTTP_X_FORWARDER_FOR: null

---

## examples


### all working proxies

```bash
$ python proxy.py

[+] total scraped proxies: 248

--- working proxies ---
                              anon level     https          country
[-] 103.148.79.107:8080       elite proxy    yes            ID
[-] 95.216.10.237:6000        anonymous      yes            FI
[-] 124.40.252.182:8080       elite proxy    yes            ID
[-] 140.227.69.170:6000       elite proxy    no             JP
[-] 194.152.42.18:8080        elite proxy    yes            RO
...
```

### level 1 (elite) and https only 

```bash
$ python proxy.py -l1 -s

[+] total scraped proxies: 90

--- working proxies ---
                              anon level     https          country
[-] 124.40.252.182:8080       elite proxy    yes            ID
[-] 61.37.223.152:8080        elite proxy    yes            KR
[-] 14.161.108.88:55443       elite proxy    yes            VN
[-] 134.19.254.2:21231        elite proxy    yes            GE
[-] 195.7.9.141:8080          elite proxy    yes            IQ
...
```

### export list of proxies to txt file 

```bash
$ python proxy.py -l1 -s -o proxies.txt

[+] total scraped proxies: 90

--- working proxies ---
                              anon level     https          country
[-] 191.100.28.115:8080       elite proxy    yes            EC
[-] 181.129.140.83:35232      elite proxy    yes            CO
[-] 200.55.218.202:53281      elite proxy    yes            CL
[-] 45.76.23.147:3228         elite proxy    yes            US
[-] 124.40.252.182:8080       elite proxy    yes            ID
...

[+] proxy list saved to: proxies.txt
```

*list can be used to rotate requests through while web scraping*

```bash
$ cat proxies.txt 

124.40.252.182:8080
191.100.28.115:8080
200.55.218.202:53281
182.253.82.156:37242
181.129.140.83:35232
45.76.23.147:3228
14.161.108.88:55443
143.255.145.129:8080
78.186.215.167:9090
193.41.88.58:53281
213.203.177.218:443
208.80.28.208:8080
110.74.199.16:63141
187.111.160.6:8080
115.21.87.201:8080
45.42.177.21:3128
197.232.65.40:55443
112.78.170.27:8080
```

### references
+ https://free-proxy-list.net/
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers


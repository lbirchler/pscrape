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

[+] total scraped proxies: 284

--- working proxies ---
                              anon level     https          country
[-] 187.216.93.20:55443       elite proxy    no             MX
[-] 216.169.73.65:34679       elite proxy    no             US
[-] 103.139.98.82:3127        anonymous      no             ID
[-] 45.42.177.21:3128         elite proxy    no             US
[-] 117.102.81.3:53281        elite proxy    no             ID
[-] 103.147.73.115:3127       anonymous      no             ID
[-] 140.227.72.100:6000       elite proxy    no             JP
[-] 165.227.155.115:8888      elite proxy    yes            DE
[-] 144.217.101.245:3129      elite proxy    yes            CA
[-] 79.143.87.117:9090        anonymous      no             GB
[-] 201.81.38.123:8080        elite proxy    no             BR
[-] 134.19.254.2:21231        elite proxy    yes            GE
[-] 54.153.183.29:80          anonymous      yes            AU
[-] 119.81.189.194:80         elite proxy    yes            HK
[-] 165.22.248.186:1081       elite proxy    yes            SG
[-] 128.199.215.211:3128      elite proxy    yes            SG
[-] 118.99.103.35:32625       elite proxy    yes            ID
[-] 47.242.200.148:80         elite proxy    yes            HK
[-] 140.112.105.116:80        elite proxy    yes            TW
[-] 14.139.57.195:23500       elite proxy    yes            IN
[-] 197.210.217.66:34808      elite proxy    no             NG
[-] 95.216.10.237:6000        elite proxy    no             FI
[-] 51.222.21.94:32768        elite proxy    no             CA
[-] 161.202.226.194:80        elite proxy    yes            JP
[-] 169.57.1.85:80            elite proxy    yes            MX
[-] 128.199.214.87:3128       anonymous      yes            SG
[-] 182.52.51.10:61124        elite proxy    no             TH
[-] 119.82.252.76:51680       elite proxy    yes            KH
[-] 62.133.168.72:55443       elite proxy    yes            RU
[-] 112.78.170.27:8080        elite proxy    no             ID
[-] 178.218.216.125:8085      elite proxy    yes            RU
[-] 45.236.152.45:6666        elite proxy    no             BR
[-] 212.175.55.46:53281       anonymous      yes            TR
```

### level 1 (elite) and HTTPS only 

```bash
$ python proxy.py -l1 -s

[+] total scraped proxies: 91

--- working proxies ---
                              anon level     https          country
[-] 115.21.87.201:8080        elite proxy    yes            KR
[-] 91.121.132.164:8888       elite proxy    yes            FR
[-] 91.216.66.70:32306        elite proxy    yes            RU
[-] 201.81.38.123:8080        elite proxy    yes            BR
[-] 45.234.200.18:53281       elite proxy    yes            BR
[-] 47.245.33.211:8118        elite proxy    yes            JP
[-] 118.172.177.168:8080      elite proxy    yes            TH
[-] 144.217.101.245:3129      elite proxy    yes            CA
[-] 46.0.108.86:55443         elite proxy    yes            RU
[-] 119.81.189.194:80         elite proxy    yes            HK
[-] 14.139.57.195:23500       elite proxy    yes            IN
[-] 128.199.215.211:3128      elite proxy    yes            SG
[-] 169.57.1.85:80            elite proxy    yes            MX
[-] 200.32.51.179:8080        elite proxy    yes            AR
[-] 161.202.226.194:80        elite proxy    yes            JP
```

### export list of proxies to txt file 

```bash
$ python proxy.py -l1 -s -o proxies.txt

[+] total scraped proxies: 91

--- working proxies ---
                              anon level     https          country
[-] 91.121.132.164:8888       elite proxy    yes            FR
[-] 190.151.94.3:46615        elite proxy    yes            CL
[-] 140.227.72.100:6000       elite proxy    yes            JP
[-] 110.172.160.42:44047      elite proxy    yes            IN
[-] 195.170.38.230:8080       elite proxy    yes            RU
[-] 119.81.189.194:80         elite proxy    yes            HK
[-] 150.109.151.179:1081      elite proxy    yes            HK
[-] 165.22.248.186:1081       elite proxy    yes            SG
[-] 128.199.215.211:3128      elite proxy    yes            SG
[-] 169.57.1.85:80            elite proxy    yes            MX
[-] 161.202.226.194:80        elite proxy    yes            JP
[-] 200.32.51.179:8080        elite proxy    yes            AR
[-] 83.167.203.174:50128      elite proxy    yes            NL

[+] proxy list saved to: proxies.txt
```

*list can be used to rotate requests through while web scraping*

```bash
$ cat proxies.txt 

190.151.94.3:46615
91.121.132.164:8888
140.227.72.100:6000
110.172.160.42:44047
195.170.38.230:8080
150.109.151.179:1081
119.81.189.194:80
165.22.248.186:1081
128.199.215.211:3128
200.32.51.179:8080
83.167.203.174:50128
161.202.226.194:80
169.57.1.85:80
```

### References
+ https://free-proxy-list.net/
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers


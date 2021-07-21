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
[-] 109.86.152.78:55443       elite proxy    yes            UA
[-] 190.121.131.6:8080        anonymous      yes            CO
[-] 187.217.81.226:3128       anonymous      yes            MX
[-] 103.102.14.8:3127         anonymous      yes            ID
[-] 181.78.22.107:999         anonymous      yes            CO
[-] 103.109.57.1:8080         elite proxy    yes            BD
[-] 124.120.142.19:8080       anonymous      yes            TH
[-] 185.179.30.129:8080       anonymous      yes            AL
[-] 43.250.127.98:9001        anonymous      yes            MN
[-] 103.52.211.178:80         anonymous      yes            IN
[-] 45.174.248.70:999         anonymous      yes            MX
[-] 88.255.101.231:8080       anonymous      yes            TR
[-] 178.219.161.211:8080      anonymous      yes            UA
[-] 45.160.78.37:999          anonymous      yes            AR
[-] 189.206.34.154:3128       anonymous      yes            MX
[-] 103.161.165.18:8181       anonymous      yes            ID
[-] 103.144.77.211:8083       anonymous      yes            ID
[-] 91.194.53.33:9090         anonymous      yes            TR
[-] 190.214.27.106:48586      elite proxy    yes            EC
[-] 185.110.190.249:3128      elite proxy    yes            DE
[-] 116.193.191.116:80        anonymous      yes            ID
[-] 54.153.183.29:80          anonymous      yes            AU
[-] 134.19.254.2:21231        elite proxy    yes            GE
[-] 79.119.154.182:53281      elite proxy    yes            RO
[-] 110.74.222.71:44970       elite proxy    yes            KH
[-] 193.41.88.58:53281        elite proxy    yes            UA
[-] 103.6.104.104:38898       elite proxy    yes            PH
[-] 200.85.169.18:47548       elite proxy    yes            NI
[-] 195.7.9.141:8080          elite proxy    yes            IQ
[-] 45.76.156.143:8000        anonymous      yes            SG
[-] 37.228.65.107:32052       elite proxy    yes            KZ
[-] 213.203.177.218:443       elite proxy    yes            IT
[-] 208.80.28.208:8080        elite proxy    yes            US
[-] 110.44.124.220:55443      elite proxy    yes            NP
[-] 78.45.30.184:8080         elite proxy    yes            CZ
[-] 45.186.6.142:3128         anonymous      yes            EC
[-] 178.217.172.206:55443     elite proxy    yes            KG
[-] 144.217.101.245:3129      elite proxy    yes            CA
[-] 45.42.177.21:3128         elite proxy    yes            US
[-] 91.121.132.164:8888       elite proxy    yes            FR
[-] 103.147.73.115:3127       anonymous      yes            ID
[-] 115.21.87.201:8080        elite proxy    yes            KR
[-] 110.74.199.16:63141       elite proxy    yes            KH
[-] 27.112.68.164:55443       elite proxy    no             ID
[-] 190.7.141.66:47576        elite proxy    no             CO
[-] 178.134.155.82:48146      elite proxy    no             GE
[-] 103.28.242.180:55443      elite proxy    no             KH
[-] 154.72.199.202:41201      elite proxy    no             UG
[-] 50.246.120.125:8080       elite proxy    yes            US
[-] 200.148.169.234:8080      anonymous      yes            BR
[-] 157.65.170.120:3128       elite proxy    no             JP
[-] 201.132.155.198:8080      elite proxy    yes            MX
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
[-] 208.80.28.208:8080        elite proxy    yes            US
[-] 213.203.177.218:443       elite proxy    yes            IT
[-] 144.217.101.245:3129      elite proxy    yes            CA
[-] 115.21.87.201:8080        elite proxy    yes            KR
[-] 140.227.72.100:6000       elite proxy    yes            JP
[-] 152.204.128.46:33047      elite proxy    yes            CO
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
[-] 182.253.82.156:37242      elite proxy    yes            ID
[-] 143.255.145.129:8080      elite proxy    yes            BR
[-] 14.161.108.88:55443       elite proxy    yes            VN
[-] 78.186.215.167:9090       elite proxy    yes            TR
[-] 193.41.88.58:53281        elite proxy    yes            UA
[-] 208.80.28.208:8080        elite proxy    yes            US
[-] 213.203.177.218:443       elite proxy    yes            IT
[-] 45.42.177.21:3128         elite proxy    yes            US
[-] 115.21.87.201:8080        elite proxy    yes            KR
[-] 187.111.160.6:8080        elite proxy    yes            BR
[-] 110.74.199.16:63141       elite proxy    yes            KH
[-] 197.232.65.40:55443       elite proxy    yes            KE
[-] 112.78.170.27:8080        elite proxy    yes            ID

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


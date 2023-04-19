# pscrape

quickly generate a list of free and working proxies

---


## Installation

```
python3 -m pip install pscrape 
```

---

## Usage

```
>>> from pscrape import Proxies
>>>
>>> proxies = Proxies(country='US', anon='elite', https=True).scrape()
>>> proxies
['20.241.236.196:3128' '204.2.218.145:8080', '104.223.135.178:10000', '5.78.50.231:8888', '4.16.68.158:443' '104.148.86.58:3129']
```

**Proxies** class parameters:
- **country** (None | str, optional): Country ISO Code. Defaults to None.
- **anon** (None | str, optional): Anonymity level. Defaults to None.
    anonymous, elite, or transparent.
- **https** (bool, optional): Https only. Defaults to False.
- **debug** (bool, optional): Display scraped and validated proxies. Defaults to False.


### CLI
```
usage: pscrape [-h] [-c COUNTRY] [-a {anonymous,elite,transparent}] [--https]
                    [-o OUTPUT_FILE]

optional arguments:
-h, --help            show this help message and exit
-c COUNTRY, --country COUNTRY
                    Country ISO Code
-a {anonymous,elite,transparent}, --anon {anonymous,elite,transparent}
                    Anonymity level
--https               Https only
-o OUTPUT_FILE, --output_file OUTPUT_FILE
                    Save list of proxies to file.
```

Example:

```
$ pscrape -c US --https -o /tmp/proxies.txt
```

```
+ Total scraped proxies:  12
> 20.241.236.196:3128    | US  | anonymous    | https
> 204.2.218.145:8080     | US  | elite proxy  | https
> 104.223.135.178:10000  | US  | elite proxy  | https
> 5.78.50.231:8888       | US  | elite proxy  | https
> 4.16.68.158:443        | US  | elite proxy  | https
> 104.148.86.58:3129     | US  | elite proxy  | https
+ Total validated proxies: 6
+ Saved proxy list to: /tmp/proxies.txt
```

```
$ cat /tmp/proxies.txt
```

```
20.241.236.196:3128
204.2.218.145:8080
104.223.135.178:10000
5.78.50.231:8888
4.16.68.158:443
104.148.86.58:3129
```

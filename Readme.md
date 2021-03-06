Read the up to date information at: https://watchers.firosolutions.com/apidoc



## Description:
```
Json Rest API for viewing watcher and Vulnerability data

Url: https://api.firosolutions.com

```

## Vulns.firosolutions.com  
Is a webui using this api



## EndPoints

*  /timesearch

Description:
search within a time frame

Sample code:
```python
>>> import json, requests
>>> asd = requests.post("https://api.firosolutions.com/timesearch", json={'find':'wordpress', 'from':'2017-01-02 00:00:00', 'to':'2019-01-02 00:00:00','apikey':'myapikeygoeshere'})
```

Curl: 
```
curl https://api.firosolutions.com/timesearch -XPOST -H "Content-Type: application/json" -d '{"find":"wordpress", "from":"2016-01-02 00:00:00", "to":"2019-01-02 00:00:00", "apikey":"myapikeygoeshere"}
```

Extra:
This function is rate limited, it can only return a maxium value of 30 results and it's limited to returning only 1000
entries from the database, if it says it returns 1000 as total the value is in 99.99% more then that

*  /random   
```
Method: POST
keys: apikey

Description:
returns a random vulnerability
```


*  /cvesearch   

```
Method: POST
keys: apikey cve

Description:
find a CVE
```

```python

def cvesearch(cve):
	url = "https://api.firosolutions.com/cvesearch"
	aa = requests.post(url, json={"apikey":"mykeyhere", "cve":cve}).text
	return json.loads(aa)



```



*  /cveloosesearch    
```
Method: POST
keys: apikey search

Description:
Search for CVE

```


```python

def cveloosesearch(cve):
	url = "https://api.firosolutions.com/cveloosesearch"
	aa = requests.post(url, json={"apikey":"mykeyhere", "search":cve}).text
	return json.loads(aa)

```

*  /rustlibs
```
Method: POST
keys: apikey libraries

code example:

```
```python
import requests
requests.post('https://api.firosolutions.com/rustlibs', 
json={"apikey": "value", 
"libraries":{"name":"version", "asd":"0"}}).text



```

*  /nodejslibs
```
Method: POST
keys: apikey libraries


Description:
Queries our api for vulnerabilities in NodeJS libraries

```
```python
import requests
requests.post('https://api.firosolutions.com/nodejslibs', 
json={"apikey": "value", 
"libraries":
	{"ids-enterprise":"4.18.1", "ammonia":"0", "tay":"man"}
     }).text

```


*  /watchers/mywatchers


```
Method: Post
keys: apikey

Description:
List my watchers

Sample:

>>> print requests.post("https://api.firosolutions.com/watchers/mywatchers", json={"apikey":'mykey'}).text

{
  "watchers": [
    {
      "name": "Wordpres Blog",
      "validuntil": "Date is here"
    },

    {
      "name": "Rust Project",
      "validuntil": "20XX-XX-XX XX:XX:XX"
    }
  ]
}

```

*  /latesttwenty     

### Description:   
get the 20 latest vulns   

```python
import requests, json
zxc = requests.post("https://api.firosolutions.com/latesttwenty", json={"apikey": 'mykey'}).text
```



*  /latest

```python
Method: POST
Keys: apikey


Description:
Get the latest Vulnerability 

Sample code:
$ python3.6
Python 3.6.8 (default, Apr 13 2019, 18:58:09) 
[GCC 4.2.1 Compatible OpenBSD Clang 7.0.1 (tags/RELEASE_701/final)] on openbsd6
Type "help", "copyright", "credits" or "license" for more information.




import requests, json
zxc = requests.post("https://api.firosolutions.com/latest", json={"apikey": 'mykey'}).text
print(json.dumps(json.loads(zxc), indent=4))
{
    "latest": {
        "category": "XSS",
        "date": "2018-09-05 18:22:50",
        "info": "for more info use the dedicated search function",
        "title": "Fraction - Less critical - XSS vulnerability - SA-CONTRIB-2018-059"
    }
}
```



*  /watchers/watcher


```
Methods: POST
Keys: apikey watchername

Description:
Display watcher information

Sample:

>>> print requests.post("https://api.firosolutions.com/watchers/watcher", json={"apikey":"mykeyhere", "watchername":"test0"}).text


{
  "watcher": {
    "CMS": "Wordpress",
    "DataBase": "mysql",
    "Valid Until": "2019-02-15 21:52:39.390069",
    "WebServer": "apache",
    "name": "test0",
    "notsolved": 2,
    "solved_vulnerabilities": 5,
    "total": 7
  }
}

```



*  /watcher/vulns/solved


```
Keys: apikey watchername
Methods: POST

Description:
Display solved Vulnerabilities

Sample:
>>> print requests.post("https://api.firosolutions.com/watcher/vulns/solved", json={"apikey":"mykey", "watchername":""}).text

{
  "Solved Vulnerabilities": {
    "reported": [],
    "watchername": "vgf"
  }
}

```

*  /watcher/vulns/unsolved


```
Keys: apikey watchername
Methods: POST

Description:
Display unsolved Vulnerabilities

Sample:
>>> print requests.post("https://api.firosolutions.com/watcher/vulns/unsolved", json={'apikey':'myname', 'watchername':'watcher0'}).text


{
  "UnSolved Vulnerabilities": {
    "reported": [
      {
        "Date": "2019-01-15",
        "solved": "no",
        "title": "ModX Open Source CMS Babel Modules 3.0.0 Open Redirect",
        "watchername": "watcher0"
      },

	{
        "Date": "2019-01-20",
        "solved": "no",
        "title": "Joomla FPSS Art Frontpage Slideshow Components 1.6.0 Databas
e Disclosure  Open Redirection  SQL Injection",
        "watchername": "watcher0"
      }
    ],
    "watchername": "watcher0"
  }
}
 
```
                             
*  /luckysearch/


```
Keys: find apikey
Method: Post

Description:
Search endpoint for searching for Vulnerabilites, the amount of result
limit is set to 20

Curl:
curl --header "Content-Type: application/json" -XPOST --data '{"find":"rouncube","apikey":"myapikey"}'  https://api.firosolutions.com/luckysearch/


Sample:
>>> print json.loads(requests.post("https://api.firosolutions.com/watchers/mywatchers", json={"apikey:"mykey", "find":"roundcube"}).text).keys()
['found', 'total']

>>> print json.loads(requests.post("https://api.firosolutions.com/watchers/mywatchers", json={"apikey:"mykey", "find":"roundcube"}).text)['total']
6


>>> print json.loads(requests.post("https://api.firosolutions.com/watchers/mywatchers", json={"apikey:"mykey", "find":"roundcube"}).text)['found'][0].keys()
[u'category', u'description', u'author', u'recommendation', u'platform', u'link', u'published_date', u'title', u'cve', u'os', u'risk']


>>> print json.loads(requests.post("https://api.firosolutions.com/luckysearch/", json={"apikey": 'myapi', 'find':'roundcube'}).text)['found'][0]

{u'category': u'unset', 
u'description': u'Andrea Basile discovered that the <q>archive</q> plugin in roundcube, a\nskinnable AJAX based webmail solution for
 IMAP servers, does not\nproperly sanitize a user-controlled parameter, allowing a remote\nattacker to inject arbitrary IMAP commands and perform malicious\
nactions.\nFor the stable distribution (stretch), this problem has been fixedin\nversion 1.2.3+dfsg.1-4+deb9u2.\nWe recommend that you upgrade your roundcu
be packages.\nFor the detailed security status of roundcube please 
refer to its\nsecurity tracker page at:\nhttps://security-tracker.debian.org/tracker/roun
dcube\n\n\n', 
u'author': u'unset', 
u'recommendation': u'We recommend that you update your system', 
u'platform': u'roundcube', u'link': 
u"[u'https://www.debian.org/security/2018/dsa-4181', 'https://security-tracker.debian.org/tracker/s
ource-package/roundcube']", 
u'published_date': u'2017-09-27T13:37:00', u'title
': u'DSA-4181 roundcube', 
u'cve': u"[u'CVE-2018-9846', u'CVE-2018-9846']", u'os': u'Debian', 
u'risk': u'unset'}


```

*  /getvuln/


```
Keys: name apikey
Method: Post

Description:
Display information about a Single Vulnerability

Sample:
```

*  Error Codes:

```
Invalid keys:
	you have not provided the right name of the keys
```



*  To be implemented:


```
EndPoints:
	/watcher/addtowatcher
	/watcher/addemptywatcher
	/watcher/addwatcher

Planned Release:
	Zero-One

```

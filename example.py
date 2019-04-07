#python3.6                                                                    
import json, requests                                                         
                                                                              
APIKEY = "api key goes here"             
print('requesting')                                                           
find = 'roundcube'#= input('Search for: ')                                   
me = json.loads(requests.post("https://api.firosolutions.com/luckysearch/",  json={"apikey": APIKEY, 'find':find}).text)                                    
                                                                              
print("Found %s amount of results" % me.get('total'))                         
#dict_keys(['author', 'category', 'cve', 'description', 'link', 'os', 'platfor
m                                                                             
#', 'published_date', 'recommendation', 'risk', 'title'])                     
                                                                              
for nr,x in enumerate(me.get('found')):                                       
        print("Nr: %s \r\nTitle: %s \r\nDescription:\r\n %s \r\nLink: %s \r\nCVE: %s" % (nr, x.get('Title'), x.get('description'), x.get('link'),x.get('cve')))                                                                           

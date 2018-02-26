import requests
import random
import parser
from bs4 import BeautifulSoup

def get_a_proxy():
  proxies = {}
  r = requests.get("https://www.proxynova.com/proxy-server-list/")
  soup = BeautifulSoup(r.content, 'lxml')
  all_proxies = []
  for row in soup.find_all('tr')[1:]:
    try:
      ip_str = row.find_all('abbr')[0].script.string
      ip = ip_str[24:].split("'")[0] + ip_str[24:].split("'")[2]
      port = row.find_all('a')[0].text.strip()
      country = row.find_all('a')[1].text.strip()
      if "China" in country:
        continue
      if not port in ['80', '3128', '8080']:
        continue
      cur_proxy = "http://{}:{}".format(ip, port)
      all_proxies.append(cur_proxy)
    except:
      pass

  if not len(all_proxies):
    raise AssertionError('No proxy is valid')
  proxies['http'] = random.choice(all_proxies)
  return proxies

if __name__ == '__main__':
  print(get_a_proxy());
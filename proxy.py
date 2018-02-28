import requests
import random
import parser
import json
from bs4 import BeautifulSoup

def get_a_free_proxy():
  proxies = {}
  r = requests.get("https://www.proxynova.com/proxy-server-list/country-cn/")
  soup = BeautifulSoup(r.content, 'lxml')
  all_proxies = []
  for row in soup.find_all('tr')[1:]:
    try:
      ip_str = row.find_all('abbr')[0].script.string
      ip = ip_str[24:].split("'")[0] + ip_str[24:].split("'")[2]
      if row.find_all('td')[1].a:
        port = row.find_all('td')[1].a.string
      else:
        port = row.find_all('td')[1].string.strip()
      uptime = row.find_all('td')[4].find_all('span')[1].string.strip()[1:-1]
      
      cur_proxy = "http://{}:{}".format(ip, port)
      
      if(int(uptime) < 110):
        all_proxies.append(cur_proxy)
        # print('append proxy: {}, uptime: {}'.format(cur_proxy, uptime))
    except:
      pass

  if not len(all_proxies):
    raise AssertionError('No proxy is valid')
  proxies['http'] = random.choice(all_proxies)
  return proxies

def get_a_chinese_proxy():
  proxies = {}
  r = requests.get("https://www.kuaidaili.com/free/intr/")
  soup = BeautifulSoup(r.content, 'lxml')
  all_proxies = []
  for row in soup.find_all('tr')[1:]:
    try:
      ip = row.find_all('td')[0].string.strip()
      port = row.find_all('td')[1].string.strip()
      cur_proxy = "http://{}:{}".format(ip, port)
      all_proxies.append(cur_proxy)
    except:
      pass

  if not len(all_proxies):
    raise AssertionError('No proxy is valid')
  proxies['http'] = random.choice(all_proxies)
  return proxies

def get_a_check_url():
  urls = []
  check_url = 'http://www.mogumiao.com/proxy/checkIp/ipList?'
  r = requests.get("http://www.mogumiao.com/proxy/free/listFreeIp")
  data = json.loads(r.content)
  for item in data['msg']:
    ip = item['ip']
    port = item['port']
    proxy = "{}:{}".format(ip, port)
    urls.append("ip_ports[]={}".format(proxy))

  check_url += '&'.join(urls)
  return check_url

def get_a_premium_proxy(check_url):
  proxies = {}
  all_proxies = []
  r = requests.get(check_url)
  data = json.loads(r.content)
  for item in data['msg']:
    try:
      ip = item['ip']
      port = item['port']
      time_str = item['time']
      time = int(time_str[:-2])
      proxy = 'http://{}:{}'.format(ip, port)
      if (time < 350):
        all_proxies.append(proxy)
      # else:
      #   print(proxy, 'timeout:{}'.format(time_str))
    except:
      pass
      # print('{}:{} request timeout'.format(ip, port))
  return random.choice(all_proxies)

def get_a_proxy():
  check_url = get_a_check_url();
  proxy = get_a_premium_proxy(check_url)
  return proxy

if __name__ == '__main__':
  print(get_a_proxy())
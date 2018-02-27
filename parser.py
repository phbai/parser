import proxy
import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup

def parse(url, proxies=None):
  r = None
  if proxies:
    try:
      r = requests.get(url, proxies=proxies, timeout=1.5)
    except Timeout:
      return 'Connection time out'
  else:
    r = requests.get(url)

  html = r.content.decode('utf-8')
  soup = BeautifulSoup(html, 'lxml')

  title = soup.title.string.split('\n')[0].strip()
  try:
    download_url = soup.source['src']
    return download_url
  except:
    return 'failed to get the link'

if __name__ == '__main__':
  # ip = '123.55.3.96'
  # port = 48487
  # a_proxy = {'http': 'http://{}:{}'.format(ip, port)}
  a_proxy = proxy.get_a_premium_proxy()
  print(a_proxy)
  # print(parse('http://myip.ipip.net', a_proxy));
  print(parse('http://91.91p30.space/view_video.php?viewkey=10dbdc2e848c104e5f3c', a_proxy));
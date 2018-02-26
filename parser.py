import proxy
import requests
from bs4 import BeautifulSoup

def parse(url, proxies=None):
  if proxies:
    r = requests.get(url, proxies=proxies)
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
  a_proxy = {'http': 'http://124.192.39.248:3128'}
  # a_proxy = proxy.get_a_proxy()
  print(a_proxy)
  print(parse('http://91.91p30.space/view_video.php?viewkey=10dbdc2e848c104e5f3c', a_proxy));
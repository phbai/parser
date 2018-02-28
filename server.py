import redis
import time
import proxy

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def set_a_proxy(proxy):
  r.set('proxy', proxy, ex=60)

def get_a_proxy():
  try:
    proxy = r['proxy']
    return proxy, 'ok'
  except:
    return 'get proxy failed', 'failed'

def get_redis_proxy():
  proxy_url, status = get_a_proxy()
  if(status == 'ok'):
    return proxy_url
  else:
    a_proxy = proxy.get_a_proxy()
    set_a_proxy(a_proxy)
    print('set proxy succeed {}'.format(a_proxy))
    return a_proxy

if __name__ == '__main__':
  print(get_redis_proxy())
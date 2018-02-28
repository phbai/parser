from flask import Flask, request
import parser
import server
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'visit /get?url=http://91.91p30.space/view_video.php?viewkey=10dbdc2e848c104e5f3c'

@app.route('/get')
def get_url():
  proxy_url = server.get_redis_proxy()
  proxy = {'http': proxy_url}
  url = request.args.get('url')
  result, status = parser.parse(url, proxy)

  if status:
    return jsonify({'status': 'failed', 'result': result})
  else:
    return jsonify({'status': 'ok', 'result': result})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
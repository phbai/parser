from flask import Flask, request
import parser
import proxy
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'visit /get?url=http://xxxx'

@app.route('/get')
def get_url():
  a_proxy = proxy.get_a_premium_proxy()
  url = request.args.get('url')
  result, status = parser.parse(url, a_proxy)

  if status:
    return jsonify({'status': 'failed', 'result': result})
  else:
    return jsonify({'status': 'ok', 'result': result})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
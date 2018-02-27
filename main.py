from flask import Flask, request
import parser
import proxy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'visit /get?url=http://xxxx'

@app.route('/get')
def get_url():
    a_proxy = proxy.get_a_premium_proxy()
    url = request.args.get('url')
    return parser.parse(url, a_proxy)

if __name__ == '__main__':
    app.run()
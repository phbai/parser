from flask import Flask, request
import parser

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = request.args.get('url')
    return parser.parse(url)

if __name__ == '__main__':
    app.run()
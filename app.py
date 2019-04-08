from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello():
    print(request.json)
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

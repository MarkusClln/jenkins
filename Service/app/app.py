from flask import Flask, request, Response
import os

app = Flask(__name__)
SERVICE_NAME = os.getenv('SERVICE_NAME')


@app.route('/', methods=['GET'])
def say_hello():
    return "Hello " + SERVICE_NAME

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
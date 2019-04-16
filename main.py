from flask import Flask, render_template,request, jsonify
import threading
import speech
import time
import json
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

data = {}


@app.route('/')
def hello():
    print("run runrun")
    return render_template('index.html')


@app.route('/background_process_test', methods=['POST'])
def background_process_test():
    print("Hello！！！！！！！！！")
    global data
    data = speech.main()
    print(data)


@app.route('/getdata')
def get_data():
    print("get data！！！！！！！！！")
    global data
    print("cur data", data)
    # data = {'name': "John", 'age': 31, 'city': "New York"}
    # res = data['score']
    # print("res", res)
    return jsonify(data), 201


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

from flask import Flask, session, render_template
from flask_socketio import SocketIO, emit
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = 'TNT'
socketio = SocketIO(app)

IP = '115.145.113.117'
PORT = '5080'


result = {}
@socketio.on('submit')
def submit(message):
    result[message['name']] = message['score']
    #emit('response', {'data':'{} Submit'.format(message['name'])}, broadcast=True)
    emit('response', {'data':message}, broadcast=True)
    emit('result', {'data' : result}, broadcast=True)


@app.route('/')
def get_index():
    print(result)
    return render_template(
        'index.html',
        ip = IP,
        port = PORT)


if __name__ == '__main__':
    socketio.run(app, host=IP, port=int(PORT), debug=True)

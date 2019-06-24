from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

client = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

@socketio.on('getClientList')
def on_message(message):
    emit('my response', client)

@socketio.on('daftar')
def on_message(message):
    client[request.sid] = message
    emit('clientConnect', {
        "msg" : message + " connected",
        "jumlah" : len(client)
    }, broadcast = True, include_self = False)

    print(len(client))

@socketio.on('connect')
def on_connect():    
    print(request.sid + ' connected')
    
@socketio.on('disconnect') 
def on_disconnect():
    print('disconnected')
    # emit('clientDc', "disconnected" + client[request.sid], broadcast = True, include_self = False)
    emit('clientConnect', {
        "msg" : client[request.sid] + " disconnected",
        "jumlah" : len(client)
    }, broadcast = True, include_self = False)
    # print(client)
    del client[request.sid]
    print(len(client))
    # print(len(client))

if __name__ == '__main__':
    socketio.run(app)
import socketio
import uuid

# standard Python
sio = socketio.Client()
ID = str(uuid.uuid4())
# print (ID)
# ID = 'aabb'
# exit()

@sio.on('clientDc')
def on_message(data):
    print(data)

@sio.on('clientConnect')
def on_message(data):
    print(data)

@sio.on('connect')
def on_connect():
    print('connected')
    # print sio.sid
    sio.emit('daftar', ID)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected')

if __name__ == '__main__':
    
    # sio.connect('http://localhost:5000')
    sio.connect('http://socket.muhammadhilman.com')
    sio.wait()
    print("A")


# print('my sid is', sio.sid)


# print('a')
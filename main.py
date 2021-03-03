from flask import Flask
from flask_socketio import SocketIO, send, emit
from settings import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

@socketio.on('messsage')
def handleMessage(msg):
    print("Message : ".format(msg))
    # on envoie à tous les clients graçe au broadcast = True
    send(msg, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


def main():
    socketio.run(app)


if __name__ == '__main__':
    main()

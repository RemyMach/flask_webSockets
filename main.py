from flask import Flask
from flask_socketio import SocketIO, send, emit
from settings import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('addMesssage')
def handleMessage(msg):
    print("Message : ".format(msg))
    # on envoie à tous les clients graçe au broadcast = True
    send(msg, broadcast=True)

@socketio.emit('pomme')
def emitexemple():
    emit('je suus une pomme', broadcast=False)


def main():
    socketio.run(app)


if __name__ == '__main__':
    main()

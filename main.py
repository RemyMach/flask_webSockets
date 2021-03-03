from flask import Flask
from flask_socketio import SocketIO, send, emit
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')
socketio = SocketIO(app)

@socketio.on('messsage')
def handleMessage(msg):
    print("Message : ".format(msg))
    # on envoie à tous les clients graçe au broadcast = True
    send(msg, broadcast=True)


def main():
    socketio.run(app)


if __name__ == '__main__':
    main()

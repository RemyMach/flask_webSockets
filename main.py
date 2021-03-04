from flask import Flask
from flask_socketio import SocketIO, send, emit
from settings import SECRET_KEY
import sys
from entity.Message import Message

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('addMessage')
def handle_message(message_received):
    message = Message(message_received)
    print("received message : {}".format(message.fieldMessage))
    # on envoie à tous les clients graçe au broadcast = True
    robot_message = Message()
    robot_message.fieldMessage = "je suis un petit robot"
    send(message.toJson(), broadcast=True)

    emit('newRobotMessage', robot_message.toJson())


if __name__ == '__main__':
    socketio.run(app)

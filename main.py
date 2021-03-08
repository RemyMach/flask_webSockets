from flask import Flask, request
from flask_socketio import SocketIO, send, emit
from settings import SECRET_KEY, MY_JWT_SECRET_KEY
import sys
from datetime import datetime
from entity.Message import Message
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["JWT_SECRET_KEY"] = MY_JWT_SECRET_KEY

socketio = SocketIO(app, cors_allowed_origins='*')
jwt = JWTManager(app)

UsersConnected = {}

@socketio.on('connect')
def test_connect():
    currentSocketId = request.sid
    emit('firstConnection', {'data': {'message': 'You are connected', 'chat_id': currentSocketId}})
    print("socket_id -> {} ".format(currentSocketId))
    UsersConnected[currentSocketId] = 1

@socketio.on('addMessage')
def handle_message(data):
    UsersConnected[data['chat_id']]  = UsersConnected[data['chat_id']]+ 1
    message = Message({'fieldMessage': data['fieldMessage'] ,'idUser': data['idUser']})
    emit('UsersConnected', UsersConnected[data['chat_id']])
    print("received message : {}".format(message.fieldMessage))
    robot_message = Message()
    robot_message.fieldMessage = "je suis un petit robot"
    robot_message.idUser = 1
    emit('newRobotMessage', robot_message.toJson())

@socketio.on('disconnect')
def test_disconnect():
    currentSocketId = request.sid
    del UsersConnected[currentSocketId]
    print('Client disconnected')



if __name__ == '__main__':
    global count_user
    socketio.run(app)

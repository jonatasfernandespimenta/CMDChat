import socketio
import json
import utils.globals as g
from commands import commands

sio = socketio.Client()
server = input('Insert the server IP: ')
port = input('Insert the server port: ')

username = input("Enter your username: ")

notify = False

@sio.event
def disconnect():
    sio.emit('exit', username)

@sio.on('enter')
def on_enter(data):
    print(data)
    for i in data:
        value = json.loads(i)
        print(value['user'] + ": " + value['message'])

@sio.on('messages')
def on_messages(data):
    i = len(data) - 1
    value = json.loads(data[i])
    if(value['user'] != username):
        if(g.notify):
            print('\a')
        print(value['user'] + ": " + value['message'])

@sio.event()
def send_message(message):
    sio.emit('message', json.dumps({'message': message, 'user': username}))


sio.connect('http://' + server + ':' + port)
sio.sleep(2)

while True:
    message = input('\n> ')
    if(message != ''):
        if(message[0] == '/'):
            commands(message, send_message)
        else:
            send_message(message)

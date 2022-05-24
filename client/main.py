import socketio
import json
import utils.globals as g
from commands import commands
import time

sio = socketio.Client()
server = input('Insert the server IP: ')
port = input('Insert the server port: ')

g.username = input("Enter your username: ")

print('\n')

@sio.event
def disconnect():
    sio.emit('exit', g.username)

@sio.on('left')
def on_left(data):
    print(data)

@sio.on('entered')
def on_entered(data):
    print(data)

@sio.on('enter')
def on_enter(data):
    for i in data:
        value = json.loads(i)
        print(value['user'] + ": " + value['message'])

@sio.on('messages')
def on_messages(data):
    i = len(data) - 1
    value = json.loads(data[i])
    if(value['user'] != g.username):
        if(g.notify):
            print('\a')
        print(value['user'] + ": " + value['message'])

@sio.event()
def clear():
    sio.emit('clear')

@sio.event()
def join():
    sio.emit('join', g.username)

@sio.event()
def send_message(message):
    sio.emit('message', json.dumps({'message': message, 'user': g.username}))


sio.connect('http://' + server + ':' + port)
sio.sleep(2)

join()
time.sleep(1)
while True:
    message = input('\n> ')
    if(message != ''):
        if(message[0] == '/'):
            commands(message, send_message, clear)
        else:
            send_message(message)

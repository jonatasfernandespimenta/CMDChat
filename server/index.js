var express = require('express'),
    app = express(), 
    server = require('http').createServer(app)

server.listen(3001);

const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

let messages = [];

io.on("connection", (socket) => {
  socket.on('join', (args) => {
    io.emit('entered', args + ' joined the chat');
  });

  socket.on('exit', (args) => {
    io.emit('left', args + ' left the chat');
  });

  socket.on('clear', () => {
    messages = [];
  });

  socket.emit('enter', messages);

  socket.on("message", (args) => {
    messages.push(args);
    console.log(messages.length);

    // emit to all clients
    io.emit('messages', messages);
  });
});

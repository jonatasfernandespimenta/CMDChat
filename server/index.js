var express = require('express'),
    app = express(), 
    server = require('http').createServer(app)

server.listen(3001);

const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

const messages = [];

io.on("connection", (socket) => {
  io.emit("someone connected");

  socket.on('exit', (args) => {
    io.emit(args.user + ' has left');
  });

  socket.emit('enter', messages);

  socket.on("message", (args) => {
    messages.push(args);
    console.log(messages.length);

    // emit to all clients
    io.emit('messages', messages);
  });
});

from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    if (not session.get('name')):
        msg = "You"
    else:
        msg = session.get('name')
    emit('status', {'msg': msg + ' have entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    if (not session.get('name')):
        msg = "You"
    else:
        msg = session.get('name')
    emit('message', {'msg': msg + ': ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    if (not session.get('name')):
        msg = "You"
    else:
        msg = session.get('name')
    emit('status', {'msg': msg + ' has left the room.'}, room=room)


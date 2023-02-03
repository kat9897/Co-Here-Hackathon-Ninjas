from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from .project import *


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
    """Sent by a client when the user entered a new message and hits the Enter key.
    The message is sent to all people in the room."""
    room = session.get('room')
    msg = message['msg']
    if (not session.get('name')):
        user = "You"
    else:
        user = session.get('name')
    send_message(user + ": " + msg, room)
    #emit('message', {'msg': user + ': ' + msg}, room=room)
    #print("Person's message: " + msg)
    therapist_res = therapist(msg)
    #print("Therapist: " + therapist_res)
    send_message("Therapist: " + therapist_res, room)
    #emit('message', {'msg': "Therapist: " + therapist_res}, room=room)


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

def send_message(text, room):
    emit("message", {"msg": text}, room=room)
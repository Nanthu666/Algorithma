import socketio
import random
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected.")

@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected.")

@sio.event
def send_random_value(sid,data):
    # random_value = random.randint(1, 100)
    print(f"Sending random value {data} to client {sid}.")
    sio.emit('random_value', data, room=sid)

if __name__ == '__main__':
    try:
        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
    except Exception as e:
        print(f"An error occurred: {e}")
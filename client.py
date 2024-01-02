import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("connected server")

@sio.event
def disconnectconnect():
    print("disconnected server")

@sio.on('random_value')
def recive_random_value(data):
    print(f'recive randam value from server:{data}')

if __name__ == '__main__':
    server_adress ='http://localhost:5000'
    sio.connect(server_adress)

    while True:
        s=input("press enter to request a random value from the server (Q to quit): ")
        sio.emit("send_random_value",s)
import socketio

class JetsonSocket:
    def __init__(self,ip_adress):
        self.sio = socketio.Client()
        self.sio.connect(ip_adress)

    def send(self, msg,data):
        self.sio.emit(msg,data)

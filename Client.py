
import socket
import pickle

diachi_server = ('localhost',9050)

class person():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    def __str__(self):
        return "{} - {} - {}".format(self.id, self.name, self.age)

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(diachi_server)
    while True:
        # Gui 1:
        data = input('Nhap id:')
        sk.send(str.encode(data))
        if data == 'bye':
            break
        # Nhan 2:
        data = sk.recv(1024)
        data = pickle.loads(data) # Doc 1 doi tuong bat ki tu dang byte
        print('Server:',data)
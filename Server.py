
import socket
import threading
import pickle

diachi_server = ('localhost',9050)

class person():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

def thread_client(client_sk, client_addr):
    while True:
        # Nhan 1:
        data = client_sk.recv(1024).decode('utf-8')
        print('Client {}:{}'.format(client_addr, data))
        if data == 'bye':
            client_sk.close()
            break
        # Kiem tra id:
        index = -1
        for i in range(len(lstPerson)):
            if str(lstPerson[i].id)==str(data).strip():
                index = i
                break
        # Gui 2
        if index == -1: # khong tim thay doi tuong, gui lai msg
            client_sk.sendall(pickle.dumps(data))
        else:
            data = pickle.dumps(lstPerson[index]) # chuyen doi tuong x -> byte
            client_sk.sendall(data)

if __name__=='__main__':
    p1 = person(1, 'Dung', 21)
    p2 = person(2, 'Hien', 22)
    p3 = person(3, 'Chinh', 23)
    p4 = person(4, 'John', 21)
    p5 = person(5, 'Tuan', 20)
    p6 = person(6, 'Lan', 18)
    lstPerson = [p1, p2, p3, p4, p5, p6]
    
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(diachi_server)
    sk.listen(5)
    print('Server listening...')
    while True:
        client_sk, client_addr = sk.accept()
        thread = threading.Thread(target=(thread_client), args=[client_sk, client_addr], daemon=1)
        thread.start()
import zmq

def create_socket():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("epgm://192.168.1.18:5555")
    return socket

def send_data(filename, socket):
    with open(filename) as log_file:
        for line in log_file:
            socket.send(line)

def main():
    socket = create_socket()
    import time
    time.sleep(1)
    send_data('/var/log/dmesg', socket)

if __name__ == '__main__':
    main()

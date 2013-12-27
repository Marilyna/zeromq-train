import zmq

def create_socket():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    # socket.bind("tcp://127.0.0.1:5000")
    socket.bind("epgm://192.168.1.35:5555")
    return socket

def send_data(filename, socket):
    with open(filename) as log_file:
        for line in log_file:
            # print ">> " + line
            socket.send(line)

def main():
    socket = create_socket()
    import time
    time.sleep(1)
    send_data('/var/log/system.log', socket)

if __name__ == '__main__':
    main()

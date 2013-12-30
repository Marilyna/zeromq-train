import time

import zmq


def create_socket():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5555")
    return socket


def send_data(filename, socket):
    sent = 0
    start = time.time()
    # sending messages during 1 sec
    while time.time() - start < 1:
        with open(filename) as log_file:
            for line in log_file:
                socket.send(line)
                sent += 1
                # if sent % 96 == 0:
                #     time.sleep(.01)
    print "Total sent:", sent


def main():
    socket = create_socket()
    # wait for 1 sec till subscribers connect to the socket
    time.sleep(1)
    now = time.time()
    send_data('/var/log/system.log', socket)
    print "Spent:", time.time() - now


if __name__ == '__main__':
    main()

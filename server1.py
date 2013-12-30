import zmq
 
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, "")
 
print "Server1 is waiting\n"
received = 0
try:
    while True:
        with open('./server-log', 'a') as server_log:
            message = socket.recv()
            server_log.write(message)
            received += 1
except KeyboardInterrupt:
    print "Total received:", received
    raise

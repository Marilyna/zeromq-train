import zmq
 
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, "")
 
print "Server2 is waiting\n\n"
received = 0
try:
    while True:
        message = socket.recv()
        print message,
        received += 1
except KeyboardInterrupt:
    print "\n\nTotal received:", received
    raise

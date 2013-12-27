import zmq
 
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("epgm://192.168.1.18:5555")
socket.setsockopt(zmq.SUBSCRIBE, "")
 
print "Server2 is waiting"
while True:
    message = socket.recv()
    print "Received request: ", message

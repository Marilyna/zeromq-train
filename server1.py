import zmq
 
context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.connect("tcp://127.0.0.1:5000")
socket.connect("epgm://192.168.1.35:5555")
socket.setsockopt(zmq.SUBSCRIBE, "")
 
while True:
    message = socket.recv()
    print "Received request: ", message
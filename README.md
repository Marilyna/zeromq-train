zeromq-train
============

A simple example of using ØMQ with Python.

1 publisher (client) and 2 subscribers (server1, server2).
The client publishes text messages into a socket and two servers receive them: server1 - writes messages to a file,
server2 - writes messages to shell.

Testing
=======

The scripts were tested locally on my MacBook Air, 8 Gb memory, Intel i5-4250U

Experiments
===========

Received messages without errors (all sent messages were received)

| Time | Messages   | Messages/s |
| ---- | ---------- | ---------- |
| 1 s  | 10064      | 10064     |
| 5 s  | 48800      | 9760      |
| 10 s | 82908      | 8291      |


Maximum amount of sent and received messages

| Time | Sent    | Server1 | Server2 | Server1/s | Server2/s |
| ---- | ------- | ------- | ------- | --------- | --------- |
| 1 s  | 262656  | 12533   | 54007   | 12533     | 54007     |
| 5 s  | 1319544 | 28501   | 262018  | 5700      | 52404     |
| 10 s | 2669350 | 55510   | 495501  | 5551      | 49550     |


The longer messages are being sent, the fewer messages per second are received. The amount of received messages depends
on queue size (how many messages can be buffered before processing), subscribers hardware (how quickly a subscriber can
process a message) and network capacity.

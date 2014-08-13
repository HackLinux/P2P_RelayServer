P2P_RelayServer
===============

Allow clients to connect with one anther by using a server as the mediator for the devices.

At the moment the server(relay.py) will listen for incoming connecting devices, but the python script is not setup to help devices find each other. 

The clients can communicate with each other only if they are on the same machine. But with the code available you code access people on a local network. To send messages with the client.py open terminal and issue the commands below to send to another terminal on the same machine.

If you don't know much about how to configure the ip and port, use the defaults shown below. To end a connection with the other terminal window, enter the word 'end' and both connections will be closed.

Switches explained
   - -p the port in which the host(which is you) allows for the client to connect to
   - -c the client ip:port which you want to connect to

Terminal 1
```sh
python client.py -c 127.0.0.1:5001 -p 5002
```
Terminal 2
```sh
python client.py -c 127.0.0.1:5002 -p 5001
```
# Python Live Video Stream

Streaming live video using Python sockets over the local network. It allows the sender and receiver to get connected over a common network for video streaming. 
In this case, for the sake of simplicity, only one-way video sharing is developed, such that if person A is the sender so in that case, person B will be the receiver.
By, enhancing it we can create a video call system with bi-way audio and video streaming. With some customizations, it can be used to send photos instead of video streams.

# Working

## Sender [or Server]
1. Creation of Socket Object uisng socket.socket(socket.AF_INET, socket.SOCK_STREAM), here AF_INET refers to the address-family ipv4 and SOCK_STREAM means connection-oriented TCP protocol. 
2. Extraction of Host IP using getsockname() method.
3. Then binding method bind(), is called, which binds it to a specified IP and port so that it can listen to incoming requests on that IP and port.
4. Once the binding is done, the server starts listening using listen() method has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections. In this case, it can have 5 connections at most.
5. Then, the establishment of the connection between the client and server takes place, using accept() method
6. Now, if some client XYZ is available, then the video stream will start on the Server using OpenCV
7. After that each frame (also known as an image) will be converted to a pickle object using the dump() method, which creates a byte stream, which is required by the receiver.
8. Also, the calculation of the length of the byte stream (pickle object) is performed using the len() method.
9. Then the calculated length (in int) is converted to bytes using the pack() method of the Struct module which can convert Python values to C structs and vice-versa.
10. Then message packet is created as struct.pack("Q", len(a)) + a [note both are byte stream, where the first 8 bytes is the length of the message and after that message is appended, that is '+ a' ]
11. Finally the packet (message/video) is sent using the sendall() method
12. From step 5, the process is repeated again and again till the time client or server exits or some exception happens.

## Reciever [or Client]
1. Creation of Socket Object takes place
2. Sender's IP address (Server) is taken as input
3. Then connections are established which connect a TCP-based client socket to a TCP-based server socket. 
4. After that, the standard payload size is calculated and set. In this case, it's 8 bytes only (fixed).
5. Then data is received in such a way that no packet is truncated. For that, first, an empty data var is initialized, after that its compared to the payload size
6. If it's less than the payload size using the recv() method, the packet is received
7. It's again checked if the received data is a packet or not
8. If it's a packet, it's appended to the data variable.
9. Now from the data variable, the packed message size (length of data in byte stream) and actual data (in byte stream) are extracted
10. Then packed message size is unpacked using unpack() method and is converted to an integer.
11. Again the length is checked and actual data is converted to frame using the loads() method
12. Finally output is displayed and the process is repeated again and again till the time client or server exits or some exception happens.

## Tools and Technologies Used:

### Python Modules used:
- socket: For providing connectivity over the network between devices using socket programming
- OpenCV: For image capturing and display
- pickle: To convert frames to byte stream and vice-vera
- struct: To convert data to byte stream and vice-versa

### Softwares Used 
- Spyder 5.0.3
- CMD
- Git Bash

### OS Used:
- Windows 10 
- RHEL 8.4

## Feature(s)  
- Live video streaming over LAN, using socket programming in python

## Demo Video: 

# Thank you
- Thank you all for using my app.
- All suggestions are warmly welcomed.


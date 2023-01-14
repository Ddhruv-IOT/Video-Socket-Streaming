# Python Live Video Stream

Stream live video using Python sockets over the local network. It allows the sender and the receiver to stream video while connected to the same network. 
In this case, for the sake of simplicity, only one-way video sharing is developed, such that if person A is the sender so in that case, person B will be the receiver.
With some customizations and enhancements, it can be used to develop a video calling system with bi-way audio-video streaming and photo sharing.

# Working

## Sender [or Server]
1. Creation of Socket Object uisng socket.socket(socket.AF_INET, socket.SOCK_STREAM), here AF_INET refers to the address-family ipv4 and SOCK_STREAM means connection-oriented TCP protocol. 
2. Extraction of Host IP using getsockname() method.
3. Then binding method bind() is called, which binds it to a specified IP and port so, that it can listen to incoming requests on that IP and port.
4. Once the binding is over. The server starts listening using the listen() method having a backlog parameter. It specifies the number of unaccepted connections the system will allow before refusing new connections. In this case, it can have five connections at most.
5. Then, the establishment of the connection between the client and server takes place using accept() method
6. Now, if some client XYZ is available, then the video stream will start on the server using OpenCV
7. After that, each frame (also known as an image) will be converted to a pickle object using the dump() method that creates a byte stream required by the receiver.
8. Also, the length of the byte stream (pickle object) is calculated using the len() method and is converted to bytes using the pack() method of the Struct module.
9. Then message packet is created as a struct.pack("Q", len(a)) + a [note both are byte stream, where the first 8 bytes is the length of the message and after that message is appended that is '+ a' ]
10. Finally, the packet (message/video) is sent using the sendall() method
11. From step 5, the process is repeated until the client or server exits or some exception happens.

## Reciever [or Client]
1. Creation of Socket Object takes place
2. Sender's IP address (Server) is taken as input
3. After that, the connection is established which connects a TCP-based client socket to a TCP-based server socket. 
4. The standard payload size is 8 bytes only (fixed).
5. The data is received in a way such that no packet is truncated. For that, first, an empty data var is initialized, after that its compared to the payload size
6. If it's less than the payload size using the recv() method, the packet is received
7. It's again checked if the received data is a packet or not
8. If it's a packet, it's appended to the data variable.
9. Now from the data variable, the packed message size (length of data in byte stream) and actual data (in byte stream) are extracted
10. Then packed message size is unpacked using unpack() method and is converted to an integer.
11. Again the length is checked and actual data is converted to frame using the loads() method
12. Finally, the output is displayed and the process is repeated until the client or server exits or some exception happens.

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

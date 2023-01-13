# Python Live Video Stream

Streaming live video using Python sockets on the local network. It allows the sender and receiver to get connected over a common network for video streaming. 
in this case for simplicity only one-way video sharing is developed, that is if person A is the sender so in that case, person B will be the receiver.
By enhancing it, we can create a full video call system with bi-way audio and video streaming. With some customizations, it can also be used to send photos instead of video streams.

# Working

## Sender [or Server]
1. Creation of Socket Object uisng socket.socket(socket.AF_INET, socket.SOCK_STREAM), here AF_INET refers to the address-family ipv4 and SOCK_STREAM means connection-oriented TCP protocol. 
2. Extraction of Host IP using getsockname() method.
3. Then binding method bind(), is called, which binds it to a specified IP and port so that it can listen to incoming requests on that IP and port.
4. Once the binding is done, the server starts listening using listen() method has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections. In this case, it can have 5 connections at most.
5. Then, the establishment of the connection between the client and server takes place, using accept() method
6. Now, if some client XYZ is available, then the video stream will start on the Server using OpenCV
7. After that each frame (also known as an image) will be converted to a pickle object
8. Then that pickle object is further converted to some binary type of string representations, it is achieved using the pack() method of the Struct module which can convert Python values to C structs and vice-versa.
9. Finally the buffer (the packet) is sent using the sendall() method
10. From step 5, the process is repeated again and again till the time client or server exits or some exception happens.

## Reciever [or Client]
1. Creation of Socket Object
2. Sender's IP address (Server) is taken as input
3. Then connections are established which connect a TCP-based client socket to a TCP-based server socket. 
4. After that, the standard payload size is calculated and set. In this case, it's 8 bytes only (fixed).
5. 

## Tools and Technologies Used:

### Python Modules used:


### Softwares Used 
- Spyder 5.0.3
- CMD
- Git Bash
- Heroku

### OS Used:
- Windows 10 

## Features  
- sentiment analysis
- word cloud
- summary
- word count
- char count
- line count
- finding a specific word

## Setting up on local machine: 
1. Clone this repo on your system.
2. Open CMD
3. Install all the dependencies using requirements.txt:
	<pre> pip install requirements.txt </pre>
3. Run the following command:
	<pre> streamlit run text_analyzer.py </pre>



# Thank you
- Thank you all for using my app.
- All suggestions are warmly welcomed.


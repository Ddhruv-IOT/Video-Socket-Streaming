# Live Video Streaming

Streaming live video using Python sockets on local network. It allows sender and reciever to get connected over common network for video streaming. 
in this case for simplicity only one way video sharing is developed, that is if person A is sender so in that case person B will be the reciever.
By enhanching it, we cah create a full video call system wih bi-way audio and video streaming. With some customizations it can also be used to send photos instead of video streams.

# Working

## Sender [or Server]
1. 
2. 

## Reciever [or Client]
1. Creation of Socket Object
2. Reciever's IP address (Server) is taken as input
3. Then connections is established which connects a TCP based client socket to a TCP based server socket. 
4. Then standard payload size is calculated and set, in this case its 8 bytes only.
5. 

## Tools and Technologies Used:

### Python Modules used:
- Streamlit: for front-end development.
- Speech_recognition: to convert audio to text for processing.
- NLTK: for text-based processing like removing stopwords, analyzing sentiments, etc.
- Wordcloud: To make the word cloud for the given input.
- Matplotlib for displaying the word cloud on the front-end.

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
3. Install all the dependncies using requirements.txt:
	<pre> pip install requirements.txt </pre>
3. Run the following command:
	<pre> streamlit run text_analyzer.py </pre>



# Thank you
- Thank you all for using my app.
- All suggestions are warmly welcomed.


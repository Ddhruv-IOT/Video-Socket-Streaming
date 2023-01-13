# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:42:51 2022

@author: ACER
"""
# Sender

import socket
import cv2
import pickle
import struct

def get_ip_address():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  return s.getsockname()[0]

# Socket creation
ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = get_ip_address()
print(f"Host IP: {host_ip}")

port = 9999
socket_address = (host_ip, port)

ser_sock.bind(socket_address)
ser_sock.listen(5)

print(f"Listening at {ser_sock}")

while 1:
    client, addr = ser_sock.accept()

    print(f"Connected to {addr}")
    if client:
        vid = cv2.VideoCapture(1)
        while(vid.isOpened()):
            img, frm = vid.read()
            a = pickle.dumps(frm)
            message = struct.pack("Q", len(a)) + a
            client.sendall(message)
            cv2.imshow('Sent Video', frm)
            key = cv2.waitKey(1) & 0xff
            if key == ord('q'):
                client.close()

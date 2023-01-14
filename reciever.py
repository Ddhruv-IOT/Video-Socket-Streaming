# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:10:26 2022

@author: ACER
"""

# Reciever

import socket
import cv2
import pickle
import struct

def get_ip_address():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  return s.getsockname()[0]


# Socket creation
cln_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = input(
    f"Kindly input server Ip address \nEx:{get_ip_address()} \nif same as server hit 'y' and enter \nYour Input: ")


if host_ip == "y":
    host_ip = get_ip_address()


print(f"Reciever IP {host_ip}")

port = 9999
socket_address = (host_ip, port)

cln_sock.connect(socket_address)

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = cln_sock.recv(4*1024)
        if not packet:
            break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += cln_sock.recv(4*1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("Recieved Video", frame)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break
cln_sock.close()

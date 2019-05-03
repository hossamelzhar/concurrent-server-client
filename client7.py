#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:48:08 2019

@author: elzhar
"""

import socket as sk
import threading as th



s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.setsockopt(sk.SOL_SOCKET,sk.SO_REUSEADDR, 1)
host='127.0.0.1'
port=7000
s.connect((host,port))

def rec_fun(s):
    while True:
        data=s.recv(2048)
        print('Server: ',data.decode('utf-8'))


while True:
    rec_thread=th.Thread(target=rec_fun,args=(s,))
    rec_thread.start()
    s.send(input('ME: ').encode('utf-8'))

s.close()
        

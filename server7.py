#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:57:50 2019

@author: elzhar
"""

import socket as sk
import threading as th


s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.setsockopt(sk.SOL_SOCKET,sk.SO_REUSEADDR, 1)
host='127.0.0.1'
port=7000
s.bind((host,port))
s.listen(7)

def send_fun(c,ad):
        rec_thread=th.Thread(target=recv_fun,args=(c,ad))
        rec_thread.start()
        while True:
            c.send(input('ME: ').encode('utf-8'))

def recv_fun(c,ad):
    while True:
        x=c.recv(2048)
        print('<',ad,'>',x.decode('utf-8'))



while True:
    c,ad=s.accept()
    print('new connection from',ad[0])
    client_thread=th.Thread(target=send_fun,args=(c,ad[0]))
    client_thread.start()

s.close()


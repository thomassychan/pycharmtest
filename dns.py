#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:28:53 2018
@author: chanthomas
"""

import socket

with open("hosts.txt") as ins:
    ins = ins.read().splitlines()
    for line in ins:
        hostname = line.rstrip()
        addr = socket.gethostbyname(hostname)
        print (line, addr)
        if 'str' in line:
                break

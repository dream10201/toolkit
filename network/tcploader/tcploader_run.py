#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import socket
import logging

def Run(p,t,conf):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((conf['host'],conf['port']))

    logging.info('connected to %s:%d, peer=%s,sock=%s',conf['host'],conf['port'],sock.getpeername(),sock.getsockname())
    sock.close()


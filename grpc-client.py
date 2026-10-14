#!/usr/bin/env python3

import lab6_pb2
from lab6_pb2_grpc import Lab6
from __future__ import print_function

import requests
import json
import time
import base64
import jsonpickle
import random
import argparse
import grpc

import lab6_pb2
import lab6_pb2_grpc

def doRawImage(addr, debug=False):
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

    reply = addr.rawImage(lab6_pb2.rawImageMsg(img))

    if debug:
        print("Response is", reply)

def doAdd(addr, debug=False):
    reply = addr.add(lab6_pb2.addMsg(a = 5, b = 10))

    if debug:
        print("Response is", reply)

def doDotProduct(addr, debug=False): #
    a = [random.random() for _ in range(100)]
    b = [random.random() for _ in range(100)]

    reply = addr.dotProduct(lab6_pb2.dotProductMsg(a, b))

    if debug:
        print("Response is", reply)

def doJsonImage(addr, debug=False): #
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    img_encoded = base64.b64encode(img).decode('utf-8')

    reply = addr.jsonImage(lab6_pb2.jsonImageMsg(img_encoded))

    if debug:
        print("Response is", reply)


# ---------------------------------------------------------
# Parse command-line arguments
# ---------------------------------------------------------

parser = argparse.ArgumentParser(
    description='REST client for measuring server operations'
)

parser.add_argument(
    'host',
    help='IP address or hostname of the REST server'
)

parser.add_argument(
    'cmd',
    choices=['add', 'rawImage', 'dotProduct', 'jsonImage'],
    help='Operation to perform'
)

parser.add_argument(
    'reps',
    type=int,
    help='Number of repetitions for measurement'
)

parser.add_argument(
    '-p', '--port',
    type=int,
    default=50051,
    help='Server port (default: 50051)'
)

parser.add_argument(
    '-d', '--debug',
    action='store_true',
    help='Print the response from the server'
)

args = parser.parse_args()


# ---------------------------------------------------------
# Build server address
# ---------------------------------------------------------




# ---------------------------------------------------------
# Perform requested operation
# ---------------------------------------------------------


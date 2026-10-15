#!/usr/bin/env python3

from __future__ import print_function
# from google.protobuf.internal.builder import BuildTopDescriptorsAndMessages
import lab6_pb2_grpc
import lab6_pb2
# from lab6_pb2_grpc import Lab6

# import requests
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

    reply = addr.rawImage(lab6_pb2.rawImageMsg(img = img))

    if debug:
        print("Response is", reply)

def doAdd(addr, debug=False):
    reply = addr.add(lab6_pb2.addMsg(a = 5, b = 10))

    if debug:
        print("Response is", reply)

def doDotProduct(addr, debug=False): #
    a = [random.random() for _ in range(100)]
    b = [random.random() for _ in range(100)]

    reply = addr.dotProduct(lab6_pb2.dotProductMsg(a = a, b = b))

    if debug:
        print("Response is", reply)

def doJsonImage(addr, debug=False): #
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    img_encoded = base64.b64encode(img).decode('utf-8')

    reply = addr.jsonImage(lab6_pb2.jsonImageMsg(img = img_encoded))

    if debug:
        print("Response is", reply)


# ---------------------------------------------------------
# Parse command-line arguments
# ---------------------------------------------------------

parser = argparse.ArgumentParser(
    description='gRPC client for measuring server operations'
)

parser.add_argument(
    'host',
    help='IP address or hostname of the gRPC server'
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

addr = f"{args.host}:{args.port}"

print(f"Running {args.reps} reps against {addr}")

channel = grpc.insecure_channel(addr) # opens a channel to the server without TLS
stub = lab6_pb2_grpc.Lab6Stub(channel)
operations = {
    'add': doAdd,
    'rawImage': doRawImage,
    'dotProduct': doDotProduct,
    'jsonImage': doJsonImage,
}
operation = operations[args.cmd]

# ---------------------------------------------------------
# Perform requested operation
# ---------------------------------------------------------

start = time.perf_counter()

for x in range(args.reps):
    operation(stub, debug=args.debug)

delta = ((time.perf_counter() - start) / args.reps) * 1000
print("Took", delta, "ms per operation")
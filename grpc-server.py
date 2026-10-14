#!/usr/bin/env python3

import lab6_pb2_grpc
import base64
import jsonpickle
from PIL import Image
import io
from concurrent import futures
import argparse
import grpc

import lab6_pb2
import lab6_pb2_grpc

class Lab6Service(lab6_pb2_grpc.Lab6Servicer):
    def add(self, request, context):
        return lab6_pb2.addReply(request.a + request.b)

    def rawImage(self, request, context):
        try:
            ioBuffer = io.BytesIO(request.image)
            img = Image.open(ioBuffer)
            reply = lab6_pb2.imageReply(width=img.size[0], height=img.size[1])
        except Exception:
            reply = lab6_pb2.imageReply(width=0, height=0)
        return reply

    def dotProduct(self, request, context):
        reply = sum(x * y for x, y in zip(request.a, request.b))
        return lab6_pb2.dotProductReply(reply)

    def jsonImage(self, request, context):
        try:
            img_bytes = base64.b64decode(request.image)
            ioBuffer = io.BytesIO(img_bytes)
            img = Image.open(ioBuffer)
            reply = lab6_pb2.imageReply(width=img.size[0], height=img.size[1])
        except Exception:
            reply = lab6_pb2.imageReply(width=0, height=0)
        return reply




if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Flask REST server'
    )

    parser.add_argument(
        '-p', '--port',
        type=int,
        default=50051,
        help='Port on which to run the server (default: 50051)'
    )

    args = parser.parse_args()
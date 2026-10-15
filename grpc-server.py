#!/usr/bin/env python3

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
        return lab6_pb2.addReply(sum = (request.a + request.b)) # sends the results reply back to the client

    def rawImage(self, request, context):
        try:
            ioBuffer = io.BytesIO(request.img)
            img = Image.open(ioBuffer)
            reply = lab6_pb2.imageReply(width = img.size[0], height = img.size[1])
        except Exception:
            reply = lab6_pb2.imageReply(width = 0, height = 0)
        return reply 

    def dotProduct(self, request, context):
        reply = sum(x * y for x, y in zip(request.a, request.b))
        return lab6_pb2.dotProductReply(dotproduct = reply)

    def jsonImage(self, request, context):
        try:
            img_bytes = base64.b64decode(request.img)
            ioBuffer = io.BytesIO(img_bytes)
            img = Image.open(ioBuffer)
            reply = lab6_pb2.imageReply(width = img.size[0], height = img.size[1])
        except Exception:
            reply = lab6_pb2.imageReply(width = 0, height = 0)
        return reply


def service(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10)) # create the server
    lab6_pb2_grpc.add_Lab6Servicer_to_server(Lab6Service(), server)
    server.add_insecure_port(f'[::]:{port}') # listen to all network interfaces on that port without TLS
    server.start() # start accepting requests
    print(f"Started server, gRPC server listening on port {port}")
    server.wait_for_termination() # keeps running until I kill the program


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='gRPC server'
    )

    parser.add_argument(
        '-p', '--port',
        type=int,
        default=50051,
        help='Port on which to run the server (default: 50051)'
    )

    args = parser.parse_args()
    service(args.port) # starts the server on the specified port
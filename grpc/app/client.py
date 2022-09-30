import logging

import grpc

import app.proto.messages_pb2 as messages
import app.proto.services_pb2_grpc as services


def run():
    """ Starts client and tries to receive data from http://localhost:50051 \
        via gRPC
    """
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = services.AssetServiceStub(channel)
        response: messages.Assets = stub.GetAll(
            messages.Directory(directory='')
        )
    print("Assets client received: " + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()

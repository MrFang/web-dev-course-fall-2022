import logging
import os
import sys
from concurrent import futures

import grpc

import app.proto.services_pb2_grpc as services
from app.AssetServicer import AssetServicer


def serve():
    """ Starts gRPC server on http://localhost:50051
    """
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_AssetServiceServicer_to_server(
        AssetServicer(f'{os.getcwd()}/{sys.argv[1]}'),
        server
    )
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

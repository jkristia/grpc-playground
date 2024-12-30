# from copilot

import asyncio
from concurrent import futures

import grpc
from test_pb2 import FooRequest, FooResponse
from test_pb2_grpc import FooGrpcServicer, add_FooGrpcServicer_to_server

class FooServer(FooGrpcServicer):
    async def getFoo(self, request: FooRequest, context):
        return FooResponse(message=request.message, index=request.index)

async def serve():
    server = grpc.aio.server()
    add_FooGrpcServicer_to_server(FooServer(), server)
    port = 50051
    server.add_insecure_port(f'[::]:{port}')
    await server.start()
    print(f'gRPC listening on port {port}')
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())

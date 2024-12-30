import asyncio
import signal

import grpc
from foo_pb2 import FooRequest, FooResponse
from foo_pb2_grpc import FooGrpcServicer, add_FooGrpcServicer_to_server

class FooServer(FooGrpcServicer):
    async def getFoo(self, request: FooRequest, context):
        print(f'request, {request.message}')
        return FooResponse(message=request.message, index=request.index + 2)

async def serve():
    server = grpc.aio.server()
    add_FooGrpcServicer_to_server(FooServer(), server)
    port = 50051
    server.add_insecure_port(f'[::]:{port}')
    await server.start()
    print(f'gRPC listening on port {port}')
    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        await server.stop(0)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server_task = loop.create_task(serve())

    def shutdown():
        server_task.cancel()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, shutdown)
    try:
        loop.run_until_complete(server_task)
    except asyncio.CancelledError:
        print("Server stopped gracefully.")    
    finally:
        loop.close()

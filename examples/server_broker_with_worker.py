from simrpc.server import SimRpcServer
import asyncio
from obj import a, add


# class a:
#     def __init__(self, name=None):
#         self.name = name

#     async def minus(self, x, y):
#         print("x-y=", x - y)
#         return x - y

#     async def update(self):
#         while True:
#             print(self.name)
#             await asyncio.sleep(5)

#     def period_task(self):
#         return [self.update()]


# def add(x, y):
#     print("x+y=", x + y)
#     return x + y


server = SimRpcServer()


settings = {
    "a": {
        "kwargs": {
            "name": "test"
        }
    }
}

# server.register_with_init(cls_list=[a], settings=settings)
server.register(a)
server.register(add)
server.start_broker()
# if you want to start worker in this ,you should use server.run()
server.run()
# else you can only start broker

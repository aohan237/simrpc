from server import SimRpcServer

server = SimRpcServer(async_task=True)


class a:
    async def minus(self, x, y):
        print("x-y=", x - y)
        return x - y


def add(x, y):
    # print("x+y=", x + y)
    return x + y


bb = a()

server.register(bb)
server.register(add)
server.run()

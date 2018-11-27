import sys
sys.path.append('/Users/linziyan/github/SimRpc')
print(sys.path)
import zmq
from simrpc.client import SimRpcClient
import time

cc = SimRpcClient()

print("cc", cc)


class a:
    name = '123'

    @cc.task(response_only=True)
    def minus(self, x, y):
        print("x+y=", x - y)
        return x - y


@cc.task(response_only=True, func=True)
def add(x, y):
    return x + y

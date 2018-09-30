import zmq
from client import SimRpcClient
import time
cc = SimRpcClient()

print("cc", cc)


class a:
    @cc.task(response_only=True)
    def minus(self, x, y):
        print("x+y=", x - y)
        return x - y


@cc.task(response_only=True, func=True)
def add(x, y):
    return x + y


bb = a()


def aa():
    ss = int(time.time() * 1000)
    for i in range(20000):

        start = int(time.time() * 1000)

        # dd = add(1, 2)
        ee = bb.minus(80, 7)
        # print(ee, dd)
        end = int(time.time() * 1000)
        # print("time used", end - start)
    print("all time used", int(time.time() * 1000) - ss)
    return 0


aa()

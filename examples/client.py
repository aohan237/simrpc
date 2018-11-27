import zmq
import time
from obj import a, add

bb = a()


def aa():
    ss = int(time.time() * 1000)
    for i in range(5):
        print('start')
        start = int(time.time() * 1000)

        dd = add(1, 2, rpc_client=True)
        ee = bb.minus(80, 7, rpc_client=True)
        print(ee, dd)
        end = int(time.time() * 1000)
        # print("time used", end - start)
    print("all time used", int(time.time() * 1000) - ss)
    return 0


aa()

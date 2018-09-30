import msgpack
import uuid
import logging

logger = logging.getLogger(__package__)


def decode_msg(service=None, entry=None, args=None, kwargs=None):
    data = {
        "service": service,
        "entry": entry,
        "args": args,
        "kwargs": kwargs,
        "id": str(uuid.uuid1()),
        "response": None
    }
    logger.debug(data)
    data_sent = msgpack.dumps(data)
    return data_sent


def encode_msg(data, response_only: bool = False):
    res = msgpack.loads(data, encoding='utf-8')
    if response_only:
        return res.get("response", {})
    else:
        return res


def decode_msg_body(data):
    return msgpack.dumps(data)

import random
import string
import logging

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
_logger = logging.getLogger()
_logger.addHandler(handler)
_logger.setLevel(logging.DEBUG)


def _rand(length=8):
    alpha_numeric = string.ascii_letters + string.digits
    return ''.join((random.choice(alpha_numeric) for i in range(length)))

import base64


def decode(password):
    return base64.b64decode(password)

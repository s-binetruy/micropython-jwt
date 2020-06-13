
import ubinascii
import ujson
from ujwt.hmac import HMAC256


class Jwt:
    def __init__(self, secret):
        self._secret = bytes(secret, 'utf-8')


    def encode(self, payload):
        header64 = self._encodeBase64(self._jsonHeader)
        payload64 = self._encodeBase64(ujson.dumps(payload))

        segments = []
        segments.append(header64)
        segments.append(payload64)
        signing = b".".join(segments)

        signature = self._sign(signing)
        signature64 = self._encodeBase64(signature)
        segments.append(signature64)

        token = b".".join(segments)
        return token


    def decode(self, token):
        raise NotImplementedError()


    def _encodeBase64(self, data):
        s = data
        if isinstance(s, str):
            s = bytes(data, 'utf-8')

        b64 = ubinascii.b2a_base64(s)[:-1]
        return b64.replace(b"=", b"").replace(b"+", b"-").replace(b"/", b"_")


    def _sign(self, data):
        return HMAC256(self._secret, data).digest()

    @property
    def _jsonHeader(self):
        return ujson.dumps({'alg': 'HS256', 'typ': 'JWT'})

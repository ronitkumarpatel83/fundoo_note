import jwt


class JWTService:
    def encode_token(self):
        encode = jwt.encode({"some": "payload"}, 'secret', algorithm="HS256")
        print(encode)
        return encode

    def decode_token(self):
        jwt.decode(self.encode_token(), 'secret', algorithms="HS256")

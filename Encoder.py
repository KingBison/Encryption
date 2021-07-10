class Encoder:

    def __init__(self, key):
        self.str = str
        self.key = key
        self.out = ""

    def encrypt(self, message):
        out = ""
        for i in range(len(message)):
            for o in self.key:
                if o[0] == message[i]:
                    out+=o[1]

        return out

        
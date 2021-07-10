class Decoder:

    def __init__(self, key):
        self.str = str
        self.key = key
        self.out = ""

    def decrypt(self, message):
        out = ""
        for i in range(len(message)):
            for o in self.key:
                if o[1] == message[i]:
                    out+=o[0]

        return out

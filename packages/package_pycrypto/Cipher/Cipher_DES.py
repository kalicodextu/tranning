from Crypto.Cipher import DES3
from Crypto import Random
from binascii import b2a_hex, a2b_hex


class MyCrypt():
    def __init__(self, key):
        self.key = key
        self.mode = DES3.MODE_OFB
        self.iv = Random.new().read(DES3.block_size)

    def myencrypt(self, text):
        length = 16
        count = len(text)
        add = (length - (count % length))
        text = text + ('\0' * add)
        cryptor = DES3.new(self.key, self.mode, self.iv)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def mydecrypt(self, text):
        cryptor = DES3.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    mycrypt = MyCrypt('0123456789123456')
    e = mycrypt.myencrypt('hello')
    d = mycrypt.mydecrypt(e)
    print e
    print d

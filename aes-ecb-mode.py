"""
Set 1, Challenge 7
https://cryptopals.com/sets/1/challenges/7
The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key
"YELLOW SUBMARINE".
(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).
Decrypt it. You know the key, after all.
Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
"""

from base64 import b64decode
from Crypto.Cipher import AES

KEY = b'YELLOW SUBMARINE'

# https://pycryptodome.readthedocs.io/en/latest/src/examples.html#encrypt-data-with-aes
def aes_ecb_decryption(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.decrypt(cipher_text)
    return data

def main():
    with open('aes-ecb-mode-ciphertext.txt', 'rb') as input_file:
        cipher_text = b64decode(input_file.read())
    print(f'KEY: {KEY.decode()}\nPLAINT_TEXT: \n{aes_ecb_decryption(cipher_text, KEY).decode()}')

if __name__ == "__main__":
    main()
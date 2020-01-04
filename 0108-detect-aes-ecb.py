"""
Set 1, Challenge 8
https://cryptopals.com/sets/1/challenges/8
In this file are a bunch of hex-encoded ciphertexts.
One of them has been encrypted with ECB. Detect it.
Remember that the problem with ECB is that it is stateless and deterministic
"""

BLOCK_SIZE = 16
# in ECB the same 16 byte plaintext block will always produce the same 16 byte ciphertext
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ecb-mode

def duplicate_blocks(cipher_text):
    for i in range(0, len(cipher_text), BLOCK_SIZE):    # range(start, stop, step)
        block = cipher_text[i: i + BLOCK_SIZE]          # creates chunks the size of BLOCK_SIZE
        duplicate_block = len(block) - len(set(block))  # gets total of block minus duplicates
        result = {'cipher_text': cipher_text, 'duplicates': int(duplicate_block)}
        return result

def main():
    cipher_text = [bytes.fromhex(cipher.strip()) for cipher in open('0108-detect-aes-ecb-ciphertext.txt', 'r')]
    # Cipher text is in hex I need to convert it to bytes

    duplicates = [duplicate_blocks(cipher) for cipher in cipher_text]
    sorted_duplicates = sorted(duplicates, key=lambda x: x['duplicates'], reverse=True)[0]
    print(f"DUPLICATES: {sorted_duplicates['duplicates']}\nCIPHER_TEXT: {sorted_duplicates['cipher_text']}")
    # TODO: Find out why I couldn't get 0104-single-byte-xor.py method of sorting working with this challenge

if __name__ == "__main__":
    main()
"""
A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost
never want to transform a single block; we encrypt irregularly-sized messages. One way we account for irregularly
sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular
padding scheme is called PKCS#7. So: pad any block to a specific block length, by appending the number of bytes
of padding to the end of the block.

"YELLOW SUBMARINE"
... padded to 20 bytes would be:
"YELLOW SUBMARINE\x04\x04\x04\x04"
"""

PLAIN_TEXT = b"YELLOW SUBMARINE YELLOW SUBMARINE"

BLOCK_SIZE = 20

def pkcs7_padding(plain_text):

    for i in range(0, len(plain_text), BLOCK_SIZE):
        block = plain_text[i: i + BLOCK_SIZE]   # Splits the plaintext in to blocks (from 01.08)

        if BLOCK_SIZE == len(block):    # If block size = BLOCK_SIZE, continue
            print(block)
            continue

        padding_size = (BLOCK_SIZE - len(block)) % BLOCK_SIZE   # Calculates number of padding characters required

        if padding_size == 0:
            padding_size = BLOCK_SIZE

        padding = (chr(padding_size) * padding_size).encode()
        if block is None:
            return padding
        print(block + padding)

def main():
    pkcs7_padding(PLAIN_TEXT)

if __name__ == "__main__":
    main()
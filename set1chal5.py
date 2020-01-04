input_byte = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

def repeating_key_xor():
    """Set 1, Challenge 5
       Encrypt the stanza, under the key "ICE", using repeating-key XOR"""
    cipher = b''
    i = 0
    for byte in input_byte:
        cipher += bytes([byte ^ key[i]])
        if i < len(key) - 1:
            i = i + 1
        else:
            i = 0
    return cipher.hex()

print(repeating_key_xor())
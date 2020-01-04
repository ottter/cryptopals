from base64 import b64decode

"""Set 1, Challenge 6
   Break repeating-key XOR. The corresponding file has been base64'd after being encrypted with repeating-key XOR.
   The goal is to decrypt it.
   
   This is an example of a Vigenere cipher breaker: https://en.wikipedia.org/wiki/Vigenere_cipher"""

# Suggested values to use
KEY_SIZE = range(2, 41)

# Source: Wikipedia. Dict found on SO. I added the space (Wiki said its more common than 'E'
LETTER_FREQ = {'E': 12.7, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
               'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
               'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07, ' ': 14.0}

def hamming_distance(ham1, ham2):
    """The Hamming distance is the total number of differing bits between two equal length strings"""
    assert len(ham1) == len(ham2), 'Mismatched input lengths'

    # (i, 'b') cuts off the leading 0s, giving a wrong answer. (i, '#010b') preserves those 0s
    ham1 = ''.join(format(i, '#010b') for i in ham1)
    ham2 = ''.join(format(i, '#010b') for i in ham2)
    dist = sum(x != y for x, y in zip(ham1, ham2))

    return dist

def repeating_key_xor(input_byte, key):
    """(Set 1, Challenge 5) Encrypt the stanza, under the key "ICE", using repeating-key XOR"""
    cipher = b''
    i = 0

    for byte in input_byte:
        cipher += bytes([byte ^ key[i]])
        if i < len(key) - 1:
            i = i + 1
        else:
            i = 0

    return cipher

def english_score(letter_input):
    """(Set 1, Challenge 3)"""
    score = 0

    for byte in letter_input.upper():
        score += LETTER_FREQ.get(chr(byte).upper(), 0)
    return score

    # Alternate method using list comprehension I found
    # return sum([LETTER_FREQ.get(chr(byte), 0) for byte in letter_input.upper()])

def single_char_xor(input_bytes, char_freq):
    output_bytes = b''

    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_freq])

    return output_bytes

def single_byte_xor(cipher):
    """(Set 1, Challenge 3) Hex encoded string has been XOR'd against a single character. Modified slightly"""
    potential_messages = []

    for key_value in range(256):
        message = single_char_xor(cipher, key_value)
        score = english_score(message)

        data = {'key': key_value, 'score': int(score), 'result': message}

        potential_messages.append(data)

    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]

def break_repeating_key_xor(cipher):
    """Break the Vigenere cipher, or repeating key XOR"""
    average_distances = []

    for key_size in KEY_SIZE:
        distances = []  # Hamming Distance

        blocks = [cipher[i:i + key_size] for i in range(0, len(cipher), key_size)]

        # for loop is .1 seconds faster than while true here
        for block in blocks:
            block_1 = blocks[0]
            block_2 = blocks[1]

            distance = hamming_distance(block_1, block_2)
            distances.append(distance / key_size)

            del blocks[0:1]

        result = {'key': key_size, 'average distance': sum(distances) / len(distances)}
        average_distances.append(result)

    possible_key_lengths = sorted(average_distances, key=lambda x: x['average distance'])[0]

    key = b''
    possible_plaintext = []
    possible_key_length = possible_key_lengths['key']

    for k in range(possible_key_length):
        block = b''

        for c in range(k, len(cipher), possible_key_length):
            block += bytes([cipher[c]])

        key += bytes([single_byte_xor(block)['key']])

    possible_plaintext.append((repeating_key_xor(cipher, key), key))

    return max(possible_plaintext, key=lambda x: english_score(x[0]))

def main():
    ## Input: Two strings of equal length with any content

    # hamming_test = hamming_distance(b'this is a test', b'wokka wokka!!!')
    # print(f"Your test input's Hamming Distance is: {hamming_test}")

    with open("repeating-key-zor-ciphertext.txt", "r") as input_file:
        cipher_text = b64decode(input_file.read())
        result, key = break_repeating_key_xor(cipher_text)

        print(f"key: {key}\nplaintext: {result}")

if __name__ == "__main__":
    main()

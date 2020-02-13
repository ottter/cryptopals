import codecs
import os

# Challenges from https://cryptopals.com/sets/1

def hex_to_base64(hex_input):
    """Set 1, Challenge 1
       Convert hex to base64"""
    x = codecs.encode(codecs.decode(hex_input, 'hex'), 'base64').decode()
    print(x.replace('\n', ''))

def fixed_xor(input_value):
    """Set 1, Challenge 2
       A function that takes two equal-length buffers and produces their XOR combination"""
    hex_input = int(input_value, base=16)
    xor_against = int('686974207468652062756c6c277320657965', base=16)
    result = f'{int(hex(hex_input ^ xor_against), 16):x}'

    assert result == '746865206b696420646f6e277420706c6179', 'Incorrect conversion'

    print(result)

def single_byte_xor(input_value):
    """Set 1, Challenge 3
       The given hex encoded string has been XOR'd against a single character. Find the key, decrypt the message"""
    # Source: Wikipedia. Dict found on SO. I added the space (Wiki said its more common than 'E'
    letter_freq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
                   'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                   'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07, ' ': 14}

    results = []
    # number of ASCII characters
    for key in range(256):
        output = b''

        # XOR every byte of the input
        for char in bytes.fromhex(input_value):
            output += bytes([char ^ key])

        # Gives combination a score depending on appearances in letter_freq
        score = 0
        for byte in output:
            score += letter_freq.get(chr(byte).upper(), 0)
        # ... and adds to (score, result) dict
        result = {'score': int(score), 'result': output}
        results.append(result)

    results = (sorted(results, key=lambda x: x['score'], reverse=True))
    # Outputs the top 5 results. Before adding space as a value, the correct answer was 5th
    for result in list(results)[0:1]:
        # print(f'Score:{result["score"]}\t Output: {result["result"]}')
        return result

def single_byte_xor_2():
    """Set 1, Challenge 4
       One of the 60-character strings in 0104-single-byte-xor-ciphertext.txt has been encrypted by single-character XOR."""
    # Trying to not use functions was an awful idea. being stubborn about it was worse
    results = []
    input_str = [line.strip() for line in open('0104-single-byte-xor-ciphertext.txt', 'r')]

    for result in input_str:
        output = single_byte_xor(result)
        results.append(output)

    results = (sorted(results, key=lambda c: c['score'], reverse=True))

    for result in list(results)[0:1]:
        print(f'Score:{result["score"]}\t Output: {result["result"].decode()}')

### To try yourself: uncomment the function call below and run

### Set 1, Challenge 1 https://cryptopals.com/sets/1/challenges/1
# hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

### Set 1, Challenge 2 https://cryptopals.com/sets/1/challenges/2
# fixed_xor('1c0111001f010100061a024b53535009181c')

### Set 1, Challenge 3
# print(single_byte_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
# This one is kind of ugly because I wanted to do it all in one function and then had to repurpose it for 01.04

### Set 1, Challenge 4
single_byte_xor_2()
from itertools import combinations
from base64 import b64decode

"""Set 1, Challenge 6
   Break repeating-key XOR. The corresponding file has been base64'd after being encrypted with repeating-key XOR.
   The goal is to decrypt it."""

# Suggested values to use
KEY_SIZE = range(2, 41)

# Source: Wikipedia. Dict found on SO. I added the space (Wiki said its more common than 'E'
LETTER_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
               'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
               'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07, ' ': 14}

def hamming_distance(ham1, ham2):
    """The Hamming distance is the total number of differing bits between two equal length strings"""
    assert len(ham1) == len(ham2), 'Mismatched input lengths'
    # (i, 'b') cuts off the leading 0s, giving a wrong answer. (i, '#010b') preserves those 0s
    ham1 = ''.join(format(i, '#010b') for i in ham1)
    ham2 = ''.join(format(i, '#010b') for i in ham2)
    dist = sum(x != y for x, y in zip(ham1, ham2))
    return dist

def main():
    # Input: Two strings of equal length with any content
    # hamming_test = hamming_distance(b'this is a test', b'wokka wokka!!!')
    # print(f"Your test input's Hamming Distance is: {hamming_test}")

    with open("set1chal6.txt", "r") as input_file:
        input_data = b64decode(input_file.read())

main()
import codecs

# Challenges from https://cryptopals.com/sets/1

def hex_to_base64(hex_input):
    """Set 1, Challenge 1"""
    x = codecs.encode(codecs.decode(hex_input, 'hex'), 'base64').decode()
    print(x.replace('\n', ''))

def fixed_xor():
    """Set 1, Challenge 2"""
    hex_input = int('1c0111001f010100061a024b53535009181c', 16)
    xor_against = int('686974207468652062756c6c277320657965', 16)
    print(f'{int(hex(hex_input ^ xor_against), 16):x}')




### Set 1, Challenge 1 https://cryptopals.com/sets/1/challenges/1
# hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

### Set 1, Challenge 2 https://cryptopals.com/sets/1/challenges/2
fixed_xor()

### Set 1, Challenge 3


### Set 1, Challenge 4


### Set 1, Challenge 5
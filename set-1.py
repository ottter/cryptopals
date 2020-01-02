import codecs

# Challenges from https://cryptopals.com/sets/1

def hex_to_base64(hex_input):
    x = codecs.encode(codecs.decode(hex_input, 'hex'), 'base64').decode()
    return print(x.replace('\n', ''))

hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
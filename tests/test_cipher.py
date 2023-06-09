# When you run this file, these next lines will show you the expected
# # and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)
from lib.cipher_debug import *

def test_cipher_encode():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == 'EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL'
    pass

def test_cipher_decode():
    result = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert result == 'theswiftfoxjumpedoverthelazydog'
    pass

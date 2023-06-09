def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    print(f"{ciphertext_chars} should be empty")
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
        print(f"{ciphertext_chars} should return list")
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    
    plaintext_chars = []
    print(f"{plaintext_chars} should be empty")
    key_first_char = "s"
    text_first_char = "t"
    encode_first_char = "E"
    print(f"{ord(key_first_char)}, {ord(text_first_char)}, {ord(encode_first_char)}")
    print(f" {ord(encode_first_char) - ord(key_first_char) + ord(text_first_char)}, should = val for decode")
    #how do we get from encode to text with step key
    for i in encrypted:

        plain_char = cipher[65 - ord(i)]
        print(f"{plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    #print(f"{alphabet} should be a to z.")
    cipher_with_duplicates = list(key) + alphabet
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
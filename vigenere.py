def char_to_num(c, base):
    """
    Convert a character to its position in the base.
    
    Args:
    c (str): Character to convert.
    base (str): Character base string.
    
    Returns:
    int: Position of the character in the base.
    """
    return base.index(c)

def num_to_char(n, base):
    """
    Convert a number to its corresponding character in the base.
    
    Args:
    n (int): Position to convert.
    base (str): Character base string.
    
    Returns:
    str: Character at the specified position in the base.
    """
    return base[n]

def vigenere_encrypt(plaintext, key, base):
    """
    Encrypt text using the Vigenère Cipher supporting all characters.
    
    Args:
    plaintext (str): Text to encrypt.
    key (str): Encryption key.
    base (str): Character base string.
    
    Returns:
    str: Encrypted text.
    """
    base_length = len(base)
    plaintext = [c for c in plaintext]
    key = [c for c in key]
    
    # Repeat key to match length of plaintext
    key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    ciphertext = []

    for p, k in zip(plaintext, key_repeated):
        if p in base:
            p_num = char_to_num(p, base)
            k_num = char_to_num(k, base)
            c_num = (p_num + k_num) % base_length
            ciphertext.append(num_to_char(c_num, base))
        else:
            # If character is not in the base, leave it unchanged
            ciphertext.append(p)

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key, base):
    """
    Decrypt text using the Vigenère Cipher supporting all characters.
    
    Args:
    ciphertext (str): Text to decrypt.
    key (str): Decryption key.
    base (str): Character base string.
    
    Returns:
    str: Decrypted text.
    """
    base_length = len(base)
    ciphertext = [c for c in ciphertext]
    key = [c for c in key]
    
    # Repeat key to match length of ciphertext
    key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext = []

    for c, k in zip(ciphertext, key_repeated):
        if c in base:
            c_num = char_to_num(c, base)
            k_num = char_to_num(k, base)
            p_num = (c_num - k_num + base_length) % base_length
            plaintext.append(num_to_char(p_num, base))
        else:
            # If character is not in the base, leave it unchanged
            plaintext.append(c)

    return ''.join(plaintext)

# Example usage
base = "<PLaiNI.F7=yCr49`#T?&{oXhVs$xSmJjqROMEk Z!+@c,-}]/UB|1D^nAp2W)lf3[8g5v%(Ywd~G_t>*KzQeu0Hb6"
plaintext = "The quick brown fox jumps over the lazy dog"
key = "w09R!"

encrypted = vigenere_encrypt(plaintext, key, base)
print("Encrypted:", encrypted)

decrypted = vigenere_decrypt(encrypted, key, base)
print("Decrypted:", decrypted)
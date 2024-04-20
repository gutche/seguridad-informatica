def xor_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        encrypted_char = chr(ord(char) ^ ord(key[key_index]))
        ciphertext += encrypted_char
        # Incrementar el índice de la clave circularmente
        key_index = (key_index + 1) % len(key)
    return ciphertext

def xor_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ ord(key[key_index]))
        plaintext += decrypted_char
        # Incrementar el índice de la clave circularmente
        key_index = (key_index + 1) % len(key)
    return plaintext

# Ejemplo de uso:
plaintext = "(:7*;31#=?&19"
key = "XOR"

# Cifrado
ciphertext = xor_encrypt(plaintext, key)
print("Texto cifrado:", ciphertext)

# Descifrado
decrypted_text = xor_decrypt(ciphertext, key)
print("Texto descifrado:", decrypted_text)

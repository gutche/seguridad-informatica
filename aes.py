from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import binascii

def aes_encrypt(plaintext, key, iv):
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return unpad(decrypted, AES.block_size).decode()

# Clave y IV
key = "SeguridadInforma"
iv = get_random_bytes(AES.block_size)
iv_hex = binascii.hexlify(iv).decode()

# Texto a cifrar
plaintext = "Hola, este es un mensaje secreto."

# Cifrado
ciphertext = aes_encrypt(plaintext, key, iv)
print("Texto cifrado:", ciphertext)

# Descifrado
decrypted_text = aes_decrypt(ciphertext, key, iv)
print("Texto descifrado:", decrypted_text)

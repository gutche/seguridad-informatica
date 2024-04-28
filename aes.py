from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def decipher(cipher_text):
    # La clave y el IV
    key = b'SeguridadInforma'  # Clave de 16 bytes
    iv = b'SeguridadInforma'   # IV de 16 bytes

    # Convertir el texto cifrado de hexadecimal a bytes
    cipher_text_bytes = bytes.fromhex(cipher_text)

    # Crear un objeto AES con el modo CBC y el IV dado
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Descifrar el texto cifrado
    plaintext = cipher.decrypt(cipher_text_bytes)

    # Eliminar el padding
    plaintext = plaintext.rstrip(b'\0')

    # Convertir el resultado descifrado de bytes a una cadena
    plaintext = plaintext.decode('utf-8')

    print("Texto descifrado:", plaintext)

    return plaintext

def cypher(plaintext):
    # La clave y el IV
    key = b'SeguridadInforma'  # Clave de 16 bytes
    iv = b'SeguridadInforma'   # IV de 16 bytes

    # Crear un objeto AES con el modo CBC y el IV dado
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Añadir el padding al texto plano
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)

    # Cifrar el texto plano
    cipher_text = cipher.encrypt(padded_plaintext)

    # Codificar el texto cifrado en hexadecimal
    cipher_text_hex = cipher_text.hex()

    print("Texto cifrado en hexadecimal:", cipher_text_hex)

texto_descifrado = decipher("f6994c079e2984d406e90a908076ed69")
cypher(texto_descifrado)

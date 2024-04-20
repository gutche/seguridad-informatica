def cifrar_cesar(texto, clave):
    texto_cifrado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isalpha():
            # Obtener el índice del carácter en el alfabeto
            if char.islower():
                idx = ord(char) - ord('a')
            else:
                idx = ord(char) - ord('A')
            # Aplicar el desplazamiento según la clave
            if clave[i % len(clave)].islower():
                shift = ord(clave[i % len(clave)]) - ord('a')
            else:
                shift = ord(clave[i % len(clave)]) - ord('A')
            # Calcular el nuevo índice
            new_idx = (idx + shift) % 26
            # Obtener el carácter cifrado y añadirlo al texto cifrado
            if char.islower():
                texto_cifrado += chr(new_idx + ord('a'))
            else:
                texto_cifrado += chr(new_idx + ord('A'))
        else:
            # Mantener los caracteres que no son letras
            texto_cifrado += char
    return texto_cifrado

def descifrar_cesar(texto_cifrado, clave):
    texto_descifrado = ""
    for i in range(len(texto_cifrado)):
        char = texto_cifrado[i]
        if char.isalpha():
            # Obtener el índice del carácter en el alfabeto
            if char.islower():
                idx = ord(char) - ord('a')
            else:
                idx = ord(char) - ord('A')
            # Aplicar el desplazamiento inverso según la clave
            if clave[i % len(clave)].islower():
                shift = ord(clave[i % len(clave)]) - ord('a')
            else:
                shift = ord(clave[i % len(clave)]) - ord('A')
            # Calcular el nuevo índice
            new_idx = (idx - shift) % 26
            # Obtener el carácter descifrado y añadirlo al texto descifrado
            if char.islower():
                texto_descifrado += chr(new_idx + ord('a'))
            else:
                texto_descifrado += chr(new_idx + ord('A'))
        else:
            # Mantener los caracteres que no son letras
            texto_descifrado += char
    return texto_descifrado
# Ejemplo de uso
texto_cifrado = "OmyemIehVBSkTmZzEa"
clave = "Vinagre"

# Descifrar el texto cifrado
texto_descifrado = descifrar_cesar(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)

# Cifrar un texto
texto_original = "TelegRamNOSeCiErRa"
texto_cifrado = cifrar_cesar(texto_original, clave)
print("Texto cifrado:", texto_cifrado)

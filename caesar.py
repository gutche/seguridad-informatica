def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        # Verificar si el caracter es una letra
        if caracter.isalpha():
            codigo = ord(caracter)
            # Manejar mayúsculas
            if caracter.isupper():
                resultado += chr((codigo + desplazamiento - 65) % 26 + 65)
            # Manejar minúsculas
            elif caracter.islower():
                resultado += chr((codigo + desplazamiento - 97) % 26 + 97)
        else:
            # Mantener caracteres que no son letras
            resultado += caracter
    return resultado

def descifrar_cesar(texto_cifrado):
    # Fuerza bruta para probar todos los desplazamientos posibles
    for desplazamiento in range(1, 26):
        resultado = ""
        for caracter in texto_cifrado:
            # Verificar si el caracter es una letra
            if caracter.isalpha():
                codigo = ord(caracter)
                # Manejar mayúsculas
                if caracter.isupper():
                    resultado += chr((codigo - desplazamiento - 65) % 26 + 65)
                # Manejar minúsculas
                elif caracter.islower():
                    resultado += chr((codigo - desplazamiento - 97) % 26 + 97)
            else:
                # Mantener caracteres que no son letras
                resultado += caracter
        print("Desplazamiento {}: {}".format(desplazamiento, resultado))


# Descifrar el texto cifrado
print("Descifrando YLYDHOFHVDU:")
descifrar_cesar("YLYDHOFHVDU")

print()
print("Cifrando VIVAELCESAR con 3 desplazamientos:",cifrar_cesar("VIVAELCESAR",3))
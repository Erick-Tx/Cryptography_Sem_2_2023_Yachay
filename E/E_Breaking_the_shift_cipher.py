def decrypt_shift_cipher(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"

# Solicitar al usuario que ingrese el valor de key
key = int(input("Ingresa el valor de key (0-25): "))

# Descifrar el mensaje usando la clave proporcionada
decrypted_text = decrypt_shift_cipher(ciphertext, key)

print(f"Decrypted Text with Key {key}: {decrypted_text}")

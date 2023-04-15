import math

from utils import Key


def encrypt(x, e, n):
    return pow(x, e, n)

def decrypt(y, d, n):
    return pow(y, d, n)


def main():
    k = Key()
    
    plaintext_message = int(input("Enter plain text here:"))
    ciphertext_message = encrypt(plaintext_message, k.e, k.n)
    print("Encrypted ciphertext: " + str(ciphertext_message))

    plaintext_message = decrypt(ciphertext_message, k.d, k.n)
    print("Decrypted plaintext: " + str(plaintext_message))

if __name__ == '__main__':
    main()

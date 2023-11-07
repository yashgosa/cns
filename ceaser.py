def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            #Upper Case => 65
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            #Lower Case => 97
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

if __name__ == "__main__":
    text = "AttackAt Once"
    s = 4
    print("Text :", text)
    print("Shift:", s)
    print("Cipher:" , encrypt(text, s))
    print(f"{encrypt(text, s)} decrypted is {encrypt(encrypt(text, s), 26 - s)}")
def encrypt(text, key):
    rail = [['*' for i in range(len(text))] for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in text:
        if ((row == 0) or (row == key - 1)):
            dir_down = not dir_down

        rail[row][col] = i
        if dir_down:
            row += 1
        else:
            row -= 1
        col += 1
    result = []

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '*':
                result.append(rail[i][j])

    return ''.join(result)


def decrypt(cipher, key):
    rail = [['*' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in cipher:
        if row == 0 or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = "_"

        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
                if (rail[i][j] == '_' and index < len(cipher)):
                    rail[i][j] = cipher[index]
                    index+= 1
    result = []
    dir_down = False
    row, col = 0, 0
    for i in cipher:
        if row == 0 or (row == key - 1):
            dir_down = not dir_down

        result.append(rail[row][col])

        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    plain_text = ''.join(result)
    return plain_text
    
if __name__ == "__main__": 

    text = "YashGosavi"
    key = 3
    cipher = encrypt(text, key)
    plain_text = decrypt(cipher, key)
    print(plain_text)
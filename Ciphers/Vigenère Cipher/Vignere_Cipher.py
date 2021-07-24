LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
def main():
    Message = input("Messge:") #Input your message here that need to be encrypted or decrypted
    Key = input("Key:") #Input Key here
    Mode = input("Mode(encrypt / decrypt)") #Choose a mode i.e., to encrypt or decrypt

    if Mode.upper() == 'ENCRYPT': #Encrypt condition 
        translated = encryptMessage(Key, Message)
    elif Mode.upper() == 'DECRYPT': #Decrypt condition
        translated = decryptMessage(Key, Message)

    print('%sed message:' % (Mode.title()))
    print(translated)
    print()


def encryptMessage(key, message):#Encryption
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):#Decryption 
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode): #Translation
    translated = [] 
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':  #For encryption
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':  #For decryption
                num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1

            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)


if __name__ == '__main__':
    main()

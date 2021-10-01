import string

# Ceaser Cipher
# plain text: A B C D.... (if key is 3) || ascii value: 65, 66, 67, 68
# cipher text: D E F G     (adding the key to the ascii value) || ascii value: 68, 69, 70, 71


class CaeserCipher:
    def __init__(self, key=3):
        self.key = key%26
        self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:]+string.ascii_lowercase[:self.key]))
        self.e.update(dict(zip(string.ascii_uppercase, string.ascii_uppercase[self.key:]+string.ascii_uppercase[:self.key])))

        self.d = dict(zip(string.ascii_lowercase[self.key:]+string.ascii_lowercase[:self.key],string.ascii_lowercase))
        self.d.update(dict(zip(string.ascii_uppercase[self.key:]+string.ascii_uppercase[:self.key], string.ascii_uppercase)))

    def encryption(self, plaintext):
        ans = []
        for letter in plaintext:
            if letter in self.e:
                ans.append(self.e[letter])
            else:
                letter
        return ''.join(ans)

    def decryption(self, ciphertext):
        ans = []
        for letter in ciphertext:
            if letter in self.d:
                ans.append(self.d[letter])
            else:
                letter
        return ''.join(ans)

print("Input the Key: ")
key = int(input(""))
c = CaeserCipher(key) # Default key value is 3 but you can change value of key
print("Enter the Message which you want to Encrypt: ")
plain_text = input("")
print("Original text: ",  plain_text)
encrypted_text = c.encryption(plain_text)
print("Encrypted text: ", encrypted_text)
decrypted_text = c.decryption(encrypted_text)
print("Decrypted text: ", decrypted_text)
import string

# Ceaser Cipher
# plain text: A B C D.... (if key is 3) || ascii value: 65, 66, 67, 68
# cipher text: D E F G     (adding the key to the ascii value) || ascii value: 68, 69, 70, 71


class CaeserCipher:
    def __init__(self, key=3):
        self.key = key%26   # whatever the key value it is append to the ascii value of the letter

        # e is dictonary in which every key element store the item as ascii value of key element + key
        # for storing the lowercase items
        self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:]+string.ascii_lowercase[:self.key]))  # {'a': 'd', 'b': 'e'.......'z':'c'}
        #for storing the uppercase items
        self.e.update(dict(zip(string.ascii_uppercase, string.ascii_uppercase[self.key:]+string.ascii_uppercase[:self.key])))  # After updating the e {'a': 'd', 'b': 'e'.......'z': 'c', 'A': 'D', 'B':'E',.....'Z':'C'}

        # same as above description
        self.d = dict(zip(string.ascii_lowercase[self.key:]+string.ascii_lowercase[:self.key],string.ascii_lowercase))
        self.d.update(dict(zip(string.ascii_uppercase[self.key:]+string.ascii_uppercase[:self.key], string.ascii_uppercase)))

    # encryption function
    def encryption(self, plaintext):
        ans = [] # To store the letters of the encrypted message
        for letter in plaintext: # iterate every letter of the plain text
            if letter in self.e:
                ans.append(self.e[letter])
            else:
                letter
        return ''.join(ans)

    # decryption function
    def decryption(self, ciphertext):
        ans = []    # To store the letters of the decrypted message
        for letter in ciphertext: # iterate every letter of the cipher text
            if letter in self.d:
                ans.append(self.d[letter])
            else:
                letter
        return ''.join(ans)

print("Input the Key: ")
key = int(input(""))
c = CaeserCipher(key) # Default key value is 3 but you can change value of key
print("Enter the Message which you want to Encrypt: ")
plain_text = input("")  # plain text which we have to enter the message
print("Original text: ",  plain_text)
encrypted_text = c.encryption(plain_text)  # encrypted text which is return by the encryption function
print("Encrypted text: ", encrypted_text)
decrypted_text = c.decryption(encrypted_text)  # decryption text which is return by the decryption function
print("Decrypted text: ", decrypted_text)
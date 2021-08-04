from string import ascii_lowercase  #imported ascii library
from secrets import SystemRandom  #imported random library
 
alphabets = list(ascii_lowercase) # Get the list of lowercase alphabet from a-z.
numbers = [i for i in range(26)] # get the list of number from 0 to 25
# make a reference table by packing the two lists into a dictionary for encryption and decryption.
mapping_table = dict(zip(alphabets, numbers))
 
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y
 
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
# Affine cipher encryption formula: C = (a * P + b) mod 26, where C is cipher text, a is key1, P is plaintext, b is key2.
def affine_enc(key1, key2, plaintext):
    cursor = list()
    ciphertext = list()
    for p in plaintext:
        cursor.append((mapping_table[p] * key1 + key2) % 26)
    for c in cursor:
        for letter, num in mapping_table.items():
            if num == c:
 
                ciphertext.append(letter)
    return ''.join(ciphertext)
 
 
# Formula for Affine decryption: P = a^-1 (C - b) mod 26, where P is plaintext, a is key1, C is cipher text and b is key2.
def affine_decrypt(key1, key2, ciphertext):
    cursor = list()
    plaintext = list()
    for c in ciphertext:
        cursor.append((modinv(key1, 26) * (mapping_table[c] - key2)) % 26)
    for cur in cursor:
        for letter, num in mapping_table.items():
            if num == cur:
                plaintext.append(letter)
    return ''.join(plaintext)
 
 
if __name__ == "__main__":
    rng = SystemRandom()
    plaintext = input("Enter your message here: ") # Change your plaintext here
    key1 = rng.randint(1, 25)  # key1 is between 1 and 25.
 
    while modinv(key1, 26) == None:
        key1 = rng.randint(1, 25)
    key2 = rng.randint(0, 25) # key2 is between 1 and 25.
     
    print(f"Key1 is {key1}\n")
    print(f"Key2 is {key2}\n")
    print("Implementing Affine Cipher...\n")
    ciphertext = affine_enc(key1, key2, plaintext.lower())
    print(f"Encrypted cipher text of {plaintext}: {ciphertext}\n")
    actual_plaintext = affine_decrypt(key1, key2, ciphertext)
    print(f"Decrypt {ciphertext}, the plaintext is {actual_plaintext}")

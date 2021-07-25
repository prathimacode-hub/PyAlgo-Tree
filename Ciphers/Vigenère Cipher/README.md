# Vignere Ciphere
## Aim 
To implement Vignere Cipher
## Purpose
The Vignere Ciphere is an Algorithm easy to understand and implement,used to encrypting and decrypting the text. 
## Short description
- Vignere Cipher was first described in 1553 by [Giovan Battista Bellaso](https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso) 
- The Vignere Cipher help us to encrypt and decrypt the text.
- This is one of the secure encryption modes
- Vignere Cipher uses letters as a key instead of a numeric key 
- Vignere Cipher works similar to Caesar Cipher algorithm but the difference is Caesar Cipher includes algorithm for one-character shift, whereas Vignere Cipher includes key with multiple alphabets shift.
- Vignere uses a Vigenere table for encryption and decryption of the text. It is also known as tabula recta.
- The possible combinations of hacking the Vignere cipher is next to impossible

## Workflow
- Vignere Ciphere consists of two modes:
    1. Encrytption mode.
    2. Decryption mode.
- Mathematical Equations:
    - `Encryption: Ei=(Pi+Ki)mod26`
    - `Decryption: Di=(Ei−Ki)mod26`
    - Here,
      - E is Encryption.
      - D is Decryption.
      - P is plaintext.
      - K is key.
- Vignere uses a Vigenere table for encryption and decryption of the text. It is also known as tabula recta.

![Vignere Cipher](https://user-images.githubusercontent.com/85128689/126861976-baaeb39a-9fb1-4676-bd89-606c7d5e2149.png)  
**Path Link:** https://github.com/DurgaSai-16/PyAlgo-Tree/blob/main/Ciphers/Vigen%C3%A8re%20Cipher/Images/Vignere%20Table.png
- Based on the mode opted by the user this helps us to either encrypting or decrypting the message

## Compilation Steps
- Download the file [Vignere_Ciphere.py](https://github.com/DurgaSai-16/PyAlgo-Tree/blob/main/Ciphers/Vigen%C3%A8re%20Cipher/Vignere_Cipher.py)
- Run the file [Vignere_Cipher.py](https://github.com/DurgaSai-16/PyAlgo-Tree/blob/main/Ciphers/Vigen%C3%A8re%20Cipher/Vignere_Cipher.py)
- Input the `message` you want encrypt or decrypt.
- Input a strong `key` 
- Choose a mode 
    1. `Encrypt`
    2. `Decrypt`
- **Encryption:**  
    - Let our Message be "PYTHON" & Key be "MASTER"   
 
    |P|Y|T|H|O|N|
    |-|-|-|-|-|-|
    |M|A|S|T|E|R|
   
    - The first letter of the plaintext is combined with the first letter of the key. The column of plain text "P" and row of key "M" intersects the alphabet of "B" in the vigenere table, so the first letter of ciphertext is "B".
    - This process continues till the message is completely encrypted
    - So,our Encrypted text will be "BYLASE" 
 - **Decryption:**
    - Decryption is done by the row of keys in the vigenere table.
    -  First, select the row of the key letter, find the ciphertext letter's position in that row, and then select the column label of the corresponding ciphertext as the plaintext. 
    -  Let's Consider Encryption example, from that our key is "MASTER" and Encrypted text is "BYLASE"
    -  In the row of the key is "M" and the ciphertext is "B" and this ciphertext letter appears in the column "P", that means the first plaintext letter is "P".
    - This process continues till the message is completely Decrypted.

## Output
**Encryption:**  
![Encryption](https://user-images.githubusercontent.com/85128689/126864767-a193803b-ee60-4e3c-9b53-c71e2c242a6d.png)
**Path Link:** https://github.com/DurgaSai-16/PyAlgo-Tree/blob/main/Ciphers/Vigen%C3%A8re%20Cipher/Images/Encryption%20Mode.png
**Decryption:**  
![Decryption](https://user-images.githubusercontent.com/85128689/126864791-41ca2fba-363f-42be-828c-890fb6419eaf.png)
**Path Link:** https://github.com/DurgaSai-16/PyAlgo-Tree/blob/main/Ciphers/Vigen%C3%A8re%20Cipher/Images/Decryption%20Mode.png

## Author:
[NALLANI DURGA SAI](https://github.com/DurgaSai-16)

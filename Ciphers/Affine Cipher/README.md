# Affine Ciphere
## Aim
To implement Affine Cipher

## Purpose
The Affine Cipher is an algorithm used for Encryption & Decryption

## Short description
- Affine cipher is actually the multiplicative cipher combined with the Caesar cipher.
- The Affine cipher is a mono alphabetic substitution cipher.
- In Affine cipher each and every letter in an alphabet will be mapped to corresponding numeric equivalent for encryption using mathematical functions and it will be converted back into another letter.
- For decryption it uses another mathematical function that converts into integer values to obtain original message.
- The affine cipher needs two keys: 
    - Multiplicative cipher multiplication 
    - Caesar cipher addition.
- In the affine cipher program, we will split a single integer into two keys.
- **Libraries:**
    - `ascii_lowercase` Module
    - `SystemRandom` Module
    - `random` Module
    
## Workflow
- The complete process depends on length of the alphabets used.
- The letters of an alphabet of size m are first mapped to the integers in the range 0 … m-1.
- The ‘key’ for the Affine cipher consists of 2 numbers, let's call them a and b. The following discussion assumes the use of a 26 character alphabet (m = 26). a should be chosen to be relatively prime to m (i.e. a should have no factors in common with m).

|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|

- **Encryption:**
- `E ( x ) = ( a x + b ) mod m` 
    - Here,
        - modulus m is size of the alphabet
        - a and b are keys of the cipher.
        - a must be chosen such that a and m are coprime.
        
- **Decryption:**
- `D ( x ) = a^-1 ( x - b ) mod m`
    - Here,
        - a^-1 is modular multiplicative inverse of a modulo m. i.e., it satisfies the equation 1 = a a^-1 mod m .

## Compilation Steps
 - Download the file [Affine_Ciphere.py](https://github.com/manvitha3579/dummy/blob/main/Affine%20Cipher/Affine_Cipher.py)

- Run the file [Affine_Cipher.py](https://github.com/manvitha3579/dummy/blob/main/Affine%20Cipher/Affine_Cipher.py)

- Input the message you want encrypt or decrypt.

- Input any key ( usually keys will be generated randomly for strong encryption )
- Choose any mode
    - Encrypt
    - Decrypt
- Finally we will obtain encrypted and decrypted test for our input message


## Output
![AffineCipher](https://user-images.githubusercontent.com/85128689/127323297-7d314cda-69b2-4a00-afbe-7a4a0223bfb6.png)

Pathlink: https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Ciphers/Affine%20Cipher/Images/Affine%20Cipher_Output.jpeg

![AffineCipher](https://user-images.githubusercontent.com/71583695/127897246-ef2f118e-8024-4ea6-93dc-bb94551a0cb7.png)

Pathlink: https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Ciphers/Affine%20Cipher/Images/Affine%20Cipher_Output-2.jpeg

![AffineCipher](https://user-images.githubusercontent.com/71583695/127897428-ef17f49c-8105-49f9-aaeb-ba9d26c54ca6.png)

Pathlink: https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Ciphers/Affine%20Cipher/Images/Affine%20Cipher_Output-3.jpeg

![AffineCipher](https://user-images.githubusercontent.com/71583695/127897574-5c01afa5-d4bd-4b10-8a6c-7b220b5cedae.png)

Pathlink: https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Ciphers/Affine%20Cipher/Images/Affine%20Cipher_Output-4.jpeg




## Author
[Manvitha Chowdary](https://github.com/manvitha3579)

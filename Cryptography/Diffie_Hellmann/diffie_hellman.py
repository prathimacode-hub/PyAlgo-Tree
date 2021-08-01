"""
- Diffie-Hellman algorithm is used only key exchange not encryption and decryption
- A public-key distribution scheme cannot be used to exchange an arbitrary message, rather it can establish a common key
known only to the two participants value of key depends on the participants and their private and public key information

"""

p=int(input("Enter prime value chosen by A & B: "))     # number chosen by both the parties

g=int(input("Enter the primitive root: "))

a=int(input("Enter private key of A: "))            # secret key of party1

A=(g**a)%p
print("A sends to B:", A)

b=int(input("Enter private key of B: "))            # secret key of party2

B=(g**b)%p
print("B sends to A:",B)

print("\nCalculating shared secret....")

sec1=(B**a)%p
print("\nShared secret key of A is: ",  sec1)

sec2=(A**b)%p
print("Shared secret key of B is: ", sec2)
print("Therefore, both the parties obtain the same value of secret key")


"""
TEST CASES: 
Q) In a Diffie-Hellman Key Exchange, Alice and Bob have chosen prime value q = 17 and primitive root = 5. If Alice’s secret key is 4 and Bob’s secret
key is 6, what is the secret key they exchanged?

Given:-  q = 17, a = 5, Private key of Alice XA = 4, Private key of Bob XB = 6

Step-1: Both Alice and Bob calculate the value of their public key and exchange with each other.

Public key of Alice                                        Public key of Bob
= 5^(private key of Alice) mod 17                          = 5^(private key of Bob) mod 17                               
= 5^(4) mod 17                                             = 5^(6) mod 17
= 13                                                       = 2

Step-2: Both the parties calculate the value of secret key at their respective side.

Secret key obtained by Alice                    Secret key obtained by Bob
= 2^(private key of Alice )mod 7                = 13^(private key of Bob) mod 7                               
= 2^(4) mod 17                                  = 13^(6) mod 17              
= 16                                            = 16    

Finally, both the parties obtain the same value of secret key.
"""






      

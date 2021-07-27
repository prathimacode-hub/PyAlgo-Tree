p=int(input("Enter prime value chosen by A & B: "))

g=int(input("Enter the primitive root: "))

a=int(input("Enter private key of A: "))

A=(g**a)%p
print("A sends to B:", A)

b=int(input("Enter private key of B: "))

B=(g**b)%p
print("B sends to A:",B)

print("\nCalculating shared secret....")

sec1=(B**a)%p
print("\nShared secret key of A is: ",  sec1)

sec2=(A**b)%p
print("Shared secret key of B is: ", sec2)
print("Therefore, both the parties obtain the same value of secret key")






      

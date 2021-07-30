"""
*************** RSA ***************** 
- Best known & widely used public-key encryption algorithm
- Uses large integers (e.g.. 1024 bits)
- Security due to cost of factoring large numbers
- Relies on the fact that Prime factorization is computationally very hard.


************* El-Gamal *************
- ElGamal cryptosystem, is based on the Discrete Logarithm Problem
- The strength of the ElGamal is based on the difficulty of discrete logarithm problem.
- It is Asymmetric Key Cryptography
Three main components :
1. Key generation
2. Encryption
3. Decryption
"""

print("1. RSA  2. El Gamal  3. Exit")

opt=int(input("Enter the option no: "))

while opt<3:
	if opt==1:
		print()
		a=int(input("Enter the first prime no: "))		# decide 2 large prime numbers
		b=int(input("Enter the second prime no: "))
		n=a*b
		phi_n=(a-1)*(b-1)
		e=int(input("Enter the public key(e): "))		# public key should be relatively prime to ø(n)
		
		d,C=0,0
		print("Calculating d....")
		for i in range(1,20):
			d=((phi_n*i)+1)/e
			if d==int(d):
				break
			else:
				continue
		print("Private key(d): ",int(d))			# private key generated
		print(" ")
		print("Public key:{",e,",",n,"}")
		print("Private key:{",int(d),",",n,"}")
		print(" ")

		print("--------Encryption--------")
		P=int(input("Enter the decimal format of plain text message: "))		# value of plaintext
		C=(P**e)%n
		print("Ciphertext: ",C)
		print(" ")
		print("--------Decryption--------")
		P=(C**int(d))%n
		print("Plaintext:",P)			# from ciphertext we get plaintext
		print(" ")
			
			
		print("1. RSA  2. El Gamal  3. Exit")
		
		opt=int(input("Enter the option no: "))
	elif opt==2:
		P=int(input("Enter a large prime no: "))		# decide a large prime number
		D=int(input("Enter the decryption key: "))		
		E1=int(input("Enter the public key(E1): "))
		E2=(E1**D)%P									# second part of public key
		print("E2: ",E2)
		print("Public key: (",E1,",",E2,",",P,")")
		print("Private key: ",D)
		print(" ")

		print("----------Encryption----------")
		R=int(input(("Select any random integer: ")))	# select random integer
	
		C1=(E1**R)%P
		
		PT=int(input("Enter the decimal format of plain text message: ")) 	# value of plaintext
		C2=(PT*(E2**R))%P
		print("C1:",C1, "&", "C2: ",C2)
		print("CT=(",C1,",",C2,")")
		print(" ")
		print("----------Decryption----------")
		
		for x in range(1,11):					# all steps proceeds according to the algorithm
			ele=C1**D
			ele=(ele*x)%P
			if ele==1:
				index=x
				break					
			
		PT=(C2*index)%P
		
		print("PT: ",PT)
		print(" ")
		print("1. RSA  2. El Gamal  3. Exit")
	
		opt=int(input("Enter the option no: "))
	else:
		break
		

"""
TEST CASES:
1==> RSA
Q) Calculate cipher text using RSA algorithm given data as follows : 
	Prime numbers p , q as 3 , 11 respectively and plain text message 00111011 i.e. 59(Binary to Decimal)

	1. Choose p = 3 and q = 11 ,P=59
	2. Compute n = p * q = 3 * 11 = 33
	3. Compute φ(n) = (p - 1) * (q - 1) = 2 * 10 = 20
	4. Select e such that it is relatively prime to φ(n)
		i.e. gcd(e, φ(n) )=1
			 gcd(e,20)=1
			 gcd(3,20)=1
	5. Calculate d such that d= e^(-1) mod ø(n) 
		ed mod ø(n)=1
		d=(ø(n)*i+1/e

		Find d such that it is divisible by e, where i=1to 9
		d=(20*i)+1/3
		d=(20*1)+1/3
		d= 21/3
		d=7
	6. Public key is (e, n) ={3, 33}
	   Private key is (d, n) ={7, 33}
	7. Calculate cipher text message for given plain text C= Pe mod n where p<n
			C= 593 mod 33
 			 = [592 mod 33]*[59 mod 33] mod 33
			 =[3481 mod 33]*[59 mod 33] mod 33
			C=[16*26]mod 33
			C=20
	8. Calculate plain text message P= Cd mod n
			P= 207 mod 33
			 = [204 mod 33]*[203 mod 33] mod 33
			 = [202 mod 33]* [202 mod 33]* [202 mod 33]*[201mod 33] mod 33
			 = [400 mod 33]*[400 mod 33]*[400 mod 33]*[201mod 33] mod 33
			 =[4]*[4]*[4]*[20]mod 33
			 = 1280 mod 33
			P=26


2==> EL-GAMAL
Problem Steps:
Step1: Key generation
	1. Select large prime number (P) P=11
	2. Select decryption key /private key (D) D=3
	3. Select second part of encryption key or public key (E1) E1=2
	4. Third part of encryption key or public key (E2)
	E2=E1^(D)mod p--> E2 =2^(3) mod11=8
	5. Public key =(E1,E2,p)--> (2,8,11) , D=3

Step2: Encryption
	1. Select random integer R R=4
	2. C1= E1^(R)mod p ---> C1= 2^(4) mod11=5
	3. C2=(PT X E2^(R)) mod p ---> C2= (7 X 8^(4))mod 11 =6
	4. CT=(C1,C2)---> CT=(5,6)

Step3: Decryption
	1. PT =(C2 X (C1^(D))^(-1)mod p , p=11,D=3,E1=2

	PT=(6 X(5^(3))^(-1) mod 11 = 18 mod 11 =7
	PT=7

"""
		
	
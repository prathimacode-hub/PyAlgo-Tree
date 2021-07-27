print("1. RSA  2. El Gamal  3. Exit")

opt=int(input("Enter the option no: "))

while opt<3:
	if opt==1:
		print()
		a=int(input("Enter the first prime no: "))
		b=int(input("Enter the second prime no: "))
		n=a*b
		phi_n=(a-1)*(b-1)
		e=int(input("Enter the public key(e): "))
		
		d,C=0,0
		print("Calculating d....")
		for i in range(1,20):
			d=((phi_n*i)+1)/e
			if d==int(d):
				break
			else:
				continue
		print("Private key(d): ",int(d))
		print(" ")
		print("Public key:{",e,",",n,"}")
		print("Private key:{",int(d),",",n,"}")
		print(" ")

		print("--------Encryption--------")
		P=int(input("Enter the decimal format of plain text message: "))
		C=(P**e)%n
		print("Ciphertext: ",C)
		print(" ")
		print("--------Decryption--------")
		P=(C**int(d))%n
		print("Plaintext:",P)
		print(" ")
			
			
		print("1. RSA  2. El Gamal  3. Exit")
		
		opt=int(input("Enter the option no: "))
	elif opt==2:
		P=int(input("Enter a large prime no: "))
		D=int(input("Enter the decryption key: "))
		E1=int(input("Enter the public key(E1): "))
		E2=(E1**D)%P
		print("E2: ",E2)
		print("Public key: (",E1,",",E2,",",P,")")
		print("Private key: ",D)
		print(" ")

		print("----------Encryption----------")
		R=int(input(("Select any random integer: ")))
	
		C1=(E1**R)%P
		
		PT=int(input("Enter the decimal format of plain text message: "))
		C2=(PT*(E2**R))%P
		print("C1:",C1, "&", "C2: ",C2)
		print("CT=(",C1,",",C2,")")
		print(" ")
		print("----------Decryption----------")
		
		for x in range(1,11):
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
		
	
		
	
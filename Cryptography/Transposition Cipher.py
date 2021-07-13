import math

key = int(input("Enter key: "))
  
# Encryption
def encryption(msg):
    cipher = ""
    text_len = float(len(msg))
    text_list = list(msg)
    col = key
      
    # maximum row of the matrix
    row = int(math.ceil(text_len / col))
  
    # the empty cells at the end are filled with '/'
    fill_null = int((row * col) - text_len)
    text_list.extend('/' * fill_null)
  
    # create Matrix and insert message  
    matrix = [text_list[i: i + col] for i in range(0, len(text_list), col)]

#print matrix
    for i in matrix:
      print(i)
  
    # read matrix column-wise 
    key_index = 0
    for i in range(col):
        cipher += ''.join([row[key_index] for row in matrix])
        key_index += 1
  
    return cipher


def decryption(c, key):
    col = key
    col, row = key, math.ceil(len(c)/key)
    no_of_blanks = row*col-len(c)
    filled = row - no_of_blanks
      
    chars = list(c)
    if no_of_blanks != 0:
        for i in range (filled,1+key):
            chars.insert(row*i-1, " ")
        
    tmp = [chars[j+i]  for j in range(row) for i in range(0,len(chars),row) if (j+i)<len(chars)]
    return ''.join(tmp)
  
msg = input("Enter message: ")
  
cipher = encryption(msg)
print("Encrypted Message: {}".format(cipher))
  
print("Decryped Message: {}".
       format(decryption(cipher,key)))

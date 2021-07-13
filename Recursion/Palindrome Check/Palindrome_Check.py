
## Palindrome checker

def isPalindrome(s):
    """This function checks if a string is palindrome or not using recursion
        Input: String to be checked
        Output: True if it is a palindrome, False if it is not
    """
    if len(s) == 0:
        return True
    if s[0] != s[len(s)-1]:
        return False
    
    return isPalindrome(s[1:-1])


## DRIVER CODE

if __name__ == "__main__":
    s = input("Enter the string to be checked: ")
    
    # This section asks user if comparisons are case sensitive
    case = input("Is it case sensitive? (1/0): ")
    if case == '0':
        tmp = s.lower()
    else:
        tmp = s[:]

    # Calling the function
    ans = isPalindrome(tmp)

    # Formatting output based on the result
    if ans:
        print (f"\"{tmp}\" is a palindrome")
    else: 
        print (f"\"{tmp}\" is not a palindrome")
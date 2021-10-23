# LCS: There are two strings in which we have to find the length of the longest common subsequence
# Subarray: Continuous sequence in an array
# Subsequence: Need not to be contiguous, but maintains order
# Subset: Same as subsequence except it has empty set


def lcs(n, m, s1, s2):
    if n == 0 or m == 0: # if the one of the string size 0 then we returned 0
        return 0
    if s1[n - 1] == s2[m - 1]: # if string have the same letter then we add one and go to the next letter
        return 1 + lcs(n - 1, m - 1, s1, s2);
    else:                       # otherwise we do maximum of both strings 
        return max(lcs(n, m - 1, s1, s2), lcs(n - 1, m, s1, s2))

if __name__ == "__main__":
    print("Longest Common Subsequence Problem")
    s1 = input("First String: ") # input the first string
    s2 = input("Second String: ") # input the second string
    print("Length of the Longest Common Subsequence: ", lcs(len(s1), len(s2), s1, s2)) # len(s) is length of the string s 

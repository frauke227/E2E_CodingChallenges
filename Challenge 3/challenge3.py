

# Palindrome Checker
# A palindrome is a number/string that is same forwards and backwards. For example 545, 151, 34543, 343, 171, 48984 are palindrome. A string like LOL, MADAM are also palindromes. Write a function called isPalindrome that takes an variable and returns true or false if the variable is a palindrome.

def isPalindrome(n):
    x = str(n).replace(" ", "").lower()
    return x == x[::-1]


print(isPalindrome(121))

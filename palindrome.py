def palindrome(s):
    s = s.replace((" "),(""))
    return s == s[::-1]

print(palindrome('helleh'))

print(palindrome('nurses run'))

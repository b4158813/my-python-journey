def is_palindrome(n):
    return n == int(str(n)[::-1])
output = filter(is_palindrome,range(1,1000))
print(list(output))
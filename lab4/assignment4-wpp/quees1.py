def min_operations_to_palindrome(s):
    n = len(s)
    operations = 0
    
    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - i - 1]))
    
    return operations


s = input("Enter the string: ")
print("Minimum operations:", min_operations_to_palindrome(s))

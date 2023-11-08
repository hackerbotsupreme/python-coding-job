def factorial_recursive(n):
    return n*factorial_recursive(n-1)

q=factorial_recursive(5)
print(q)
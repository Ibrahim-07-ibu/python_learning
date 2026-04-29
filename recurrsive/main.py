def factorial(n):
    if n == 0:          # Base case
        return 1
    return n * factorial(n-1)   # Recursive call
print(factorial(5))


n = 10
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b



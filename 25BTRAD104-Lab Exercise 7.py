def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibo_count = int(input("How many Fibonacci numbers? "))

for i in range(fibo_count):
    print(fibonacci(i), end=" ")
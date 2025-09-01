fib1 = 1
fib2 = 2

result = 0

while fib2 < 4_000_000:
    if fib2 % 2 == 0:
        result += fib2
    fib1, fib2 = fib2, fib1 + fib2

print(result)
import math
N = 600851475143

ans = N
div = 2
roof = int(math.sqrt(ans) + 1)

while div < roof:
    for div in range(2,roof):
        if ans % div == 0:
            ans = ans / div
            roof = int(math.sqrt(ans) + 1)
            break

print(ans)

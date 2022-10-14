n = int(input())
a = n
while True:
    is_prime = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime == True:
            break
    else:
            a += 1

x= abs(n-a)

b = n
while True:
    is_prime = True
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            is_prime = False
            break
    if is_prime == True:
            break
    else:
            b -= 1

y= abs(n-b)

if x < y:
    print(x)
else:
    print(y)
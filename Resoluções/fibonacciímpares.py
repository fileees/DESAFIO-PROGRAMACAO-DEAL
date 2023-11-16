a, b = 1, 1
c = 1

while c <= 30:
    if a%2 != 0:
        print(a)
    a = b
    b = a + b
    c += 1

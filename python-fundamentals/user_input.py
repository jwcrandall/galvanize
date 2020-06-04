total, x = 0, 1
while x <= 8:
    if x == 5:
        x += 1
        continue
    total += x
    x += 1
    print total, x
print total

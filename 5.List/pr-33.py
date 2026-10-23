
a = [1, 2, 3, 6, 8, 9, 7, 4, 52, 14, 23, 65]

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)

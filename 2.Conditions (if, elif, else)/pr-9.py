a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

largest = max(a, b, c)

print("Largest number is:", largest)

if a == b == c:
    print("All three numbers are equal.")
elif a == b == largest:
    print("First and second numbers are tied for largest.")
elif a == c == largest:
    print("First and third numbers are tied for largest.")
elif b == c == largest:
    print("Second and third numbers are tied for largest.")
a = int(input("Entyer the first number: "))
b = int(input("Enter the second number: "))

print("Choose the operator:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
ch = int(input("Enter your choice(1-4): "))

if ch == 1:
    print("The sum of", a, "and", b, "is", a + b)
elif ch == 2:
    print("The difference between", a, "and", b, "is", a - b)
elif ch == 3:
    print("The product of", a, "and", b, "is", a * b)
elif ch == 4:
    if a == 0:
        print("Division by zero is not allowed")
    elif b == 0:
        print("Division by zero is not allowed")
    else:
        print("The division of", a, "by", b, "is", a / b)
else:
    print("Invalid choice")
str = input("Enter a string: ")

reverse = ""

for i in str:
    reverse = i + reverse

print("The reverse of the string is:", reverse)
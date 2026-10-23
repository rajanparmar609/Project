text = input("Enter the text: ")

reverse = ""

for i in text:
    reverse = i + reverse

print("The reverse of the text is: ", reverse)

if reverse == text:
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")

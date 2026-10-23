n = input("Enter a string: ")

vowelcount = 0

for i in n:
    if i in "aeiouAEIOU":
        vowelcount += 1
        print(i, "is a vowel")
    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        print(i, "is a consonant")
    else:
        print(i, "is a special character")

print("The number of vowels is:",vowelcount)
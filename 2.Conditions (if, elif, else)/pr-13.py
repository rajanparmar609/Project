
ch = input("Enter a character: ").lower()

if len(ch) != 1 or not ch.isalpha() or not ch.isascii():
    print("Invalid input")
elif ch in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")

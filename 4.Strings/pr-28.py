text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

if sorted(text1) == sorted(text2):
    print("The words are anagrams.")

else:
    print("The words are not anagrams.")
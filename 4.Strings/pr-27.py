str = input("Enter the string: ")

max_char = 0
max_frequent = ""

for i in str:
    if str.count(i) > max_char:
        max_char = str.count(i)
        max_frequent = i

print("This the most frequent time appraes is:", max_frequent)
print("Number of times it appears is :", max_char)
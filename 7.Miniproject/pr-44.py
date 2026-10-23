print("Is Python interpreted language?")
print("1) Yes")
print("2) No")
ans1 = input("\n Answer: ")

print("\nWhich is not python library?")
print("1) Numpy")
print("2) Tensorflow")
print("3) Pytorch")
print("4) Java")
ans2 = input("\n Answer: ")

print("\nWhat is pip in python?")
print("1) Package manager")
print("2) Package installer")
print("3) Package uninstaller")
print("4) Package")
ans3 = input("\n Answer: ")

print("\nWhich is the function used to print in python?")
print("1) print()")
print("2) display()")
print("3) input()")
print("4) output()")
ans4 = input("\n Answer: ")

print("Which Data Type is used in Python?")
print("1) list")
print("2) tuple")
print("3) dict")
print("4) all of the above")
ans5 = input("\n Answer: ")

print("\n\n")
score = 0

if ans1 == "1":
    print("The answer is \"Yes\" correct")
    score += 1
else:
    print("The answer is incorrect. Correct answer is \"Yes\"")

if ans2 == "4":
    print("The answer is \"Java\" correct")
    score += 1
else:
    print("The answer is incorrect. Correct answer is \"Java\"")

if ans3 == "1":
    print("The answer is \"Package manager\" correct")
    score += 1
else:
    print("The answer is incorrect. Correct answer is \"Package manager\"")

if ans4 == "1":
    print("The answer is \"print()\" correct")
    score += 1
else:
    print("The answer is incorrect. Correct answer is \"print()\"")

if ans5 == "4":
    print("The answer is \"all of the above\" correct")
    score += 1
else:
    print("The answer is incorrect. Correct answer is \"all of the above\"")

print("\n\n")
print("Your score is", score)
r = [5,74,59,63,47,88,996,547,5225,65,41,5,2,5,51845,14845,55]

largest = None
second_largest = None

for i in r:
    if largest is None or i > largest:
        second_largest = largest
        largest = i
    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i

print("Largest number:", largest)
print("Second-largest distinct number:", second_largest)

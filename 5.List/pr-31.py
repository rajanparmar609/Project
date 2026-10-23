a = [7,1,5,6,6,4,1,1,2,2,3,9,5,6,3,2,1]

b = []
for i in a:
    if i not in b:
        b .append(i)
print("Original list:" , a)
print("New list: ", b)
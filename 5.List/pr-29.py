a = [52,3,25,84,1,2,35,69,74]

larger = []
smaller = []

for i in a:
    if i > 50:
        larger .append(i) 
    else:
        smaller .append(i)

print("This numbers are larger ",larger)
print("This numbers are smaller ",smaller)

# d1 = 1
# d2 =2
# d3 = 3

# d4 = d1+d2+d3
# d1=d2
# d2=d3
# d4=d4





n = int(input("Enter the length of the sequence: ")) # Do not change this line

d1 = 1
d2 = 2
d3 = 3

print(d1)
print(d2)
print(d3)

for num in range(n-3):
    d4 = d1+d2+d3
    d1 = d2
    d2 = d3
    d3 = d4
    print(d4)
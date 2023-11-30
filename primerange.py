n = int(input("Enter a start of the range: "))
z = int(input("Enter a end of the range: "))

#range
#zakres = []
#for i in range(n,z+1):
#    zakres.append(i)
zakres = list(range(n, z+1))

#dla każdego elementu w liście zakres
for x in zakres:
    d = 0
    
    for i in range (1, x+1):
        if x % i == 0:
            d += 1
        
    if d == 2:
        print(x, end=" ")


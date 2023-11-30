x = input("Poproszę o liczbę: ")

y = len(x)
c = 0
for i in range(y):
    a = x[i]
    a = int(a)
    c += a

print(c)
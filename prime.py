n = int(input("Enter a number: "))

dzielniki = 0

#i = n
#while i > 0:
 #   if n % i == 0:
  #      dzielniki += 1
   # i -= 1
   
for i in range (1, n+1):
    if n % i == 0:
        dzielniki += 1


if dzielniki == 2:
    print(n, "is a prime number")
else:
   print(n, "isn't a prime number")
z = input("Enter a string: ")
a = z.lower()
vowels = ["a", "e", "i", "o", "u", "y"]

x = len(a)
l = len(vowels)
i = 0
v = 0

#while i < l:
 #   b = a.count(vowels[i])
  #  i += 1
   # v = v + b
for i in vowels:
    v += a.count(i)


print("Vowels:", v)
print("Consonants", x - v)
#print(x)


#l = len(vowels)

#for _ in range (0,l):
 #   b = a.count(vowels[l]})
  #  if b > 0:
   #     c = c + b






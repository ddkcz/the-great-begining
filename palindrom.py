a = input("Enter a word: ")
# odwracanie stringa
# a = b[::-1]
if a == a[::-1]:
    print(a, "it is a polindrom")
else: 
    print(a, "it isn't a palindrom")
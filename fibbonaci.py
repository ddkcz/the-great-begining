# Initialize the first two numbers in the Fibonacci sequence
a, b = 0, 1

# Iterate using a for loop to generate and print the first 15 Fibonacci numbers
for _ in range(15):
    print(a, end=' ')
    a, b = b, a + b
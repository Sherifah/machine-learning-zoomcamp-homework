#print("Hello World")

"""
x = input("Enter your name: ")
print(f"Your name is {x}")
"""

"""
successful = False
for number in range(1, 3):
    print(f"Attempt {number} {number * '.'}")
    if successful:
        print("Successful")
        break
"""

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print (x)
print(f"We have {count} even numbers")
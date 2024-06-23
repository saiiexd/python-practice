# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s = set()  # Initialize the set to store unique numbers

n1 = input("Enter number 1: ")
s.add(int(n1))

n2 = input("Enter number 2: ")
s.add(int(n2))

n3 = input("Enter number 3: ")
s.add(int(n3))

n4 = input("Enter number 4: ")
s.add(int(n4))

n5 = input("Enter number 5: ")
s.add(int(n5))

n6 = input("Enter number 6: ")
s.add(int(n6))

n7 = input("Enter number 7: ")
s.add(int(n7))

n8 = input("Enter number 8: ")
s.add(int(n8))

print("Unique numbers:", s)  # Print the set of unique numbers

name = input("Please enter your name: ")
age = int(input("Please enter your age {0}: ".format(name)))

if 18 < age < 31:
    print("Welcome to the holiday")
else:
    print("Go away from me")
# File name: OddOrEven.py
# Author: Kyle Barker
# Email Address: kb33@usca.edu
# Test # 1, Part 2
# Description: This program checks whether a number is odd or even, only using whole numbers between 1 and 50 and gives an error message for invalid inputs
# Last changed: February 11th, 2019 at 3:40 PM
print("======================================================================")
print("Odd or Even Game")
print("MENU OPTIONS\n1-Enter a number(between 1...50) to check\n2-Exit Program")
print("======================================================================")
#receive menu input
while True:
    options=input("Menu Options: ")
    if options=="2":
        break
    elif options=="1":
#receive integer input
        print("Check odd or even")
        n=int(input("Please enter a number: "))
        if n in range(1, 51, 2):
            print("Your number is odd")
            continue
        elif n in range(2, 51, 2):
            print("Your number is even")
            continue
#Invalid integer message
        else:
            print("Invalid integer, only use numbers between 1 and 50")
#Invalid menu message
    else:
        print("Not a valid menu option, use 1 to check for odd or even, use 2 to exit")
print("Bye!")

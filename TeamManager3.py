#!/usr/bin/env python3
def welcome():
    print("======================================================================")
    print("Baseball Team Manager")
    print("MENU OPTIONS\n1-Calculate batting average\n2-Exit Program")
    print("======================================================================")

def calculate_average():
    print("Calculate batting average...")
    at_bats=int(input("Official number of at bats:\t"))
    hits=int(input("Number of hits: "))
    average = hits/at_bats
    print("Batting average: "+str(round(average, 3)))

def main():
    welcome() 
    while True:
        options=input("Menu Options: ")
    if options=="1":
#calculate batting average based off hits and at bats
        
#give result
        print("Bye!")
    elif options=="2":
        print("Bye!")
    if options=="3":
        print("Not a valid menu option, use 1 to calculate batting average, use 2 to exit program.")
    print("MENU OPTIONS\n1-Calculate batting average\n2-Exit Program")


    



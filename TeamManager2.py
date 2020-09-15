#!/usr/bin/env python3
def print_welcome(message):
    def calculate_average(at_bats, hits, average):
        def main():
            print("======================================================================")
print("Baseball Team Manager")
print("MENU OPTIONS\n1-Calculate batting average\n2-Exit Program")
print("======================================================================")
while True:
    options=input("Menu Options: ")
    if options=="1":
#receive inputs
        print("Calculate batting average...")
        at_bats=int(input("Official number of at bats:\t"))
        hits=int(input("Number of hits: "))
#calculate batting average based off hits and at bats
        average = hits/at_bats
#give result
        print("Batting average: "+str(round(average, 3)))
        print("Bye!")
    elif options=="2":
        print("Bye!")
    if options=="3":
        print("Not a valid menu option, use 1 to calculate batting average, use 2 to exit program.")
    print("MENU OPTIONS\n1-Calculate batting average\n2-Exit Program")


    



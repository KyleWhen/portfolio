#!/usr/bin/env python3

#display title
print("======================================================================")
print("Baseball Team Manager")
print("This program calculates the batting average for a player based on the player's official number of at bats and hits")
print("======================================================================")

#receive inputs
player_name=str(input("Player's name:\t\t"))
at_bats=int(input("Official number of at bats:\t\t"))
hits=int(input("Number of hits:\t\t"))

#calculate batting average based off hits and at bats
average= hits/at_bats
average = round(average, 3)

#give result
print(player_name +"'s batting average is\t\t"+str(average))

#################################
# File: volume.py
# Author: Benjiman Walsh
# Date: February 7, 2021
# Description: Program that calculates the volume of a 
#  cube for CS 362 HW4 Question 1
#################################



def cube_volume(length):
    if(length > 0):
        return length*length*length
    else:
        raise ValueError

#length = input("Length: ")

#print(cube_volume(int(length)))

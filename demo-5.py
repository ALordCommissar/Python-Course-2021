# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:00:30 2021

@author: Daniel Mishler
"""
# Exceptions (when things get messy)
# Spaghetti code

# Try-except

# Always ask for permission never forgiveness (use ifs)

# Always ask for forgiveness never permission
try:
    quotient = 9/1
except:
    quotient = None
print(quotient)

try:
    newFile = open("newFile.txt","r")
    print(newFile.read())
    newFile.close()
except:
    print("File not found!")
    
# Strengths of try-except:
    # Doesn't crash code (vital for longevity)
    # Extends the ease of use of python (it would be HARDER or SLOWER to do without)
# Weaknesses of try-except:
    # HIDES the errors (it takes work to debug)
    # try-except is addictive and OFTEN there are better and more readable ways
        # (It's like a spice)


# find()

interpretString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print(interpretString)
# find() will always return the index of the FIRST match
# If find() returns -1, then the pattern was not found.
# no one said find() had to search for single characters:
    # You can search strings.

# split()
# splits a string based on its whitespace
splitMe = "Hello my name is Daniel"
newList = splitMe.split()
print(newList)

# aside: index() is find() for lists
# index() is to lists as find() is to strings.

interpretSplit = interpretString.split('l')
print(interpretSplit)
# By default, splits on all whitespace. Otherwise, splits on your argument.

# Slice

sliceMe = [1,1.1,1.2,1.3,1.4,1.5,1.6]

# sliceMe[a:b]
# a subarray consisting of index a, and all indexes up to but NOT including b.
# If an argument is missing, then go to the end.


def findAC(ACstring):
    # Take a string that contains an armor class and return an int (that is AC)
    print("converting",ACstring,"to int")
    try:
        AC = int(ACstring)
    except:
        ACsplit = ACstring.split()
        AC = int(ACsplit[0])
    return AC


AC1 = findAC("10")
AC2 = findAC("13 (armor scraps)")

print(AC1,AC2)

def findACBetter(ACstring):
    # Take a string that contains an armor class and return an int (that is AC)
    print("converting",ACstring,"to int")
    ACsplit = ACstring.split()
    AC = int(ACsplit[0])
    return AC

AC1 = findACBetter("10")
AC2 = findACBetter("13 (armor scraps)")

print(AC1,AC2)
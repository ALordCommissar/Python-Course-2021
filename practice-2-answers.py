# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:35:40 2021

@author: Donald Whitworth
"""

# Practice problem 1
# Here's a random seed.
import random
random.seed(5)
# Run this program. What does the following print function output?
print(random.randint(1,20))
# It outputs: _____
# Now CHANGE the Random seed so that it outputs a 20 first, every time.
# You may have to do some guess and check.

# Practice problem 2
# There are other methods in "random" that exist.
# For example, random can generate real numbers randomly, too.
# Make a print statement below that prints a random *real* number
# Between 0 and 1.
# Yes, I just asked you to use the internet to find out how to do it.
# The ability to find what you need to solve problems is the key
# To being a great programmer.

print(random.uniform(0,1))

# Practice problem 3
# Create a class called "Dog"
# The "Dog" has a member variable called mood
    # It should be initialized to "playful"
# The "Dog" should have two member functions.
    # The first should be called "play()" and sets its mood to "hungry"
    # The second should be called "feed()" and sets its mood to "playful"
    
class Dog:
    def __init__(self):
        self.mood = "playful"
        print("Spot is",self.mood)
        return
    def play(self):
        self.mood = "hungry"
        print("Spot is",self.mood)
        return
    def feed(self):
        self.mood = "playful"
        print("Spot is",self.mood)
        return

# Practice problem 4
# Remember how we made a Die class in class?
# Go ahead and copy-paste that code below. Then add a new method to
# the class. Call this method "Advantage()".
# The method will roll twice and return the higher of the two rolls.

class Die:
    def __init__(self,dieMax):
        self.max = dieMax
        self.name = "d"+str(self.max)
        return
    def roll(self):
        return random.randint(1,self.max)
    def loudRoll(self):
        result = random.randint(1,self.max)
        print(self.name,"rolls",result)
        return result
    def Advantage(self):
        result1 = random.randint(1,self.max)
        result2 = random.randint(1,self.max)
        if result1 > result2:
            return result1
        else:
            return result2


# Practice problem 5
# Remember how we made a Die class in class?
# You don't *have* to have dice use the randint function for your
# Random number generation. Check this out: I can create a "rigged"
# die like this. (When you get here, remove the commenting ''' and try it)

outcomes = [1,1,2,3,6,6]
for i in range(10): # Do the following 10 times.
    index = random.randint(1,6) - 1 # could also say randint(0,5)
    print(outcomes[index])

# Use this idea to create a class that rolls a 20-sided die,
# except instead of having all numbers 1-20, skip 19 and replace it
# with 20.



class D20:
    def __init__(self):
        return
    def roll(self):
        outcomes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,20]
        index = random.randint(1,20) - 1
        return outcomes[index]
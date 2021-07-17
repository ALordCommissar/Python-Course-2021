# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:11:03 2021

@author: Donald Whitworth
"""

# Practice problem 1:

# properly import the "utils.py" library. You can do it however you want.
# Run this code and make sure that "utils loaded successfully" prints.

import json
import time
import utils

# Note: you are absolutely allowed to change things in the utils.py file,
# But (like any professional coding environment), you should ensure that
# any code you write will still run and work with the default utils.py!


# Practice problem 2:
# (this one is review for for loops)
# What is the average result of a D20 rolled with advantage?
# Write whatever code you need to determine this answer below.

firstDie = utils.Die(20)
secondDie = utils.Die(20)
rollWrite = open("rolls.txt","w")
for i in range(1000):
    result1 = firstDie.roll()
    result2 = secondDie.roll()
    if result1 >= result2:
        rollWrite.write(str(result1))
        rollWrite.write("\n")
    else:
        rollWrite.write(str(result2))
        rollWrite.write("\n")

rollWrite.close()

rollRead = open("rolls.txt","r")
numbers = rollRead.read()
numList = numbers.split()
for number in numList:
    number = int(number)
realNumList = []
for number in numList:
    realNumList.append(int(number))
result = 0
for number in realNumList:
    result += number
print(result/1000)
rollRead.close()



# Answer in a comment here:
"""
13.8
"""
# No, googling the answer is not good enough
    # (but you can use that to check your work!)



# Practice problem 3:
# Go ahead and download and run that "Utils testing" file and fiddle
# around for a bit.
    # How many zombies are needed so that they have a 1% chance to win?
"""
9
"""
    # How many zombies are needed so that they have a 66% chance to win?
"""
12
"""
    # How many zombies are needed so that they have a 99% chance to win?
"""
17
"""
# There's another file I made on the website called "fightSimulation.txt"
# That file is the result of a huge number of fights from the demo code!
# How many times did the troll win total?
simRead = open("fightSimulation.txt","r")
simResults = simRead.read()
realResults = simResults.split()
result = 0
for data in realResults:
    if data == str("Troll"):
        result += 1
    else:
        continue
print(result)
simRead.close()
"""
660
"""
# What was his victory percentage?
"""
66%
"""
# How many zombies did I have fighting the troll?
"""
12
"""

# Yes, you'll probably need to write some file parsing here.




# Practice problem 4:
# Write a function called "monsterFromFile"
# That takes the name of a file as an argument.
# This function will find out the monster's armor class, attack bonus,
# damage dice, damage bonus, and even name. It will return a monster
# With all of this information properly allocated. This way you can
# define monsters much more easily! You just have to say something like
# skeleton = monsterFromFile('skeleton.monster')
# And that's all you need! So much simpler.

def monsterFromFile(filename):
    monFile = open(filename,"r")
    monText = monFile.read()
    monDict = json.loads(monText)
    monFile.close()
    monsterName = monDict["name"]
    monsterHitDice = monDict["hitDice"].split()
    monsterHitDice = int(monsterHitDice)
    monsterHP = monsterHitDice*7
    monsterAttBonus = 1
    monsterDamBonus = 2
    monsterDamDie = utils.Die(6)
    armorList = monDict["otherArmorDesc"].split()
    for armor in armorList:
        if armor == str("13"):
            AC = int(armor)
        else:
            continue
    monsterAC = AC
    monster = utils.rollingMonster(monsterHP,monsterDamDie,monsterDamBonus,monsterAttBonus,monsterAC,monsterName)
    return monster

skeleton = monsterFromFile('skeleton.monster')

# Once you've written the function, finish it out by downloading
# the acolyte and skeleton files from the website





# Practice problem 5:
# Copy the "fightManyRoll" function from utils.py here.
# Change the name to "fightManyRollPrint"
# At the end of each fight, this function will append to a file
# (call the file whatever you want) the following information:
# - A fight has just occurred
# - The winner
# - how many monsters fought on each side
# - The names of all the monsters involved
# - The total remaining current HP of the winning side

def fightManyRollPrint(soloMonster,group,suspense = False,printing = True):
    if not soloMonster.alive:
        print("You forgot to refresh")
        return
    for monster in group:
        if not monster.alive:
            print("you forgot to resfresh")
            monster.show()
            return
    while True:
        if suspense:
            time.sleep(2)
        if printing:
            print(soloMonster.name, "vs", "monster group")
            soloMonster.show()
            for monster in group:
                monster.show()
        # First, the big monster tries to hit one in the group
        for monster in group:
            if monster.alive:
                target = monster
                break
        if soloMonster.attack() >= target.AC:
            target.damage(soloMonster.hit())
        # Then, each living monster gets a chance to attack
        for monster in group:
            if monster.alive:
                if monster.attack() >= soloMonster.AC:
                    soloMonster.damage(monster.hit())
        if not group[-1].alive or not soloMonster.alive:
            break
    victor = ""
    if soloMonster.alive:
        if printing:
            print("the victor is", soloMonster.name)
            soloMonster.show()
            victor = soloMonster.name
        return soloMonster.name
    else:
        if printing:
            print("the victor is", "the monster group")
            for monster in group:
                monster.show()
            victor = "Monster group"
        return "group"
    fightManyAppend = open("fightMany.txt","a")
    fightManyAppend.write("A fight has just occured\nThe winner is:",victor,"\n")
    numMonsters = 0
    monNames = []
    for monster in group:
        numMonsters += 1
        monNames.append(monster.name)
    fightManyAppend.write("The number of monsters in group is:",numMonsters,"\nMonsters in the group:",monNames,"\n")
    if victor == soloMonster.name:
        fightManyAppend.write("Total remaining HP:",soloMonster.HP)
    else:
        groupHP = 0
        for monster in group:
            monster.HP += groupHP
        fightManyAppend.write("Total remaining HP:",groupHP)
    fightManyAppend.close()

# Now, have one skeleton fight two acolytes
# a couple times in this new function.


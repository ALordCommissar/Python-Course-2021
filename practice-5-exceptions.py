# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:00:39 2021

@author: Donald Whitworth
"""

import utils
import json
import math
import time

# Practice problem 1a:
# Remember the try-except block we learned in class?
# Take a look at this division function

def ironDivision(a,b):
    if b == 0:
        return None
    if type(a) != int:
        if type(a) != float:
            return None
    if type(b) != int:
        if type(b) != float:
            return None
    else:
        quotient = a/b
        return quotient

# Go back into that function and use some if statements to handle the
# following:
    # if b is equal to 0, just return "None"
    # if a is not an integer or float, just return "None"
    # if b is not an integer or float, just return "None"

# Practice problem 1b:
# Let's tackle the same problem in a different way

def lazyDivision(a,b):
    try:
        quotient = a/b
    except:
        quotient = None
    return quotient
   

# This time, fix all of the above problems, except do it
# WITHOUT if statements and do it in no more than 5 lines!

# Practice problem 2:
# Last week, I was hard on you with monsterFromFile. This week, we're
# going to finish it out now.
# You should already have the AC and name of the creature down pat.

# HP:
    # The HP of the monster is calulated as follows:
        # (number of hit dice) * (hit dice average roll + constitution mod)
    # The number of hit dice and the constitution mod are in the monster Dict!
    # The hit dice type is found in the monster's size. If the monster is:
        # Tiny: d4 (average 2.5)
        # Small: d6 (average 3.5)
        # Medium: d8 (average 4.5)
        # Large: d10 (average 6.5)
        # Huge: d12 (average 10.5)
        # Gargantuan: d20
    # Finally, round up if you found something that ends in 0.5

# Attack Bonus:
    # Take a look at the "actions" key. It might be an array, it might
    # be another dict. Figure out how you're going to handle this!
    # Then, once you have a string that has an attack bonus in it,
    # Find out how to pick out that number.
    # I'd recommend looking into the .find() method for strings
    # and knowing how to splice!

# Damage bonus:
    # Just like you found the attack bonus, hunt down the damage bonus
    # in the same string. It can be found in the open and close parentheses!

# Damage diece:
    # Be cautious with this one: it's found next to the damage bonus,
    # but be sure you parse the NUMBER of dice and the TYPE of die correctly,
    # and be ready to create a utils.Dice() array of all the dice used!
    # If you're having trouble, just start with one die instead, and go
    # from there.

def monsterFromFile(filename):
    monFile = open(filename,"r")
    monText = monFile.read()
    monDict = json.loads(monText)
    monFile.close()
    
    monName = monDict["name"]
    
    ACstring = monDict["otherArmorDesc"].split()
    monAC = int(ACstring[0])

    monsterHitDice = monDict["hitDice"]
    if monDict["size"] == "tiny":
        avgRoll = 2.5
    elif monDict["size"] == "small":
        avgRoll = 3.5
    elif monDict["size"] == "medium":
        avgRoll = 4.5
    elif monDict["size"] == "large":
        avgRoll = 5.5
    elif monDict["size"] == "huge":
        avgRoll = 6.5
    elif monDict["size"] == "gargantuan":
        avgRoll = 10.5
    conPoints = monDict["conPoints"]
    conMod = ((conPoints)-10)//2
    monsterHP = math.ceil(monsterHitDice*(avgRoll+conMod))
    
    findBonus = monDict["actions"][0]["desc"].find("+")
    monAttBonus = int(monDict["actions"][0]["desc"][findBonus+1])
    
    findDamStr = monDict["actions"][0]["desc"].find("(")
    findDamStrEnd = monDict["actions"][0]["desc"].find(")")
    actStr = monDict["actions"][0]["desc"]
    actStrSlice = slice(findDamStr,findDamStrEnd)
    damStr = actStr[actStrSlice]
    
    findDamBonus = damStr.find("+")
    if findDamBonus == -1:
        monDamBonus = 0
    else:
        monDamBonus = int(damStr[findDamBonus+2])
        
    numDie = int(damStr[1])
    monDamDie = utils.Die(int(damStr[3]))
    
    monster = utils.rollingMonster(monsterHP,monDamDie,monDamBonus,monAttBonus,monAC,monName)
    return monster

# Practice problem 3:
# We're going to bring it all home:
# write a function called "fightFinal" that will:
    # Have a group of monsters fight a second group of monsters.
        # Turn order goes as the following:
            # First alive group A monster attacks first alive group B monster
            # First alive group B monster attacks first alive group A monster
            # Second alive group A monster attacks first alive group B monster
            # Second alive group B monster attacks first alive group A monster
            # Third alive group A monster attacks first alive group B monster
            # Third alive group B monster attacks first alive group B monster
            # ...
            # And so on. If a monster group only has 3 versus 7, then the
            # group with more monsters gets to all act before the next round
            # starts. So a fighting order with [A1,A2,A3] vs. [B1,B2,B3...B8]
            # might look like:
                # A1 -> B1
                # B1 -> A1
                # A2 -> B1 (kills it)
                # B2 -> A1
                # A3 -> B2
                # B3 -> A1
                # B4 -> A1 (kills it)
                # B5 -> A2
                # B6 -> A2
                # B7 -> A2
                # B8 -> A2
    # The monsters are all rolling monsters, of course.
    # Also: still print the results of the fight like last assignment,
    # now accounting for the groups.
# You should be able to properly read
    # Zombie
    # Skeleton
    # Acolyte

def fightFinal(group1,group2,suspense = False,printing = True):
   for monster in group1:
        if not monster.alive:
            monster.refresh()
   for monster in group2:
        if not monster.alive:
            monster.refresh()
   
   tarIndex1 = 0
   tarIndex2 = 0
   while True:
        if suspense:
            time.sleep(2)
        if printing:
            print("Team Deathmatch")
            for monster in group1:
                monster.show()
            for monster in group2:
                monster.show()
                
        if len(group1) >= len(group2):
            maxLength = len(group1)
        else:
            maxLength = len(group2)
        
        for i in range(maxLength):
            try:
                if not group1[tarIndex1].alive:
                    tarIndex1 += 1
                else:
                    pass
                if not group2[tarIndex2].alive:
                    tarIndex2 += 1
                else:
                    pass
            except:
                pass
            if not group1[-1].alive or not group2[-1].alive:
                break
            if group1[i].attack() >= group2[tarIndex2].AC:
                group2[tarIndex2].damage(group1[i].hit())
            if group2[i].attack() >= group1[tarIndex1].AC:
                group1[tarIndex1].damage(group2[i].hit())
            
        if not group1[-1].alive or not group2[-1].alive:
            break
   victor = ""
   if group1[-1].alive:
        if printing:
            print("the victor is", "the first monster group")
            for monster in group1:
                monster.show()
        victor = "First Monster Group"
   else:
        if printing:
            print("the victor is", "the second monster group")
            for monster in group2:
                monster.show()
        victor = "Second Monster Group"
   fightFinalAppend = open("fightFinal.txt","a")
   fightFinalAppend.write("\nA fight has just occured\nThe winner is:"+victor+"\n")
   numMonsters = 0
   monNames = []
   for monster in group1:
        numMonsters += 1
        monNames.append(monster.name)
   fightFinalAppend.write("The number of monsters in the first group is:"+str(numMonsters)+"\nMonsters in the group:"+str(monNames)+"\n")
   numMonsters = 0
   monNames = []
   for monster in group2:
        numMonsters += 1
        monNames.append(monster.name)
   fightFinalAppend.write("The number of monsters in the second group is:"+str(numMonsters)+"\nMonsters in the group:"+str(monNames)+"\n")
   if victor == "First Monster Group":
       group1HP = 0
       for monster in group1:
           group1HP = monster.curHP + group1HP
       fightFinalAppend.write("Total remaining HP:"+str(group1HP))
   else:
       group2HP = 0
       for monster in group2:
            group2HP = monster.curHP + group2HP
       fightFinalAppend.write("Total remaining HP:"+str(group2HP))
   fightFinalAppend.close()
   return victor
# Practice problem 4a:
# Have 3 zombies and 3 skeletons fight 6 skeletons.
team1 = []
team2 = []
for i in range(3):
    team1.append(monsterFromFile("zombie.monster"))
for i in range(3):
    team1.append(monsterFromFile("skeleton.monster"))
for i in range(6):
    team2.append(monsterFromFile("skeleton.monster"))
fightFinal(team1,team2,False,False)
# Empirically show who wins if the zombies and skeletons array is
# organized so that the zombies act and are hit first.
# A mathematical argument is not good enough. Use python to prove it.
# (one fight is not enough)
team1wins = 0
team2wins = 0
for i in range(10):
    fightFinal(team1,team2,False,False)
    if fightFinal(team1,team2,False,False) == "First Monster Group":
        team1wins += 1
    else:
        team2wins += 1
print("Team 1 wins:",team1wins)
print("Team 2 wins:",team2wins)
# 4b: do the same for if the skeletons act and are hit first.
team3 = []
for i in range(1000):
    team3.append(monsterFromFile("skeleton.monster"))
for i in range(3):
    team3.append(monsterFromFile("zombie.monster"))
team1wins = 0
team2wins = 0
for i in range(1000):
    fightFinal(team3,team2,False,False)
    if fightFinal(team3,team2,False,False) == "First Monster Group":
        team1wins += 1
    else:
        team2wins += 1
print("Team 1 wins:",team1wins)
print("Team 2 wins:",team2wins)

"""
As far as I can tell, regardless of whether the skeletons or the zombies are at the front of the team, so to speak, the all skeleton team wins at a similar rate of about 70%
"""

# Practice problem 5:
"""
Make an extension to our code to include something we don't have yet!
"""
# Suggestion:
# Note that the "Troll" is a class that exists sort of outside the
# normal generic monster class. That's because the troll is special:
# our code infrastructure isn't really designed to handle all these
# special abilities in a generic rolling monster.
# However, we made the troll regenerate before it attacks
# so that it fits into our fight function.
# (shoot, actually there's a bug where it does it before it hits,
# why don't you go ahead and fix that?)
# Pick any monster that has a special ability like the troll.
# (Hell, even the Zombie's undead fortitude is good enough)
# And make a monster class for it.

# Suggestion:
# Add an initiative system for the monsters

# Suggestion:
# Implement a mechanic of ranged attacks versus melee attacks

# Suggestion:
# Implement ciritical attacks (roll 20 = autohit and double dice)
# alongisde critical fails (roll 1 = miss your attack)

# Or anything else that you wish!
# Submit any relevant changes to known files to me as well.
# For this assignment, it is okay if you change utils.py
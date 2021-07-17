# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:31:12 2021

@author: whitw
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:51:35 2021

@author: Daniel Mishler
"""
import random
import time

class Die:
    def __init__(self,dieMax):
        self.max = dieMax
        self.name = "d"+str(self.max)
        return
    def roll(self): # Always use "self" as first argument!
        return random.randint(1,self.max)
    def loudRoll(self):
        result = random.randint(1,self.max)
        print(self.name,"rolls",result)
        return result

# Need to cover:
    # Copy-pasting class code at the top of a file.
    # For loops basics (10 minutes: use list of strings as example)
    # Monster classes: (~20 minutes: Make a Zombie and skeleton)
            # damage
            # hit
            # alive (data)
            # print
    # Bigger functions (~10 minutes: fight zombie vs skeleton)
    # Non-generic monsters: Troll


# Looping
# we will be using "While" and "for"

variable = 0
if variable == 0:
    print("variable is 0")
else:
    print("variable is not 0")
    
# "while" works the same way

while variable < 10:
    # you can stop a program with cntrl+c
    print("variable is ", variable)
    variable = variable + 1

while True: # Is just like saying 'while 1 < 2'
    print("True loop")
    break

variable = 0
while True:
    # you can stop a program with cntrl+c
    print("variable is ", variable)
    variable = variable + 1
    if variable == 10:
        break

strings = ["Hello", "my", "name", "is", "Terry", "Davis"]
# A list of strings

for thing in strings: # A for loop works in an interesting way:
    # The for loop will execute once for each element in the list,
    # And "thing" will be that element!
    print(thing)

for character in strings[0]:
    # the for loop breaks up strings and lists both!
    print(character)

# I can next for loops too!
for thing in strings:
    print(thing)
    for character in thing:
        print(character, "in", thing)

class genericMonster:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self,HP,damageDie,damageBonus,name="generic monster"):
        self.maxHP = HP
        self.curHP = HP
        self.damageDie = damageDie
        self.damageBonus = damageBonus
        self.alive = True
        self.name = name
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
    def hit(self): # dealing damage
        damage = self.damageBonus + self.damageDie.roll()
        return damage
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True

zombieDie = Die(6)

zombie = genericMonster(22,zombieDie,1,"zombie") # Both are valid
zombie = genericMonster(22,Die(6),1,"zombie") # Overwrite with the other valid way xd

zombie.show()

skeleton = genericMonster(15,Die(6),2,"Skeleton")

skeleton.show()

def fight(monster1,monster2,suspense = False):
    if not monster1.alive or not monster2.alive:
        print("You forgot to refresh")
        return
    while True:
        if suspense:
            time.sleep(2)
        print(monster1.name,"vs",monster2.name)
        monster1.show()
        monster2.show()
        monster2.damage(monster1.hit())
        if not monster2.alive:
            break
        monster1.damage(monster2.hit())
        if not monster1.alive:
            break
    print()
    if monster1.alive:
        print("the victor is", monster1.name)
        monster1.show()
        return monster1.name
    else:
        print("the victor is", monster2.name)
        monster2.show()
        return monster2.name

skeletonwins = 0
for i in range(2): # Execute 4 times
    victor = fight(skeleton,zombie)
    if victor == "Skeleton":
        skeletonwins += 1
    skeleton.refresh()
    zombie.refresh()

print()
print(skeletonwins)

class Dice:
    def __init__(self,dieList):
        self.dice = dieList
        self.name = ""
        for die in dieList:
            self.name = die.name
        return
    def rollCall(self):
        for i in self.dice: # For each die
            print(i.name)
    def roll(self):
        result = 0
        for i in self.dice:
            result += i.roll()
        return result
    def loudRoll(self):
        result = 0
        for i in self.dice:
            result += i.loudRoll()
        print("group total:",result)
        return result

class Troll:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self):
        self.maxHP = 84
        self.curHP = 84
        self.damageDie = Dice([Die(6),Die(6),Die(6),Die(6)])
        self.damageBonus = 10
        self.alive = True
        self.name = "Troll"
        self.regenDie = Die(20)
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
    def regen(self):
        if self.alive:
            self.curHP += self.regenDie.roll()
            if self.curHP > self.maxHP:
                self.curHP = self.maxHP
    def hit(self): # dealing damage
        damage = self.damageBonus + self.damageDie.roll()
        self.regen() # This is exclusively so it fits in our fight function.
        return damage
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True

troll = Troll()
zombie = genericMonster(22*10,Die(6),1,"zombie") # Overwrite with the other valid way xd


fight(troll,zombie,suspense=True)
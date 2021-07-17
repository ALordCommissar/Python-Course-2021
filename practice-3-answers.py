# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:49:26 2021

@author: Donald Whitworth
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
# Practice set 3: advanced classes

# Practice problem 1:
# Go ahead and copy the code for the generic monster class that we made in class.

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


# Now initialize three zombies (health 22, damage 1+1d6)
# (Pst... if you can't run the code after just copying the zombie init code,
          # think about what class you might be missing in this file still)

zombie1 = genericMonster(22,Die(6),1,"zombie1")
zombie2 = genericMonster(22,Die(6),1,"zombie2")
zombie3 = genericMonster(22,Die(6),1,"zombie3")


# Now create an list called zombies that contains the three zombies you made.

zombies = [zombie1,zombie2,zombie3]

# Now use a for loop to iterate through the list
    # and print the stats of each zombie.

for zomb in zombies:
    zomb.refresh()
    zomb.show()

# Practice problem 2:
# Remember that "fight" function that we made earlier?
# We're going to make a similar function called "fightMany"
# It takes in two arguments:
    # The first is a single strong monster
    # The second is a list of many other monsters teaming up against it
# Remember that in order to make this function you'll have to have *all*
# of the other creatures act and do their damage each round.
# Write your function here:

def fightMany(strongMonster,Avengers):
    if not strongMonster.alive or not Avengers[-1].alive:
        print("Refresh needed")
        return
    while True:
        print()
        print(strongMonster.name,"vs monster team")
        strongMonster.show()
        for monster in Avengers:
            monster.show()
            if monster.alive == True:
                strongMonster.damage(monster.hit())
            else:
                continue
        if not strongMonster.alive:
            break
        for monster in Avengers:
            if monster.curHP > 0:
                monster.damage(strongMonster.hit())
                break
            elif monster.curHP == 0:
                continue
        if not Avengers[-1].alive:
            break
    print()
    if strongMonster.alive:
        print("the victor is", strongMonster.name)
        strongMonster.show()
        return strongMonster.name
    else:
        print("the victor is monster team")
        for monster in Avengers:
            monster.show()
        return
            
        
            
        
troll = Troll()
troll.refresh()
fightMany(troll,zombies)
    
# Do some experimentation now & run the code as needed to check:
    # How many zombies does it take to beat a troll?
        # Trolls have 84 HP and do 28 damage.
    # (yes, there is some randomness, but 3 is not enough.)


# Practice problem 3:
# Go back up to the generic monster class. Copy and paste it here.
# Change the class name to "rollingMonster".
# We need to add two data values:
    # Attack bonus (name it whatever you want)
    # Armor class (name it watever you want)
# Both of these data values will need to be passed as
        # arguments to the class in __init__()

# You should *also* make a new method called "attack."
# This method will simply roll a d20 and add the monster's attack bonus.
# Write the class here

class rollingMonster:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self,HP,damageDie,damageBonus,armorClass,attBonus,name="generic monster"):
        self.maxHP = HP
        self.curHP = HP
        self.damageDie = damageDie
        self.damageBonus = damageBonus
        self.alive = True
        self.AC = armorClass
        self.attBonus = attBonus
        self.name = name
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
        print("Armor class",self.AC)
        print("Attack bonus +",self.attBonus)
    def attack(self):
        attDie = Die(20)
        attack = self.attBonus + attDie.roll()
        return attack
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

# Also, go ahead and initialize a rolling zombie:
    # HP 22
    # Damage 1+1d6
    # Attack bonus +3
    # Armor class 8
# And a rolling skelton:
    # HP 15
    # Damage 2+1d6
    # Attack bonus +4
    # Armor class 13

RollZombie = rollingMonster(22,Die(6),1,8,3,"Zombie")
RollSkeleton = rollingMonster(15,Die(6),2,13,4,"Skeleton")



# Practice problem 4:
# Remember that "fight" function that we made in class?
# We're going to make yet another similar function called "fightRoll"
# It takes the same structure of arguments that the one in class takes,
# Except these monsters must both be rolling monsters.
# This function will add the iconic step of D&D combat into the mix:
    # A monster will first roll.
    # If the monster's attack score is >= the opponent's Armor Class:
        # Then do damage
    # Otherwise
        # No damage is dealt.
    # Action passes to the other monster
    # Repeat until we have a winner
# Write that function here

def fightRoll(monster1,monster2,suspense=False):
    if not monster1.alive or not monster2.alive:
        print("You forgot to refresh")
        return
    while True:
        if suspense:
            time.sleep(2)
        print()
        print(monster1.name,"vs",monster2.name)
        monster1.show()
        monster2.show()
        attRoll1 = monster1.attack()
        if attRoll1 >= monster2.AC:
             monster2.damage(monster1.hit())
        else:
            continue
        if not monster2.alive:
            break
        attRoll2 = monster2.attack()
        if attRoll2 >= monster1.AC:
            monster1.damage(monster2.hit())
        else:
            continue
        if not monster1.alive:
            break
    print()
    if monster1.alive:
        print("the victor is",monster1.name)
        monster1.show()
        return monster1.name
    else:
        print("the victor is",monster2.name)
        monster2.show()
        return monster2.name

# Go ahead and fight a zombie and a skeleton again.
# Let the skeleton go first. Is it still a zombie win every time?


fightRoll(RollZombie,RollSkeleton,False)
RollZombie.refresh()
RollSkeleton.refresh()



# Practice problem 5:
# Let's bring it all together: make a function called "fightManyRoll"
# That allows a single rolling monster to fight many rolling monsters.
# Go ahead and make a "rollingTroll" monster too (AC of 15, +7 to hit)
# write it here and set a troll up in a fight with a bunch of zombies.
# How many zombies does it take to win now?

class rollingTroll:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self):
        self.maxHP = 84
        self.curHP = 84
        self.damageDie = Dice([Die(6),Die(6),Die(6),Die(6)])
        self.damageBonus = 10
        self.alive = True
        self.name = "Troll"
        self.regenDie = Die(20)
        self.AC = 15
        self.attBonus = 7
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
        print("Armor class",self.AC)
        print("Attack bonus +",self.attBonus)
    def regen(self):
        if self.alive:
            self.curHP += self.regenDie.roll()
            if self.curHP > self.maxHP:
                self.curHP = self.maxHP
    def attack(self):
        attDie = Die(20)
        attack = self.attBonus + attDie.roll()
        return attack
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
        
def fightManyRoll(strongMonster,Avengers):
    strongMonster.refresh()
    for monster in Avengers:
        monster.refresh()
    if not strongMonster.alive or not Avengers[-1].alive:
        print("Refresh needed")
        return
    while True:
        print()
        print(strongMonster.name,"vs monster team")
        strongMonster.show()
        for monster in Avengers:
            monster.show()
            if monster.alive == True:
                attRoll = monster.attack()
                if attRoll >= strongMonster.AC:
                    strongMonster.damage(monster.hit())
            else:
                continue
        if not strongMonster.alive:
            break
        for monster in Avengers:
            if monster.curHP > 0:
                strongAttRoll = strongMonster.attack()
                if strongAttRoll >= monster.AC:
                    monster.damage(strongMonster.hit())
                break
            elif monster.curHP == 0:
                continue
        if not Avengers[-1].alive:
            break
    print()
    if strongMonster.alive:
        print("the victor is", strongMonster.name)
        strongMonster.show()
        return strongMonster.name
    else:
        print("the victor is monster team")
        for monster in Avengers:
            monster.show()
        return
    
rollTroll = rollingTroll()
rollZombie1 = rollingMonster(22,Die(6),1,8,3,"Zombie 1")
rollZombie2 = rollingMonster(22,Die(6),1,8,3,"Zombie 2")
rollZombie3 = rollingMonster(22,Die(6),1,8,3,"Zombie 3")
rollZombie4 = rollingMonster(22,Die(6),1,8,3,"Zombie 4")
rollZombie5 = rollingMonster(22,Die(6),1,8,3,"Zombie 5")
rollingZombies = [rollZombie1,rollZombie2,rollZombie3,rollZombie4,rollZombie5]
fightManyRoll(rollTroll,rollingZombies)

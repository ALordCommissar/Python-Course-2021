# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:31:40 2021

@author: whitw
"""

import utils
import json
import math
import time



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
    monDamDie = utils.Die(damStr[3])
    
    monster = utils.rollingMonster(monsterHP,monDamDie,monDamBonus,monAttBonus,monAC,monName)
    return monster
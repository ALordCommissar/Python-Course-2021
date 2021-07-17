# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:18:32 2021

@author: whitw
"""

import utils
import json
import math
import time



def fightFinal(group1,group2,suspense = False,printing = True):
   for monster in group1:
        if not monster.alive:
            print("you forgot to resfresh")
            monster.show()
            return
   for monster in group2:
        if not monster.alive:
            print("you forgot to resfresh")
            monster.show()
            return
   
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
                    continue
                if not group2[tarIndex2].alive:
                    tarIndex2 += 1
                else:
                    continue
            except:
                tarIndex1 + 0
                tarIndex2 + 0
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
        return "group1"
   else:
        if printing:
            print("the victor is", "the second monster group")
            for monster in group2:
                monster.show()
            victor = "Second Monster Group"
        return "group2"
   fightFinalAppend = open("fightFinal.txt","a")
   fightFinalAppend.write("A fight has just occured\nThe winner is:",victor,"\n")
   numMonsters = 0
   monNames = []
   for monster in group1:
        numMonsters += 1
        monNames.append(monster.name)
   fightFinalAppend.write("The number of monsters in the first group is:",numMonsters,"\nMonsters in the group:",monNames,"\n")
   numMonsters = 0
   monNames = []
   for monster in group2:
        numMonsters += 1
        monNames.append(monster.name)
   fightFinalAppend.write("The number of monsters in the second group is:",numMonsters,"\nMonsters in the group:",monNames,"\n")
   if victor == "First Monster Group":
       group1HP = 0
       for monster in group1:
           monster.HP += group1HP
           fightFinalAppend.write("Total remaining HP:",group1HP)
   else:
        group2HP = 0
        for monster in group2:
            monster.HP += group2HP
            fightFinalAppend.write("Total remaining HP:",group2HP)
   fightFinalAppend.close()
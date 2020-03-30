"""
Created on Sat Mar 28 2020
Topic:- Polymorphism in python(Duck Typing)
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""

class pycharm:
    def execute(self):
        print("Compiling...")
        print("Running...")

class HPTECH:
    def execute(self):
        print("Spell check...")
        print("Convention check...")
        print("Compiling...")
        print("Running...")

class laptop:
    def code(self,ide):
        ide.execute()
        
ide = HPTECH()

lap = laptop()
lap.code(ide)
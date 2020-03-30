"""
Created on Sat Mar 28 2020
Topic:- Consturctor, Self and Comparing Objects
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""


class people:
    
    def __init__(self):
        self.name = "Harish"
        self.age =  "21"

    def compare(p1, p2):
        if p1.age == p2.age:
            return True
        else:
            return False
        
p1 = people()

print(p1.name, p1.age)

p2 = people()

p2.name = "Rachna"
p2.age = 20

print(p2.name, p2.age)

if p1.compare(p2):
    print("They are Same")
else:
    print("They are not same")
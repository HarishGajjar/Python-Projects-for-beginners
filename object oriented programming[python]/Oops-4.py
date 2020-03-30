"""
Created on Sat Mar 28 2020
Topic:- Types of method in python
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""
class student:
    
    school = "HPTECH"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2 +self.m3) / 3
    
    @classmethod
    def getschool (cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Python School!")
        
s1 = student(35,40,60)
s2 = student(80,95,70)

print(s1.avg(), s1.getschool())
print(s2.avg(),s2.getschool())
student.info()
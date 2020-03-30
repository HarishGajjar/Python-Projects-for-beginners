"""
Created on Sat Mar 28 2020
Topic:- Operator Overloading
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        sum = student(m1, m2)
        return sum
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

s1 = student(58,45)
s2 = student(60,75)

s3 = s1 + s2 
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("S1 Wins!")
else:
    print("S2 Wins")


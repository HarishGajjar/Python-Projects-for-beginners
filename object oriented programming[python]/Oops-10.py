"""
Created on Sat Mar 29 2020
Topic:- Method Overriding
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""
class student:
    
    def sum(self,a, b):
        s = a + b
        return s

s1 = student()
print(s1.sum(25,45))
"""
Created on Sat Mar 29 2020
Topic:- Method Overloading
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""

class A:
    def show(self):
        print("In Class A!")

class B(A):
    pass

a1 = B()
a1.show()
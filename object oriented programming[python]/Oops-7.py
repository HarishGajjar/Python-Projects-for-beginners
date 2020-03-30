
"""
Created on Sat Mar 28 2020
Topic:- Constructor in Inheritance & Method Resolution Error(MRO)
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""
class A:
    def __init__(self):
        print("In A Init")
        
    def feature1(self):
        print("Feature 1-A is Working...")

class B:
    def __init__(self):
        print("In B Init")
        
    def feature1(self):
        print("Feature 1-B is Working...")
        
class C(A):
    def __init__(self):
        super().__init__()
        print("In C Init")
                
  

c1 = C()
c1.feature1()

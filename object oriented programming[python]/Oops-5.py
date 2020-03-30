"""
Created on Sat Mar 28 2020
Topic:- Inner class in python
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""

class student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
    
    def show(self):
        print(self.name, self.rollno)
        
    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        
        def show (self):
            print(self.brand, self.cpu, self.ram)

s1 = student('Harish', 26)
s2 = student('Rachna', 52)

s1.show()
s1.lap.show()
print()
s2.show()
s2.lap.brand = "AMD"
s2.lap.cpu = "Ryzen 3"
s2.lap.show()

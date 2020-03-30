"""
Created on Sat Mar 28 2020
Topic:- __init__ Mthod in python
@author: HarishGajjar
Credit:- Telusko
original Source :- https://youtu.be/qiSCMNBIP2g
"""

class computer:
    
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        
    def config_message(self):
        print("Configuration of this computer is ",
              self.cpu, self.ram, self.storage)
        
        
comp1 = computer("Intel I3", "8GB",  "500GB")
comp2 = computer("Intel I5", "16GB", "1TB")
comp3 = computer("Ryzen 5", "8GB", "500GB")
comp4 = computer("Ryzen 7", "16GB", "1TB")

computer.config_message(comp1)
computer.config_message(comp2)
computer.config_message(comp3)
computer.config_message(comp4)


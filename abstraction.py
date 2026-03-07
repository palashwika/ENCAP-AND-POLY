#Import necessary Modules
from abc import ABC, abstractmethod

#Create a base class
class Absclass(ABC):

    #function to print a value
    def print(self,x):
        print("Passed value ", x)

    #abstract method
    def task(self):
        print("We are insixde Absclass task ")

#Create sub class; overrides abstract method
class test_class(Absclass):
    def task(self): #has same function as line 12
        print("We are inside test_class task")

#object creation
test_obj=test_class()
test_obj.task()
test_obj.print(100)

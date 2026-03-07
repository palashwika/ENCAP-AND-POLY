#import necessary packages
from abc import ABC, abstractmethod 
#create a base class
class Animal(ABC):

    #abstract method
    #should be implemented by all sub-classes
    def move(self):
        pass

#sub classes
class Human(Animal): 

    def move(self):  #same method used for sub classes
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

R=Human()
R.move()

R=Snake()
R.move()

R=Dog()
R.move()

R=Lion()
R.move()

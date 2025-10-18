"""
What is Class : A class is a blueprint for creating objects. It defines a set of attributes
and methods that the created objects will have. Classes allow for the encapsulation of data 
and functionality, promoting code reusability and organization in object-oriented programming.

What is object : An object is just a variable that contains data and has behavior associated with it.

"""


# Basic  class example

class Car:
    #attribbutes 
    def __init__(self,name,model,fuel_type,car_type):
        self.name=name
        self.model=model
        self.fuel_type=fuel_type      #self is like mediator variable that store attribute info of class and we can use these attributes later on same class using self
        self.car_type=car_type

        self.range="400km"


    def car_description(self):        # passing self parameters in essential that how we can access attributes that self have that we just defined in def __init__
        print(f"The {self.name} {self.model} is a {self.car_type} car and it go upto range of {self.range}")


object_or_instance = Car('Tesla',"Roadstar 2025",'Battery','Sports')    # so we create object/instance of the class by you know assiging call of that class to a variable

object_or_instance.car_description()

# also we can access and change attributes of class

print(object_or_instance.name,object_or_instance.model)

object_or_instance.name='BYD'

object_or_instance.car_description()
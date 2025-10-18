# Instance methods : its a normal object methods that we are defined so far , we can access it using object or self.

class Instance:
    def __init(self):
        self.name='Santosh'

    def instance_method(self):                # so this is intance method as we know it can
        pass                           #access the instance/self variables and methods



""" Class methods : It belongs to class not the instane or self

> so we can access class varaibles but not the self or instance variables

> where to use it ? ----> When need to call the method wihtout creating an object
>                   ----> Factory method to create new instance wihout calling the __init__ constructor

"""


class Person:
    species = "Homo sapiens"   #a class varaible 

    def __init__(self,age=24):
        self.name='Santosh'
        self.age=age

    @classmethod                   # a decorator that indicate or flag that this method is belong to a class method
    def get_species(cls):   # if we dont use this @classmethod then python treat this method as normal method
        print(cls.species)  # and it will give error when we call it using object beacuse we will not able to call it by class name

    @classmethod
    def create_new_objc(cls):
        return cls()




    def test_method():
        try:
            print('Test pass')
        except Exception as e:
            print('Got error : ',e) 



# calling class methods
Person.get_species()   

obj1 = Person(age=24.8)
obj1.get_species()

#calling a method witout self and any cls
Person.test_method()

# obj2 = Person(age=24.8)
# obj2.test_method()       # got error because calling through object automatically     
                    #input the self argument in method but while defining we gave it 0 parameters
                    #  so it require 0 parameters.




# factory methods to create new object without calling the __init__ constructor

new_obj = Person.create_new_objc()
print(new_obj.name)




# Static methods : They are helper methods that dosnt belongs to class or instance/self,
#                  so access data of class or instance varaible is not possible by static methods
#       gernaly we use static methods to create similar grouped methods like below


class MathsOperations:
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def Multiply(a,b):
        return a*b
    

print(MathsOperations.add(2,3), MathsOperations.Multiply(2,3))

obj3 = MathsOperations()
print(obj3.add(2,4))           

"""
So main is we didnt defined the __init__ constructor then how python created the object obj3 :
well when we dont define the __init__ constructor then python by defaut provide the __init__ without any instance variable or data
that how it created the obj3

"""



"""
| Feature               | Instance Method     | Class Method     | Static Method         |
| --------------------- | ------------------- | ---------------- | --------------------- |
| First parameter       | `self`              | `cls`            | None                  |
| Access instance data? | ✅ Yes               | ❌ No             | ❌ No                  |
| Access class data?    | ✅ Yes               | ✅ Yes            | ❌ No                  |
| Called on             | Object              | Class or Object  | Class or Object       |
| Use case              | Works with instance | Works with class | Utility/helper method |

"""


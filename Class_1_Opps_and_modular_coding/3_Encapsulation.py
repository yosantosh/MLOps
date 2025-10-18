# Some times developers need to hide attributes and methods of class so that can be achive by Encapsulaton.

class Encapsulation:
    def __init__(self):
        self.__hiddenA='This is hidden Attribute'    # used __ to hide attribute
        self.Name = 'Looka'

    def __hidenMethod(self):
        return "This is hiden method"
    

    def getter(self):                # also we can use any metod name here
        return self.__hiddenA
    
    def setter(self,value_to_set):
        self.__hiddenA = value_to_set
        pass
    

obj = Encapsulation()
# print(obj.__hiddenA)                       # error beacause python store hidden attribute with name like 
                                #_Encapsulation__hiddenA

print(obj._Encapsulation__hiddenA)
print(obj._Encapsulation__hidenMethod())     # same to access method
print(obj.getter())
obj.setter("New Setted value")
print(obj.getter())




"""
What is Inheritance : If you are defining a class which is related to other aleady defined class then 
you can inherit the constructor, variables and methods from other class into current class.

Both class should folow parent child behaviour and parent class must be inherit to child class


what  can be inherit : Constructor , non-private attributes and non private methods including : class variables too

what cant be inherit : private variables and methods starts with __

can child inherit in parents : NO


"""


# Basic inherit example

class Car:
    weels = 4
    def __init__(self,brand,model,made_in_year,weight):
        self.brand = brand
        self.model = model
        self.weight=weight
        self.made_in_year=made_in_year

    def car_name(self):
        print(f'{self.brand} {self.model} {self.made_in_year}')


    #child class

class EV_car(Car):
    fuel_type='Battery'    #class variable

    def car_name(self):   # method overriding : if we call EV_car.car_name() then it will call this new method not from parent class
        print(f'{self.brand} {self.model} {self.made_in_year} ---> fuel type : {EV_car.fuel_type}')
    



obj = EV_car('Tesla','Y','2025','1000kg')
obj.car_name()

"""
Automatic constructor __init__ calling from parent class :
We didnt defined constructor in EV_car class so python by default called the parent class constructor so 
we have all instance attributes.


so we can Acess both type of variabels class and instance too

"""

print(obj.weight, obj.weels)



class EV_car1(Car):
    fuel_type='Battery'  

    def __init__(self,brand,model,made_in_year,weight,Motor_Power,charging_port):
        self.brand = brand     # so here we defined the constructor so python will not call the default parent class constructor
        self.model = model
        self.weight=weight
        self.made_in_year=made_in_year
        self.Motor_Power=Motor_Power
        self.charging_port=charging_port

    def car_name(self):   
        print(f'{self.brand} {self.model} {self.made_in_year} ---> fuel type : {EV_car1.fuel_type}')

    

# The super() function is used to call the methods from parent class to within child class

class Ev_car2(Car):
    fuel_type='Battery'

    def __init__(self,brand,model,made_in_year,weight,Motor_Power,charging_port):
        super().__init__(brand,model,made_in_year,weight)        # calling parent class constructor 1st

        self.Motor_Power=Motor_Power
        self.charging_port=charging_port

        
    
    def car_name(self):
        return super().car_name()


obj4= Ev_car2('Tesla','Y',2025,'1000kg','120','ccsi')
obj4.car_name()







# ----------------------------------------------------------------------------------------------


# Types of Inheritance

# 1 ----> Single Inheritance : Single child class inherit from singel parent class as we saw it earlier


# 2 ----> Multiple Inheritance : Inherit multiple parents in child class

class Father:
    def skills(self):       # in absence of __init__ constructor python pass default __init__ constructor with self parameter only
        print('Programming and electric skills')

class Mother:
    def skills(self):
        print("Dancing, cooking and painting")

class Child(Father,Mother):
    def child_skills(self):
        print("coding and gaming")


obj5 = Child()
obj5.child_skills()
obj5.skills()         #python will call father skills method : MRO search method: 1st find in father then mother 




# 3 ------>   multi level inheritnace :  


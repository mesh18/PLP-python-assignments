#creating first class in object oriented programming
class car:
    color = "red"

    def drive(self):
        print("the car is driving")
    
my_car = car()
print(my_car.color)
my_car.drive()

# creating a constructor
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = student("alice",20 )
s2 = student("bob",22)

print(s1.name,s1.age)
print(s2.name,s2.age)

#creating constructors with default arguments
class employee:
    def __init__(self,name,position = "intern"):
        self.name = name
        self.position = position

e1 = employee("charlie")
e2 = employee("david","manager")

print(e1.name,e1.position)
print(e2.name,e2.position)
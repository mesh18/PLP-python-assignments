#basic oops principles
#EXAMPLE 1
#INHERITANCE
class vehicle:
    def __init__(self,wheels):
        self.wheels = wheels

#defining child classes
class car(vehicle):
    pass
class bike(vehicle):
    pass
#creating objects
my_car = car(4)
my_bike = bike(2)
#accessing attributes
print("car has",my_car.wheels,"wheels")
print("bike has",my_bike.wheels,"wheels")

#EXAMPLE 2
class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def display_info(self):
        print("Username:",self.username)
        print("Email:",self.email)

class admin(user):
    def __init__(self,username,email,admin_level):
        super().__init__(username,email)
        self.admin_level = admin_level

    def display_info(self):
        super().display_info()
        print("Admin Level:",self.admin_level)

#creating objects
normal_user = user("john_doe","john@example.com")
admin_user = admin("admin_user","admin@example.com",1)

#accessing methods
normal_user.display_info()
admin_user.display_info()
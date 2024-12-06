class SmartPhone:
    def __init__(self,OS,type,brand):
        self.OS = OS
        self.type = type
        self.brand = brand
    def call(self, num):
        print(f'Calling {num}');
    def message(self, msg, receiver):
        print(f"Sending! {msg} to {receiver}");

maxwells_phone = SmartPhone('IOS', 'iphone xr', 'Apple')

print(maxwells_phone.brand, maxwells_phone.type, maxwells_phone.OS)

maxwells_phone.call('09045678500');
maxwells_phone.message('Hello dear have you eaten', 'cynthia');   



class Iphone(SmartPhone):
    pass
xxMax = Iphone('ios', 'iphonexxMax', 'Apple')

print(xxMax.brand)


# question 2
# polymorphism

class Vehicle :
    def __init__(self, brand,type):
        self.brand = brand
        self.type = type;
    def move(self):
        print('move');

class Car(Vehicle) :
    def move(self):
        print('Drive');

class Boat(Vehicle) :
    def move(self):
        print('Sail');

stanley_car = Car('Mercedes', 'Gla 250');
print(stanley_car.brand, stanley_car.type);
stanley_car.move();

Geralds_boat = Boat('Touring', '568');
print(Geralds_boat.brand, Geralds_boat.type);
Geralds_boat.move();

# Encapsulation

class Student :
    def __init__(self, name, id, graduation_year):
        self.name = name;
        self.id = id;
        self.graduation_year = 2024;

student_x = Student('Malcom kenneth', '20424110DA', 2015);

print(student_x.name, student_x.id, student_x.graduation_year) # will be Malcom kenneth 20424110DA 2024 rather than 2015



        

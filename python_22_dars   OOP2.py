# class Student:
#     def __init__(self,name):
#         print("Inside construktor")
#         self.name=name
#         print("All variables initialized")
#
#
#     def show(self):
#         print(f" Hello my name is ",self.name)
#
# s1=Student("Aslddin")
# s1.show()
from Tools.scripts.dutree import display


# class Employee:
#     def display(self):
#         print("Inside display")
# emp=Employee()
# emp.display()



# class Company:
#     def __init__(self):
#         self.name="PYnative"
#         self.adress="AVS  street"
#     def show(self):
#         print("Name: ",self.name  , "Adress:",self.adress)
# cmp=Company()
# cmp.show()



# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
#     def show(self):
#         print(self.name,self.age,self.salary)
# emma=Employee("Emma",20,7333)
# emma.show()
#
# kelly=Employee("Kelly",23,57777)
# kelly.show()


#1-MASALA.1.
  # "Texnika" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
  #   info() - (brand, model, type) ni print qilib beradi.
  #
  # "Notebooks" child klassi bor. Unda konstruktirida qo'shimcha (video_card, ram, display).
  #   more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.
  #
  # "Televisions" child klassi bor. Unda konstruktirida (size, display) parametrlari bor.
  #   more_info() - (brand, model, type, size, display) ni print qilib beradi.
  #
  # "Smartphones" child klassi bor. Unda konstruktirida (size, sim_count) parametrlari bor.
  #   more_info() - (brand, model, type, size, sim_count) ni print qilib beradi.

#
# class Texnika:
#     def __init__(self,brand,model,type):
#         self.brand=brand
#         self.model=model
#         self.type=type
#
#     def info(self):
#         print(f" {self.brand},  {self.model},  {self.type}")
#
# class Notebooks(Texnika):
#     def __init__(self,brand,model,type,videocard,ram,display):
#         super().__init__(brand,model,type)
#         self.vodecard=videocard
#         self.ram=ram
#         self.display=display
#     def info1(self):
#         super().info()
#         print(f" {self.vodecard}   {self.ram}  ,  {self.display}")
# class  Televisions(Texnika):
#     def __init__(self,brand,model,type,size,display):
#         super().__init__(brand,model,type)
#         self.size=size
#         self.display=display
#     def info1(self):
#         super().info()
#         print(f" {self.size}  ,  {self.display}")
# class Smartphones(Texnika):
#     def __init__(self,brand,model,type,size,sim_count):
#         super().__init__(brand,model,type)
#         self.size=size
#         self.sim_count=sim_count
#
#     def info1(self):
#         print(f" {self.size} ,  {self.sim_count}")
#
#
#
# notebook=Notebooks("HP","Victus","Notebook","RTX-2050","8 GB","Full HD 15.6 ")
# notebook.info1()
#
# televezor=Televisions("Samsung","Samsung QN90C","Oled",55,"QLED")
# televezor.info1()
#
# telefon=Televisions("Iphone","Iphone 16 pro max","Pro",7,"LCD")
# telefon.info1()



#2. "Transport" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
  #   info() - (brand, model, type) ni print qilib beradi.
  #
  # "ElentroCars" - child klassi bor. Unda konstruktirida qo'shimcha (battery_life, chargin_time).
  #   more_info() - (brand, model, type, battery_life, chargin_time) ni print qilib beradi.
  #
  # "SportCars" - child klassi bor. Unda konstruktirida qo'shimcha (motor, color).
  #   more_info() - (brand, model, type, motor, color) ni print qilib beradi.
  #
  # "Truck" - child klassi bor. Unda konstruktirida qo'shimcha (motor, height, long, wieght).
  #   more_info() - (brand, model, type, height, long, wieght) ni print qilib beradi.

# class Transport:
#     def __init__(self,brand,model,type):
#         self.brand=brand
#         self.model=model
#         self.type=type
#     def info(self):
#         print(f"{self.brand} , {self.model} , {self.type}")
# class ElektroCars(Transport):
#     def __init__(self,brand,model,type,battery_life,chargin_time):
#         super().__init__(brand,model,type)
#         self.battery_life=battery_life
#         self.chargin_time=chargin_time
#     def info1(self):
#         super().info()
#         print(f" {self.battery_life} , {self.chargin_time}")
# class Sportcars(Transport):
#     def __init__(self,brand,model,type,motor,color):
#         super().__init__(brand,model,type)
#         self.motor=motor
#         self.color=color
#     def info1(self):
#         super().info()
#         print(f" {self.motor} {self.color}")
# class Truck(Transport):
#     def __init__(self,brand,model,type,height,long,wieght):
#         super().__init__(brand,model,type)
#
#         self.height=height
#         self.long=long
#         self.wieght=wieght
#     def info1(self):
#         super().info()
#         print(f" {self.height} , {self.long},{self.wieght}")
#
# elektromobile=ElektroCars("Tesla","Model 3","Sedan","348 miles (560 km)","15-30 min (Supercharger to 80%)")
# elektromobile.info1()
#
# sportcar=Sportcars("Bugatti","Bugatti Chiron","Coupe	","W16 Quad-turbo (1,479 hp)","Blue, Black, White, Gold")
# sportcar.info1()
#
# yuk_moshina=Truck("Toyota","Tacoma	","Mid-size Pickup	","70 in (1.78 m)","212 in (5.38 m)","5,600 lbs (2,540 kg)")
# yuk_moshina.info1()




#3-MASALA."University" - parent klass. Konstruktorida esa (university) parametrlari bor.
  #   info() - (university) ni print qilib beradi.
  #
  # "Staff" - child klass. Unda konstruktirida qo'shimcha (first_name, last_name, age) parametrlari bor.
  #   staff_info() - (university, first_name, last_name, age) ni print qilib beradi.
  #
  # "Student" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (group) parametrlari bor.
  #   more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.
  #
  # "Teacher" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
  #   more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.
  #
  # "OtherStaff" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position) parametrlari bor.
  #   more_info() - (university, first_name, last_name, position,) ni print qilib beradi.

#
class University:
    def __init__(self,university):
        self.university=university
    def info(self):
        print(f"University: {self.university}")
class Staff(University):
    def __init__(self,university,first_name,last_name,age):
        super().__init__(university)
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def info1(self):
        super().info()
        print(f"University: {self.university}, First name  :{self.first_name} ,Last name: {self.last_name} ,Age: {self.age})")
class Student(Staff):
    def __init__(self,university,first_name,lastname,age,group):
        super().__init__(university, first_name, lastname, age)
        self.group=group

    def  info1(self):
        super().info()
        print(f" University: {self.university} , First name :{self.first_name} ,Last name: {self.last_name} ,Age: {self.age}, Group :{self.group}")

class  Teacher(Staff):
    def __init__(self,university,first_name,last_name,age,position, subject):
        super().__init__(university,first_name,last_name,age)
        self.position=position
        self.subject=subject

    def info1(self):
        super().info()
        print(f" University: {self.university},First name: {self.first_name}, Last name: {self.last_name} Age: {self.age} Position: {self.position} ,Subject: {self.subject}")

class OtherStaff(Staff):
    def __init__(self,university,first_name,last_name,position):
        super().__init__(university,first_name,last_name,position)
        self.position=position

    def info1(self):
        super().info()
        print(f"University: {self.university},First name: {self.first_name}, Last name: {self.last_name} ,Position: {self.position}")

university_name="TerDu"

staff1=Staff("TerDu","Asliddin","Norqobilov",20)
staff1.info1()

student1=Student(university_name,"Asliddin","Norqobilov","20","KI -123")
student1.info1()

teacher1=Teacher(university_name,"Alouddin","Nasriddinov",35,"Phd","Progammer AI")
teacher1.info1()

otherstaff1=OtherStaff(university_name,"Ozodbek","Ziyodullayev" ,"student")
otherstaff1.info1()



#3.2..."Object" - child klass. U "University" dan vorislik oladi. Unda konstruktirida qo'shimcha (name) parametrlari bor.
  #   object_info() - (university, name) ni print qilib beradi.
  #
  # "Computer" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
  #   object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.
  #
  # "Mebel" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
  #   object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi.


class Object(University):
    def __init__(self,university,name):
        super().__init__(university)
        self.name=name

    def info1(self):
        super().info()
        print(f" University: {self.university} , Obyekt nomi: {self.name}")
class Computer(Object):
    def __init__(self,university,name,soni,tizimi,holati):
        super().__init__(university,name)
        self.soni=soni
        self.tizimi=tizimi
        self.holati=holati
    def info1(self):
        print(f"University: {self.university},Obyekt nomi: {self.name} Soni : {self.soni}, Tizimi: {self.tizimi},Holati: {self.holati}")
class Mebel(Object):
    def __init__(self,university,name,soni,turi,holati):
        super().__init__(university,name)
        self.soni=soni
        self.turi=turi
        self.holati=holati
    def info1(self):
        print(f" University : {self.university}, Obyrkt nomi {self.name} , Soni : {self.soni},Turi: {self.turi}, Holati : {self.holati}")

obyekt1=Object(university_name,"Universitet")
obyekt1.info1()


kompyuter1=Computer(university_name,"Kompyuter",200,"Windows-11","yaxshi")
kompyuter1.info1()

mebel=Mebel(university_name,"Shkaf",100,"Kitob javoni","yaxshi")
mebel.info1()
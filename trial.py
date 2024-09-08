#Super
'''
in pyhton supe function us sued to refer to the parent class or siperclass.
it allows you to call methods defined in the superclass from the subclass
enabling you to extend and customize the functionality inherited from the parent class.


'''
class Emp:
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        # self.name = "Nairobi"
        self.Add = Add

class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id,name,Add)
        self.Emails = Emails

Emp_1 = Freelance(103, "wdaefwfw", "Nodia", "afbwef@gmail.com")
print(f'My id is {Emp_1.id}')
print(f'The name is {Emp_1.name}')
print(f'The Address is {Emp_1.Add}')
print(f'The email is {Emp_1.Emails}')

# what is the super () method used for ?
'''
a method in the parent class can be called in python usign the super() function
It is typical practice in object orinted programming. to call the methods of the superclass and
enable method overrding and inheritance.

Benefits of super functions.
1. need not remeber or specify the parent class name to access its methods.
This function can be used both in single and multiple inheritances.
2. This implements modulairty and code resuasability as there is no need to re write the entire function
3. the super function in python is called 
'''

'''
Understanding python super() with __init__() methods.
the __init__() method in programming is reffered to as a constructor
when this method is called it allows the class to initialize the attributes of the class.
in an inherited subclass, a parent class can be reffered to with the ise of the super() fucntion.
THE super function return a temporary object of the superclass that allows access to all of its chils access.


SUPER FUNCTIONS WITH SINGLE INHERITANCE.

'''
class Animals:
    def __init__(self):
        self.legs = 4
        self.tail= True
        self.domestic = True
        self.mammals = True
    
    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")

class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()

class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailAndLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")

Tom = Dogs()
print(Tom.isMammal())
Jack = Horses()
print(Jack.hasTailAndLegs())

# Super with multiples inheritances.
'''
what is a super()__init__() is used to call the __init__()method of the superclass in a derived class.
this is neccessaru when you want to ensire that the initialization ocde in the base class is executed before 
executing any in the derived class.
'''
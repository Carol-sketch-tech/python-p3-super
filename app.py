'''
super reduces repeatition of code and enhance using inheritance.
use super to call methods on a parent class from the chils class.

Student inherits from class user we can choose to either allow the student class to inherit 
a certain method from user or overwrite that methos with another implementation that is specific to student.
'''
'''
what if there is a method in the parent class that we want our child 
to share some of the functionality of?
or what if we want our child class to inherit a methos from the parent and then augment it in some way?
we can achieve this with the use of the super keyword.
'''

# Using super to superchange inheritance.
'''
say we are creating an education app in which users are either students or teachers.
we have parent, User class that both our student and Teacher classes inherits from.

our user class has a method , log_in() that sets an instance varibale self.logged_in equal to True.
'''

class User:
    def __init__(self,name):
        self.name = name 
        print(self.name)
        # self.name = "Someone else"
        print(self.name)

    def log_in(self):
        self.logged_in = True
        print("the first log_in() details are displayed.")

class Student(User):#augmenting or superchange the log_in() method inside of the student class.
    def __init__(self, name, grade):
       print("User.__init__ called.")
       super().__init__(name)
       self.grade = grade

    def nameMy(self,name):
        print(f"{name} will report back to school tomorrow and make something out of my last year there.")
        # Super lets us to do just that. we can all super with an argumnet from the Student.__init__ method, whch will call the User.__init__ method with that argument.w
    def log_in(self):            # we have redefined the log_in() mehtod and tell it to inherit any functionality of the log_in method defined in the parent or superclass which is the user.
        super().log_in()     #in the log_in() method above the super keyword will call on the log_in() method as defined in the superclass.
        self.in_class = True       # from the output displayed in the terminal, log_in() on a student instance the super keyword calls the specified method in the parent class, adding the functionality of the original method to your new method in a single line
        print("the second log_in() details are displayed.")


caroline = Student("Mark",50)
print(caroline.nameMy)


wanjiru = Student("Wanjiru", 22)

'''
when a student logs into our app we need to not only set their logged in attribute to attribute to True, we need
to set their "in class" attribute to True as well.
'''

# Calling Super with Arguments.
'''
While we can stll create new students with our updated class defination its nor particularly DRY.
notht he student and User classes define a name instance varibale and set it when the class is instatiated.

Super lets us to just that. we can call super with an argument from the Student.__init__ method whic will call the User.__init__ method with the argument.
'''
# Just like in the previous example, super is used to call a method on the superclass from the subclass- the only differnvce is that this time we are passing in
# arguments that are required by the method defined in the superclass.
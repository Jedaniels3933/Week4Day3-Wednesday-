#
#

# Inheritance : When a class inherits the properties and methods of another class- Extends a parent class with additional functionality and charastics through subclasses that inherit from it.
###   Inheritance : When a class inherits the properties and methods of another class- Extends a parent class with additional functionality and charastics through subclasses that inherit from it. Once a class is created, it can be used as a base for other classes. The new class is called a child class , and the class that it inherits from is called a superclass.

#Polymorphism : When objects from diff classes respond similarly to the same method in their own unique way
# zeros on on more specific functionality
#Can have objects from different classes (subclasses ) responding similarity to the same methos on their own unique way
# When a subclass provides a specific implementation that's already defined in the parent( Super class)

# Parent Class - Superclass

class User():
    def __init__(self, email, password , username):
        self.email = email
        self._password = password
        self.username = username

# All methods are inherited by the subclass (child class)
    def user_info(self):
        print(f"User: {self.username} can be contacted at {self.email}")

    # Setter
    def set_password(self, new_pass):
        self._password = new_pass

    #Getter for username

    def get_username(self):
        print(self.username)

    # Create an ADMIN 
    #Class that inherits from the User (parent class)
    class Admin(User):   #Class Admin inherits from User class

     def __init__(self, email, _password, username, admin_id, isadmin = True):
        super().__init__(email, _password, username)# What to inherit - do not have the repeat everything 
        self.admin_id = admin_id
        self.isadmin = isadmin
    
    def user_info(self):
        print(f"Admin : {self.admin_id} {self.username} can get support at {self.email}")
    
    def get_password(self):
        print(self._password)
    
    def admin_info(self):# Instantiate a user class object
        billy_bob = User('billy@email.com', '1234', 'billy-b')
        billy_bob.user_info()

      # instantiate an Admin class object
    travis = Admin('traviscpeck@codingtemple.com','1234', 'Travicci', 1)
    travis.user_info()

    billy_bob.get_username()
    billy_bob.set_password("this is the new password")

    travis.get_username()

    travis.set_password('123456789')
    

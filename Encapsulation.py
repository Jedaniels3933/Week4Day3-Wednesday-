# Encapsulation : When you restrict access to some of the objects components.   Bundling data and methods within a class , controlling access to them

# 3 ways to Encapsulate : Public, private, and protected attributetes- Dunder __ 
        ## Public : Accessible from anywhere, both inside and outside the class they are defined in
        ## Private : (__) Accessible only within the class they are defined in: (__private): ONly assessable within the calss its defined - useful for securing a hiding data structure
        ## Protected( _ ) : Accessible only within the class they are defined in and its subclasses: (_protected): Only assessable within the class its defined and its subclasses
            ###Accesable in both the class its defined in as well as any of its subclasses

class Smartphone():

    def __init__(self, model, credit_card, operating_system):
        self.model = model # public attribute
        self.__wallet = credit_card # private attribute, only accessible within this class
        self._operating_system = operating_system # protected attribute, accessible within this class and any subclasses

    def get_info(self):
        print(f"Model: {self.model}")
        print(f"Wallet: ****-****-****-{self.__wallet[-4:]}")
        print(f"OS: {self._operating_system}")
    
    def get_wallet(self): # need a 'getter' in order to decide how a user can access and view the __wallet. this information is completely under our controll
        return self.__wallet
    
    def set_wallet(self, new_card): # creating a 'setter' to controll how my __wallet information is altered
        flag = False
        for i in new_card:
            if i.isdigit():
                flag = True
                continue
            else:
                flag = False
                print("Please enter a valid card number ( no dashes or spaces)")
                break
        if flag:
            self.__wallet = new_card
            print("Card number updatedto: {new_card[-4:]}")

iphone = Smartphone("iPhone XS", '1111-1111-2222-0000', 'iOS 13')

# print(iphone.__wallet) # this will throw an error because __wallet is private and not accessible from outside the class
#  Getters and Setters

#Getters: Meth used to access any attribute including (private and protected) since cant get otherwise from outside the class 
print(iphone.get_wallet())
iphone.__wallet = '12345678' # We can't do this because __wallet is private and not accessible from here, only within the class itself
print(iphone.get_wallet()) #__wallet remains unchanged
iphone.get_info()

#Setters = Meth used to set any attriburtes ( including (private and protected))
iphone.set_wallet('4321123478907654')








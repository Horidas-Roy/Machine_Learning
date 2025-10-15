class MobilePhone:
    def __init__(self,model,battery = 100):
        self.model = model
        self.__battery = battery
    
    def use(self):
        self.__battery -= 1
    
    def charge(self):
        if self.__battery < 100:
            self.__battery += 1
        else:
            print("Battay is Full...!")
    def get_battery(self):
        return self.__battery
    
myPhone = MobilePhone("Nokia 1200") 

myPhone.use()
myPhone.use()
myPhone.charge()
print(myPhone.get_battery())
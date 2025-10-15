class Phone:
    def __init__(self,model,battery=100):
        self.model = model
        self.battery = battery
    
class SmartPhone(Phone):
    def __init__(self,model,battery,operatingSystem):
        self.operatingSystem = operatingSystem
        super().__init__(model,battery)

class GamingPhone(SmartPhone):
    def __init__(self,model,battery,operatingSystem,coolingSystem):
        self.coolingSystem = coolingSystem
        super().__init__(model,battery,operatingSystem)

    def startGame(self,name):
        print(f"Playing {name} on {self.model}")

gamingPhone = GamingPhone("Redmi - 1208","4000mA","Android","Air cooling")

gamingPhone.startGame("Ludo")
print(gamingPhone.battery)
print(gamingPhone.operatingSystem)
print(gamingPhone.coolingSystem)
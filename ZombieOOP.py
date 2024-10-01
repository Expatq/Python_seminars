class Monster:
    def __init__(self, name:str, destruct:int):
        self.name = name
        self.power = destruct
        print(f"The monster {self.name} the {self.__class__.__name__} was created")

    def growl(self, s:str):
        print(f"{s} growled {self.name} the {self.__class__.__name__}")

    def attack(self):
        print(f"The monster {self.name} the {self.__class__.__name__} attacked with force {self.power}")


class Zombie(Monster):
    def __init__(self, name:str, destruct=5):
        super().__init__(name, destruct)
        
    def growl(self, up = False):
        s = "Raaaauuughhhh" if not up else "Raaaauuughhhh".upper()
        super().growl(s)

    def attack(self):
        super().attack()
        self.growl()

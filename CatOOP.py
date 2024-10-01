class AbstractCat:
    def __init__(self, weight=0):
        self.w = weight

    def eat(self, food:int):
        self.w += food // 10

        if self.w > 100:
            self.w = 100

        return self

    def get_weight(self):
        return self.w

    def __str__(self):
        return f"{self.__class__.__name__} ({self.w})"



class HomeCat(AbstractCat):
    def __init__(self, weight=0, name=''):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return "meow"

    def get_name(self):
        return self.name

    def sleep(self):
        return "Snore"*(self.w // 5)



class MouseCatcher(HomeCat):
    def meow(self):
        return super().meow().upper()

    def catch_mice(self):
        return "Got it!"

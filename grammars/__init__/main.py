class Player:
    def __init__(self, name, xp):
        self.name = name
        self.xp = xp

    def say_hello(self):
        print("hello I'm", self.name, self.xp)

    def just_hi(self):
        print(f"hi, I'm {self.name}")


kim = Player("kim", 100)
print(kim.name, kim.xp)
kim.say_hello()
kim.just_hi()

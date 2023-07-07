class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello I'm", self.name)

    def just_hi(self):
        print(f"hi, I'm {self.name}")


class Player(Human):
    def __init__(self, name, xp):
        self.xp = xp


class Fan(Human):
    def __init__(self, name, fan_name):
        self.fan_name = fan_name


kPlayer = Player("kim", 1000)
kPlayer.say_hello()
nico_fan = Fan("nico_fan", dontknow)
nico_fan.say_hello()

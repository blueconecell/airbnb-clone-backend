class Human:
    def __init__(self, name):
        print("initailize now!")
        self.name = name

    def say_hello(self):
        print("hello I'm", self.name)

    def just_hi(self):
        print(f"hi, I'm {self.name}")


class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp


class Fan(Human):
    def __init__(self, name, fan_name):
        super().__init__(name)
        self.fan_name = fan_name


kPlayer = Player("kim", 1000)
kPlayer.say_hello()
nico_fan = Fan("nico_fan", "dontknow")
nico_fan.say_hello()


##########################################


class Dog:
    def woof(self):
        print("woof! woof")


class Beagle(Dog):
    def jump(self):
        print("jump")

    # 메소드 오버라이딩
    def woof(self):
        # super().woof()
        print("super woof!")


b = Beagle()
b.woof()

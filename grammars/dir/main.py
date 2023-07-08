class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(super().__str__())
        return f"Dog : {self.name}"

    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "😥"

    # __str__()은 메모리 주소값을 반환하여 준다.
    # 오버라이딩하여 메모리주소가 아니라 이모지를 반환하게 바꾼 것이댜.


jia = Dog("jia")
# print(jia)
print(jia.name)
# print(dir(jia))
paul = Dog("paul")
print(paul)

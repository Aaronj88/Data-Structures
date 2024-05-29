class Animal:
    pet_name = "something"  #<-- hidden var
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def breath(self):
        print(self.name, "is breathing")
        print(self.pet_name)

    def sleep(self):
        print(self.name, "is sleeping")

    def eat(self):
        print(self.name, "is breathing")


class Dog(Animal):

    def __init__(self, breed, color, name, age, weight):
        super().__init__(name, age, weight)
        self.breed = breed
        self.color = color

    def bark(self):
        print(self.name, "is barking")

    def walk(self):
        print(self.name, "is walking")
        print(self.pet_name)


Dog1 = Dog("Husky", "White and Black", "Milo", 2, 24)
Dog1.breath()
Dog1.bark()








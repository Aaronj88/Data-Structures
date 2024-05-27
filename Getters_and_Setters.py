class Human:
    def __init__(self,age,height,name,weight = 1):
        self.age = age
        self.height = height
        self.name = name
        self.weight = weight

    def breath(self):
        print(self.name," is breathing.")

    def get_height(self):
        return self.height
    
    def set_height(self,height):
        self.height = height


p1 = Human(13,"6 feet","Aaron",40)

print(p1.get_height())
p1.set_height("15000 feet")
print(p1.get_height())



#UPLOAD TO GITHUB





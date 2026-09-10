class Animal: 
  def __init__(self,name):
    self.name = name
  def makeSound(self):
    print("Sounddddddddddddd")

class Cat(Animal):
  def __init__(self, name,breed):
    super().__init__(name)
    self.breed = breed

myCat = Cat("Yellow Cat","Grass Cat")
myCat.makeSound()
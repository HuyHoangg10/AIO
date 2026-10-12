from abc import ABC,abstractmethod

class Shape(ABC):
  @abstractmethod
  def compute_area():
   pass

class Square(Shape):
   def __init__(self,side):
     super().__init__()
     self.side = side
    
   def compute_area(self):
     return self.side **2
   
my_square = Square(4)
print(my_square.compute_area())
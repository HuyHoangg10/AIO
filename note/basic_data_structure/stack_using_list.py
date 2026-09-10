# stack : LIFO 
# LAST IN FIRST OUT 

class Stack:
  def __init__(self,capacity):
    self.__data = []
    self.capacity = capacity
  def describe(self):
    print(self.__data)
  def add(self,item):
    self.__data.append(item)
  def remove(self):
    self.__data.pop()

stack = Stack(5)
stack.add(1)
stack.add(1)
stack.add(1)
stack.add(2)
print("Stack before remove")
stack.describe()
print("Stack after remove")
stack.remove()
stack.describe()
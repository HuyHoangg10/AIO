class ID:
  def __init__(self,number):
    self.number = number
  def show_info(self):
    return f"{self.number}"

class Student:
  def __init__(self,name,id):
    self.name = name
    self.id = id

id = ID("SV001")
print(vars(id))

student = Student("Hoang",id.show_info())
print(vars(student))
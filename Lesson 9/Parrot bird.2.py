class parrot:

   def __init__(self, name, age):
    self.name = name
    self.age = age
   def sings(self, song):
    return "{} sings {}" .format(self.name, song)
   def dance(self):
    return "{} is now dancing" .format(self.name) 
Blu = parrot("Blu", 15)
print(Blu.sings ("Happy"))
print(Blu.dance())   
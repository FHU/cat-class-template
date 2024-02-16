#Revmoe pass and complete the cat class
class Cat():
    def __init__(self, name='unknown', age=0):
        self.name = name
        self.age = age
    def speak(self):
        return "Meow"

stella = Cat()
stella.name = 'Stella' 
stella.age = 7
garfield = Cat()
garfield.name = 'Garfield'  
garfield.age = 50

print(garfield.speak())
print(stella.speak())


#Create objects here
#These should NOT be indented inside the class


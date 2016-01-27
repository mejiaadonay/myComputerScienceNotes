
# Inheritance
# Author:   Jose Escobar Mejia
# Date:     01/27/2016

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
    
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    
jose_escobar = Parent("Escobar", "brown")
#print(jose_escobar.last_name)
jose_escobar.show_info()

#adonay_mejia = Child("Mejia", "brown", 5)
#print(adonay_mejia.last_name)
#print(adonay_mejia.number_of_toys)

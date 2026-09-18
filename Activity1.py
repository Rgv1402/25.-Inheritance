class Family_Member:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Colour: ", self.eye_color)
        print("Height (in cm): ", self.height_cm)

class Kid(Family_Member):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)
    def show_traits(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().show_traits()
    def fav_hobby(self, hobby):
        self.hobby = hobby
        print(self.name,"'s Favourite hobby is", hobby)

child = Kid("Maya", 10, "brown", 128)
child.show_traits()
child.fav_hobby("painting")

print("\nIs child subclass of Family member? ", issubclass(Kid, Family_Member))
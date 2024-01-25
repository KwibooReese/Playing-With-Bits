class animal():
    
    def __init__(self, animal):
        
        self.animal_dict = {
            "human":1,
            "dog":3,
            "cat":5,
            "dinosaur":9
        }
        self.all_permissions = {
            "speak":1,
            "woof":2,
            "meow":4,
            "roar":8
        }
        self.animal = animal
        self.permissions = self.animal_dict[self.animal]   

    def user_has_permissions(self, permission_to_look_for):
        return (self.permissions & permission_to_look_for) > 0

    def speak(self, string):
        if not self.user_has_permissions(self.all_permissions["speak"]) > 0:
            print("You do not have permission to speak")
        else:
            print(string)

    def woof(self):
        if not self.user_has_permissions(self.all_permissions["woof"]) > 0:
            print("You are not a dog")
        else:
            print("WOOF WOOF WOOF WOOF")

    def meow(self):
        if not self.user_has_permissions(self.all_permissions["meow"]) > 0:
            print("You are not a cat")
        else:
            print("meow!")

    def roar(self):
        if not self.user_has_permissions(self.all_permissions["roar"]) > 0:
            print("You are not a dinosaur")
        else:
            print("roar!!!!!!!!!!!!!")

speaking_animal = animal("human")
speaking_animal.meow()

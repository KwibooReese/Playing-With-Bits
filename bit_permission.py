user_permissions = 8

all_permissions = {
    "speak":1,
    "woof":2,
    "meow":4,
    "roar":8
}

def speak(string):
        if not user_has_permissions(all_permissions["speak"]) > 0:
            print("You do not have permission to speak")
        else:
            print(string)

def user_has_permissions(permission_to_look_for):
     return (user_permissions & permission_to_look_for) == 1

speak("hello")
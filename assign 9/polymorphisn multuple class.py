class dog:
    def sound(self):
        print ("barks")
class cat:
    def sound(self):
        print ("meow")
class cow:
    def sound(self):
        print("moo")
def make_sound(animal):
    animal.sound()
dogs=dog()
cats=cat()
cows=cow()

make_sound(dogs)
make_sound(cats)
make_sound(cows)

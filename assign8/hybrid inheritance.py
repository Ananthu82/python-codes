class animal:
    def sound(self):
        print("sound")
class bird (animal):
    def sound(self):
        print("bird sound")
class mammal(animal):
    def sound(self):
        print("mammal sound")
class bat(bird,mammal):
    def sound(self):
        print("bat sound")
        bird.sound(self)
        mammal.sound(self)

bat1=bat()
bat1.sound()
    
class animal:
    def speak(self):
        print("the animal makes a sound")
    
class dog(animal):
    def speak(self):
        super().speak()
        print("the dog barks")
animal=animal()
dog=dog()
dog.speak()


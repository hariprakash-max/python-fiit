# method overriding
class bear(object):
    def sound(self):
         print("groarr")
class dog(object):
    def sound(self):
        print("woof woof!")
def makesound(animaltype):
    animaltype.sound()
bearobj=bear()
dogobj=dog()
makesound(bearobj)
makesound(dogobj)

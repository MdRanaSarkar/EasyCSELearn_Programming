class Parrot:
    def fly(self):
        return "Parrot Can Fly"
    def swim(self):
        return "Parrot Cannot Swim"
    
class Penguin:
    def fly(self):
        return "Penguin Can't Fly"
    def swim(self):
        return "Penguin Can Swim"
    
def flying_test(bird):
    print(bird.fly())
    
    
pp = Parrot()

pen = Penguin()

flying_test(pp)
flying_test(pen)

class Goblin(object):
    def __init__(self):
        self.name = "Goblin"
        self.health = 60
        self.power1 = 5
        self.power2 = 10
        self.power3 = 15
        self.attack1 = "Bite"
        self.attack2 = "Scratch"
        self.attack3 = "Double Scratch"
        
    def is_alive(self):
        return self.health > 0

class Vampire(object):
    def __init__(self):
        self.name = "Vampire"
        self.health = 100
        self.power1 = 5
        self.power2 = 10
        self.power3 = 15
        self.attack1 = "Bite"
        self.attack2 = "scratch"
        self.attack3 = "Suck blood"

    def is_alive(self):
        return self.health > 0

        
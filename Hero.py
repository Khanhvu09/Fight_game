class Hero(object):
    def __init__(self):
        self.health = 100
        self.power1 = 10
        self.power2 = 20
        self.power3 = 35
        self.power4 = 55
        self.power5 = 80
        self.gold = 200

    def is_alive(self):
        return self.health > 0

    def not_out_of_gold(self):
        return self.gold > 0
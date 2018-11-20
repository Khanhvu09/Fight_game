import random
class Main(object):
    def __init__(self, health, power1, power2, power3, gold):
        self.health = health
        self.power1 = power1
        self.power2 = power2
        self.power3 = power3
        self.gold = gold

hero1 = Main(100, 20, 30, 40, 20)
goblin = Main(100, 5, 15, 30, 0)

while hero1.health > 0 and goblin.health > 0:
    print """
    You have %d health. 
    The goblin has %d health.
    What do you want to do?
    1. Attack 
    2. Heal
    3. Shop 
    4. flee""" % (hero1.health, goblin.health)

    user_input = raw_input("> ")

    if user_input == "1":
        i = raw_input ("""
    Choose attack: 
    1. Superman Punch
    2. Sword Slash
    3. Epic Attack
        """)
        i = str(i)
        choice = 0
        for choice in i:
            if choice == "1":
                goblin.health -= hero1.power1
                print "You have done %d damage to the goblin" % hero1.power1
            elif choice == "2":
                goblin.health -= hero1.power2
                print "You have done %d damage to the goblin!" % hero1.power2
            elif choice == "3":
                print " You have done %d damage to the goblin!" % hero1.power3
                goblin.health -= hero1.power3

    #============================
    #========In-game store=======
    #============================
    while user_input == "3":
        print """
    1. 20 Heal Potion (10 gold)
    2. 50 heal potion (25 gold)
    3. 80 heal potion (50 gold)
    4. Exit
        """
        option = raw_input("> ")
        if option == "1":
            if hero1.gold >= 20:
                hero1.gold -= 10
                hero1.health += 20
                print "You have used 10 gold. You now have %d gold left." % hero1.gold
                print "Your health is now %d." % hero1.health 
            else:
                print "You do not have enough gold."
        if option == "2":
            if hero1.gold >= 25:
                hero1.gold -= 25
                hero1.health += 50
                print "You have used 25 gold. You now have %d gold left." % hero1.gold
                print "Your health is now %d" % hero1.health 
            else:
                print "You do not have enough gold."
        if option == "3":
            if hero1.gold >= 50:
                hero.gold -= 50
                hero1.health += 80
                print "You have used 50 gold. You now have %d gold left." % hero1.gold
                print "Your health is now %d" % hero1.health
            else:
                "You do not have enough gold."
        if option == "4":
            break  
    #===========================        

    if goblin.health <= 0: 
        hero1.gold += 20
        print "You gained 20 gold. You now have %d gold" % hero1.gold
    
    


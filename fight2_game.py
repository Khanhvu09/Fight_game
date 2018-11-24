import os
from Hero import Hero
import Monster
from random import randint
    # from gold import Gold

os.system('clear')
gameOn = True

while gameOn:
        #=======================
        #======== Banner =======
        #=======================

    text = "Tower of Vengeance"
    textLength = len(text)
    w = 4
    h = 3
    print ("*" * textLength + "*" * w)
    for x in range(h - 2):
        print ("* " + text + " *")
    print ("*" * textLength + "*" * w)

        #====================================
        #======== Hit Enter to begin ========
        #====================================

    raw_input("""
Get ready for Tower 1!

Hit Enter to begin
""")

    os.system('clear')

    hero = Hero()
    tower = 1
    gold = 0


    while hero.is_alive() and gameOn == True:
        if hero.gold <= 0:
            print """
Game Over.
You ran out of gold. 
Next time use your gold more wisely."""
            start_over = raw_input("Would you like to play again (Y or N)? ")
            start_over = start_over.upper()
            if start_over == "Y":
                gameOn = False
                gameOn = True
                hero.gold = 200 
                hero.health = 100
                tower = 1
            else:
                print "Thank you for playing"
                gameOn = False

        #===========================================
        #======== Iterating through monster ========
        #===========================================

        monsters = []
        for monsters in range(1,3):
            tower += 1
            if monsters == 1:
                monster = Monster.Goblin()
                gold = 20
            elif monsters == 2:
                monster = Monster.Vampire()
                gold = 40
            gameOn = True
            while (hero.is_alive() and hero.not_out_of_gold() and monster.is_alive()) and gameOn:
                print """
You have %d health. 
The %s has %d health.
What do you want to do?
1. Attack 
2. Heal (You will lose a turn to attack)
3. flee
""" % (hero.health, monster.name, monster.health)
                user_input = raw_input("> ")

                os.system('clear')
        #===========================    
        #======== 1. Attack ========
        #===========================

                if user_input == "1":
                    attack = True
                    while (attack):

                        print ("""
Your health: %d
%s health: %d
Choose attack: (You have %d gold)
1. Superman Punch (10 damage) (10 gold)
2. Sword Slash (20 damage) (20 gold)
3. Epic Attack (35 damage) (40 gold)
4. Shinryuken (55 damage) (70 gold)
5. Demon Armageddon (80 damage) (100 gold)
""") % (hero.health, monster.name, monster.health, hero.gold)
            
                        option = raw_input("> ")

                        if option == "1":
                            if hero.gold >= 10:
                                monster.health -= hero.power1
                                hero.gold -= 10
                                os.system('clear')
                                print """
You have dealt %d damage to the %s
""" % (hero.power1, monster.name)
                                attack = False
                            else:
                                os.system('clear')
                                print "Not enough gold"
                        elif option == "2":
                            if hero.gold >= 20:
                                monster.health -= hero.power2
                                hero.gold -= 20
                                os.system('clear')
                                print """
You have dealt %d damage to the %s!
""" % (hero.power2, monster.name)
                                attack = False
                            else:
                                os.system('clear')
                                print "Not enough gold"
                        elif option == "3":
                            if hero.gold >= 40:
                                monster.health -= hero.power3
                                hero.gold -= 40
                                os.system('clear')
                                print """
You have dealt %d damage to the %s!
""" % (hero.power3, monster.name)
                                attack = False
                            else:
                                os.system('clear')
                                print "Not enough gold"
                        elif option == "4":
                            if hero.gold >= 70:
                                monster.health -= hero.power4
                                hero.gold -= 70
                                os.system('clear')
                                print """
You have dealt %d damage to the %s!
""" % (hero.power4, monster.name)
                                attack = False
                            else:
                                os.system('clear')
                                print "Not enough gold"
                        elif option == "5":
                            if hero.gold >= 100:
                                monster.health -= hero.power5
                                hero.gold -= 100
                                os.system('clear')
                                print """
You have dealt %d damage to the %s!
""" % (hero.power5, monster.name)
                                attack = False
                            else:
                                os.system('clear')
                                print "Not enough gold"
        #=========================
        #======== 2. Heal ========
        #=========================

                elif user_input == "2":
                    shop = True
                    while (shop):
                        print """
Choose Heal Potion: (You have %d gold)
1. 20 Heal Potion (20 gold)
2. 50 Heal potion (50 gold)
3. 80 Heal potion (80 gold)
4. Exit
""" % hero.gold
                        option = raw_input("> ")
                        if option == "1":
                            if hero.gold >= 20:
                                hero.gold -= 20
                                hero.health += 20
                                print "You have used 10 gold. You now have %d gold left." % hero.gold
                                print "Your health is now %d." % hero.health 
                                shop = False
                            else:
                                print "You do not have enough gold."
                        elif option == "2":
                            if hero.gold >= 50:
                                hero.gold -= 50
                                hero.health += 50
                                print "You have used 25 gold. You now have %d gold left." % hero.gold
                                print "Your health is now %d" % hero.health 
                                shop = False
                            else:
                                print "You do not have enough gold."
                        elif option == "3":
                            if hero.gold >= 80:
                                hero.gold -= 80
                                hero.health += 80
                                print "You have used 50 gold. You now have %d gold left." % hero.gold
                                print "Your health is now %d" % hero.health
                                shop = False
                            else:
                                print "You do not have enough gold."
                        elif option == "4":
                            shop = False

        #===================================
        #======== When monster dies ========
        #===================================
                while monster.health <= 0:
                    if monster.health <= 0 and monsters == 2:
                        print """
You have defeated the final boss!"""
                        break
                    else:
                        hero.gold += gold
                        print "%s has been killed!!\n" % monster.name
                        print "You gained %d gold. You now have %d gold\n" % (gold, hero.gold)
                        print ("Get ready for Tower %i !!!\n") % tower
                        raw_input("Hit enter to continue")
                        os.system('clear')
                        break
                        
                if user_input == "3":
                    print "Thank you for playing"
                    gameOn = False
            if user_input == "3":
                break

        #===============================
        #======= Monster Attacks =======
        #===============================

                if monster.health > 0:
                    attack = randint(1,3)
                    if attack == 1:
                        hero.health -= monster.power1
                        print "The %s used %s for %d damage" % (monster.name, monster.attack1, monster.power1)
                    if attack == 2:
                        hero.health -= monster.power2
                        print "The %s used %s for %d damage" % (monster.name, monster.attack2, monster.power2)
                    if attack == 3:
                        hero.health -= monster.power3
                        print "The %s used %s for %d damage" % (monster.name, monster.attack3, monster.power3)
                    if hero.health <= 0:
                        print "Thou hast been slain."
        #==============================
        #======= When hero dies =======
        #==============================
                if hero.health <= 0:
                    print "Game Over"
                    break

        #===========================================
        #======= Choosing not to play anymore ======
        #===========================================
            if monster.health <= 0 and monsters == 2:
                gameOn = False

    #========================================
    #======== Choosing to play again ========
    #========================================
        if user_input == "3":
                break
    if user_input == "3":
        break

    raw_input("Hit enter to continue")
    start_over = raw_input("Would you like to play again (Y or N)? ")
    start_over = start_over.upper()
    if start_over == "Y":
        hero.gold = 200 
        hero.health = 100
        tower = 1
        gameOn = True
    else:
        print "Thank you for playing"
                
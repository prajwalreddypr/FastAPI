#acceptance criteria

# enemies can fight each other
# different  types of ennemies
# each player has diff powers, health points and attach damage
#all implemented using oops

# #player
# 1. Name/ Type
# 2.Health points
# 3. Attack damage

from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

#multiple objects of enemy
# zombie = Zombie( 15, 3)
# ogre = Ogre(20, 4)
# big_zombie = Enemy("Big Zombie", 30, 5)
# zombie.__type_of_enemy = 'Ogre'
# print(zombie.get_type_of_enemy())

# def battle(e1: Enemy, e2: Enemy):
#     e1.talk()
#     e2.talk()
    
#     while e1.health_points > 0 and e2.health_points > 0:
#       print("--------------")
#       e1.special_attack()
#       e2.special_attack()
      
#       print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left.")
#       print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left.")
      
#       e2.attack()
#       e1.health_points -= e2.attack_damage
#       e1.attack()
#       e2.health_points -= e1.attack_damage
      
#       print("------------------")
      
      
#       if e1.health_points > 0:
#           print(f"{e1.get_type_of_enemy()} wins !")
#       else:
#           print(f"{e2.get_type_of_enemy()} wins !") 
          
# zombie = Zombie(10, 1)
# ogre = Ogre(20, 3) 

# battle(zombie, ogre)


def hero_battle(hero: Hero, enemy: Enemy):
    
    while hero.health_points > 0 and enemy.health_points > 0:
        
        print("--------------")
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        
        hero.attack()
        enemy.health_points -= hero.attack_damage
        
        print("--------------")
        
        if hero.health_points > 0:
            print("Hero wins")
        else:
            print("ENemy wins")

zombie = Zombie(10, 1)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)
        
    
    
    
    
    
    
    
    

# battle(zombie)
# battle(ogre)

# print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}")

# print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}")

# zombie.talk()
# ogre.talk()



# print(f"{zombie.type_of_enemy} has {zombie.health_points} health points and  with an attak damage of {zombie.attack_damage}")


# zombie.talk()
# zombie.reply()
# zombie.walk_forward()
# zombie.attack()
# print(big_zombie.attack_damage)




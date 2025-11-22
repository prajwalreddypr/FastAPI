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

#multiple objects of enemy
zombie = Zombie( 15, 3)
ogre = Ogre(20, 4)
# big_zombie = Enemy("Big Zombie", 30, 5)
# zombie.__type_of_enemy = 'Ogre'
# print(zombie.get_type_of_enemy())


print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}")

print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}")

zombie.talk()
ogre.talk()



# print(f"{zombie.type_of_enemy} has {zombie.health_points} health points and  with an attak damage of {zombie.attack_damage}")


# zombie.talk()
# zombie.reply()
# zombie.walk_forward()
# zombie.attack()
# print(big_zombie.attack_damage)



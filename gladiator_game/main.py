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


#multiple objects of enemy
zombie = Enemy('Zombie', 15, 3)
big_zombie = Enemy("Big Zombie", 30, 5)


print(f"{zombie.type_of_enemy} has {zombie.health_points} health points and  with an attak damage of {zombie.attack_damage}")

# zombie.talk()
# zombie.reply()
# zombie.walk_forward()
# zombie.attack()
print(big_zombie.attack_damage)



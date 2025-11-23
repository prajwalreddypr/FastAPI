from Enemy import *
import random

# Child class Ogre
class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
          super().__init__(type_of_enemy = "Ogre", health_points = health_points, attack_damage = attack_damage)
    
    def talk(self):
        print("Ogre is slamming hands all around")
        #method overrriding. overrides the talk function from Enemy.
        
    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre attack has increase by 4.")
    
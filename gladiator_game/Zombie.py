from Enemy import *

# Child Class zombie
class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy = 'Zombie', health_points = health_points, attack_damage=attack_damage)
        
    def talk(self):
        print("Grumbling") #method override. overrides talk from parent
        
    def spread_disease(self):
        print("The zombie is trying to spread infection")
        #zombie only method
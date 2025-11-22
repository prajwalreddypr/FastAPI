class Enemy:
    
    type_of_enemy: str 
    health_points: int = 10
    attack_damage: int = 1
    
    #default/empty constructor
    def __init__(self):
        pass
    
    #no argument constructor
    def __init__(self):
        print("New enemy has been created with no starting values")
        
    #Parameter constructor
    
    def __init__(self, type_of_enemy, health_points =10, attack_damage = 1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    
    
    def talk(self):
        print(f"I amm a {self.type_of_enemy}. Be prepared to fight.")
        
    def reply(self):
        print("This is my responding")
        
    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")
    
    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")
    
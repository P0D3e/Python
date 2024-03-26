class Pokemon:
    def __init__(self, name : str, element : str, attack : int, defence : int, health : float):
        self.name = name
        self.type = element
        self.attack = attack
        self.defence = defence
        self.health = health



def __str__(self):
    return f"{self.name} {self.type}"


Bulbasaur = Pokemon("bulbasaur", "grass", 92, 92, 200)
Charmander = Pokemon("charmander", "fire", 98, 81, 188)
Squirtle = Pokemon("squirtle", "water", 90, 121, 198)
Pikachu = Pokemon("pikachu", "electric", 103, 76, 180)


name = input("Input the name of the pokemon : ")

def calculate_damage(attack_type, defence_type, attack, defence):

    if element == "fire" and element2 == "grass":
        attack = attack * 2
    if element == "fire" and element2 == "water":
        attack = attack * 0.5
    if element == "fire" and element2 == "electric":
        attack = attack * 1
    if element == "water" and element2 == "grass":
        attack = attack * 0.5
    if element == "water" and element2 == "electric":
        attack = attack * 0.5
    if element == "grass" and element == "electric":
        attack = attack * 1
    if element == element2:
        attack = attack * 1

    return 50 * (attack/defence)

print(Pokemon, element)

print(calculate_damage)
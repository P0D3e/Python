"""
fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric

> 2x
= 1x
< 0.5x
"""

type1 = input("Input your type of Pokemon")
type2 = input("Input the enemys Pokemon type")
atk = input("Input your Pokemons attack points")
deff = input("Input the enemys defend points")

def calculate_damage(atk_type, def_type, atk, deff):

    if type1 == "fire" and type2 == "grass":
        atk = atk * 2
    if type1 == "fire" and type2 == "water":
        atk = atk * 0.5
    if type1 == "fire" and type2 == "electric":
        atk = atk * 1
    if type1 == "water" and type2 == "grass":
        atk = atk * 0.5
    if type1 == "water" and type2 == "electric":
        atk = atk * 0.5
    if type1 == "grass" and type2 == "electric":
        atk = atk * 1
    if type1 == type2:
        atk = atk * 1

    return 50 * (atk/deff)

print(calculate_damage("fire", "electric", 40, 20))

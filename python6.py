"""
#
# Part: Functions
# 
"""
def myFullname(firstname="Unknown", lastname="Forger"):
    FullName = firstname + " " + lastname
    return FullName

print(myFullname("loid","forger"))
print(myFullname("Anya","forger"))
print(myFullname("Yor","forger"))
print(myFullname("Bond","forger"))

def redpotion(hp):
    hp += 50
    return hp

current_hp = 100
print("Current HP:", current_hp)
current_hp = redpotion(current_hp)
print("After using red potion, HP:", current_hp)

    
#ported from Femtoms ruby p1 sim
from random import random, randint
from math import floor

'''for melee damage the cap is 10, and for range and mage (no dawnbringer) the cap is 3.
From there, the damage is calculated by rolling two numbers, one between 0 and 10(inclusive) and another one between 0
and the weapon's max hit. The actual hit is whichever of these two are the lowest.
This will happen three times for the scythe,so total damage is
accuracy * min(randint(0, 10), randint(0, max)) +
accuracy * min(randint(0, 10), randint(0, max//2)) +
accuracy * min(randint(0, 10), randint(0, max//4)).
The dawnbringer (as far as we can tell) calculates its damage from this function : ((magic level * %dmg gear) / 6 ) - 1. This attack is 100% accurate -- gear discord'''
 
verzik_hp = 1750 # four man verzik hp
iterations = 1

# Weapons
scythe = {"accuracy": .9612, "max_hit": 48, "cap": 10}
dragon_claws = {"accuracy": .9482, "max_hit": 43, "cap": 10}
sang_staff = {"accuracy": .9289, "max_hit": 29, "cap": 3}
# Dawnbringer is a special case
dawnbringer = "dawnbringer"


def calculate_attack(weapon):
  # Dawnbringer spec
  if weapon == "dawnbringer":
    return randint(75, 150)

  # Any other weapon runs this code
  elif weapon["accuracy"] > random():
    return min(randint(0, weapon["cap"]), randint(0, weapon["max_hit"]))
  # else keyword not actually needed, but makes code more readable
  else:
    return 0


#calculates total damage of one scythe hit(3 splats) 
def calculate_scythe_attack():
  scythe_original_max = scythe["max_hit"]
  scythe_damage = 0
  scythe_damage += calculate_attack(scythe)
  #floor() drops decimal as osrs attacks are rounded down.
  # Note the use of calculate_attack's max hit override for 2nd and 3rd scythe hits.
  scythe["max_hit"] = floor(scythe["max_hit"] / 2)
  scythe_damage += floor(calculate_attack(scythe))

  scythe["max_hit"] = floor(scythe["max_hit"] / 2)
  scythe_damage += floor(calculate_attack(scythe))

  scythe["max_hit"] = scythe_original_max
  return scythe_damage
 
#calculates total damage from inputted attacks from spec chart for 1 iteration 
def simulator(dawnbringers, scythes, claws, tridents): 
    total_damage = 0

    for i in range(dawnbringers):
        total_damage += calculate_attack(dawnbringer)
    for j in range(scythes):
        total_damage += calculate_scythe_attack()
    for k in range(claws):
        total_damage += calculate_attack(dragon_claws)
    for l in range(tridents):
        total_damage += calculate_attack(sang_staff)
    return total_damage
 
#runs number of iterations requested and increases death counter if verzik dies. Prints % and number of deaths

def simulate(dawnbringers, scythes, claws, tridents):
  verzik_deaths = 0
  total_damage = 0
  # Loops one per iteration.
  for i in range(iterations):
    iteration_damage = simulator(dawnbringers, scythes, claws, tridents)
    total_damage += iteration_damage
    if iteration_damage >= verzik_hp:
      verzik_deaths += 1
  # Percentage chance Verzik dies given the inputs
  percentage = verzik_deaths * 100 / iterations
  # Main terminal output. I think you can make this look better with a multiline comment.
  print(f"The chance of killing Verzik over {iterations} iterations with... \n\nDawnbringer Specs: {str(dawnbringers)} \nScythe Hits: {str(scythes)} \nClaw Hits: {str(claws)} \nTrident Hits: {str(tridents)} \n\n...is {percentage}%.")


# Dawnbringers, Scythes, Claws, Tridents (sangs)
# Could easily add a func that asks for user input?
simulate(0, 150, 0, 0)


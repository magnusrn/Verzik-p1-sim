#ported from Femtoms ruby p1 sim
from random import random, randint
from math import floor
from inputs import iterations_per_increment as iterations
 
verzik_hp = 1750 # four man verzik hp

# Weapons
scythe = {"accuracy": .9612, "max_hit": 48, "cap": 10}
dragon_claws = {"accuracy": .9482, "max_hit": 43, "cap": 10}
sang_staff = {"accuracy": .9289, "max_hit": 29, "cap": 3}
blade = {"accuracy": .9371, "max_hit": 31, "cap": 10}
# Dawnbringer is a special case
dawnbringer = "dawnbringer"

# Calculates one hitsplat of a weapon. calculate_scythe_attack() uses this 3 times.
def calculate_hit(weapon):
  # Dawnbringer spec
  if weapon == "dawnbringer":
    return randint(75, 150)

  elif weapon["accuracy"] > random():
    return min(randint(0, weapon["cap"]), randint(0, weapon["max_hit"]))

  else:
    return 0


# Calculates total damage of one scythe hit (3 splats) 
def calculate_scythe_hit():
  # Stores scythe max hit
  scythe_original_max = scythe["max_hit"]
  scythe_damage_counter = 0

  scythe_damage_counter += calculate_hit(scythe)
  #floor() drops decimal as osrs attacks are rounded down.
  # Note the use of calculate_attack's max hit override for 2nd and 3rd scythe hits.
  scythe["max_hit"] = floor(scythe["max_hit"] / 2)
  scythe_damage_counter += floor(calculate_hit(scythe))

  scythe["max_hit"] = floor(scythe["max_hit"] / 2)
  scythe_damage_counter += floor(calculate_hit(scythe))
  # Resets scythe max hit
  scythe["max_hit"] = scythe_original_max
  return scythe_damage_counter
 

# Wondering if we can consolidate the below 3 funcs into one single func?

# Calculates total damage from inputted attacks from spec chart for 1 iteration. 
def simulator(dawnbringers, scythes, claws, tridents, blades): 
    total_damage = 0
    for i in range(dawnbringers):
        total_damage += calculate_hit(dawnbringer)
    for j in range(scythes):
        total_damage += calculate_scythe_hit()
    for k in range(claws):
        total_damage += calculate_hit(dragon_claws)
    for l in range(tridents):
        total_damage += calculate_hit(sang_staff)   
    for m in range(blades):
        total_damage += calculate_hit(blade)
    return total_damage
 
# Runs number of iterations requested and increases death counter if verzik dies. Prints % and number of deaths
def simulate(dawnbringers, scythes, claws, tridents, blades):
  # Init vars
  verzik_deaths = 0
  total_damage = 0
  # Loops once per iteration.
  for i in range(iterations):
    iteration_damage = simulator(dawnbringers, scythes, claws, tridents, blades)
    total_damage += iteration_damage
    if iteration_damage >= verzik_hp:
      verzik_deaths += 1
  # Percentage chance Verzik dies given the inputs
  percentage = verzik_deaths * 100 / iterations
  # Main terminal output. I think you could make this look better with a multiline comment.
  #print(f"The chance of killing Verzik over {iterations} iterations with... \n\nDawnbringer Specs: {str(dawnbringers)} \nScythe Hits: {str(scythes)} \nClaw Hits: {str(claws)} \nTrident Hits: {str(tridents)} \nBlade Hits: {str(blades)} \n\n...is {percentage}%.")
  return percentage

# EXPORTED AND USED IN MAIN.PY
def execute_simulation(dict_of_attacks):
  # Unpacks dictionary
  dawnbringers = dict_of_attacks.get("D", 0)
  scythes = dict_of_attacks.get("S", 0)
  claws = dict_of_attacks.get("C", 0)
  tridents = dict_of_attacks.get("T", 0)
  blades = dict_of_attacks.get("B", 0)
  # Calls simulator
  return simulate(dawnbringers, scythes, claws, tridents, blades)



# Needs dictionary_maker
# Imported from list_maker
def final_simulator(all_attack_dictionaries):
  # Error handling
  if len(all_attack_dictionaries) == 0:
    print("Tick increment cannot be greater than the total number of ticks selected!\nReduce the tick increment of select more ticks.")
    return
  for i in range(len(all_attack_dictionaries)):
    percentage = execute_simulation(all_attack_dictionaries[i])
    time_in_seconds = round((all_attack_dictionaries[i]['tick'] + 4) * 0.6, 1) # 3 ticks extra added
    print(f"{percentage}% chance of killing by tick {all_attack_dictionaries[i]['tick'] + 1}. ({time_in_seconds}s approx)")


#D = dawnbringer
#S = scythe
#T = trident
#B = swift blade
#C = claw scratch

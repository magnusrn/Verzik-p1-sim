#ported from Femtoms ruby p1 sim
from random import random, randint
from math import floor

#D = dawnbringer
#S = scythe
#T = sang_staff
#B = swift blade
#C = claw scratch 

# Weapons
scythe = {"accuracy": .9612, "max_hit": 48, "cap": 10}
dragon_claws = {"accuracy": .9482, "max_hit": 43, "cap": 10}
sang_staff = {"accuracy": .9289, "max_hit": 29, "cap": 3}
swift_blade = {"accuracy": .9371, "max_hit": 31, "cap": 10}
# Dawnbringer is a special case
dawnbringer = "dawnbringer"


# Calculates ONE hitsplat of a weapon.
def calculate_hit(weapon):
  # Dawnbringer spec
  if weapon == "dawnbringer":
    return randint(75, 150)
  # Every other weapon
  elif weapon["accuracy"] > random():
    return min(randint(0, weapon["cap"]), randint(0, weapon["max_hit"]))
  else:
    return 0


# Calculates total damage of one scythe hit (3 hitsplats) 
def calculate_scythe_hit():
  # Stores scythe max hit as it changes during this function
  scythe_original_max = scythe["max_hit"]
  scythe_damage_counter = 0
  # Hitsplat 1
  scythe_damage_counter += calculate_hit(scythe)
  # Hitsplat 2
  scythe["max_hit"] = floor(scythe["max_hit"] / 2)
  scythe_damage_counter += floor(calculate_hit(scythe))
  # Hitsplat 3
  scythe["max_hit"] = floor(scythe["max_hit"] / 2)
  scythe_damage_counter += floor(calculate_hit(scythe))
  # Resets scythe max hit to it's original value
  scythe["max_hit"] = scythe_original_max
  return scythe_damage_counter
 

# Simulates a P1 based on a dictionary of attacks and number of iterations given. Returns a percentage chance of killing Verzik.
def simulate(dict_of_attacks, iterations = 1000, verzik_hp = 1500):
  # Unpacks dictionary
  dawnbringers = dict_of_attacks.get("D", 0)
  scythes = dict_of_attacks.get("S", 0)
  claws = dict_of_attacks.get("C", 0)
  tridents = dict_of_attacks.get("T", 0)
  blades = dict_of_attacks.get("B", 0)

  # Init vars
  verzik_deaths = 0

  # Loops once per iteration.
  for i in range(iterations):
    iteration_damage = 0
    for i in range(dawnbringers):
        iteration_damage += calculate_hit(dawnbringer)
    for j in range(scythes):
        iteration_damage += calculate_scythe_hit()
    for k in range(claws):
        iteration_damage += calculate_hit(dragon_claws)
    for l in range(tridents):
        iteration_damage += calculate_hit(sang_staff)   
    for m in range(blades):
        iteration_damage += calculate_hit(swift_blade)
    if iteration_damage >= verzik_hp:
      verzik_deaths += 1

  # Percentage chance Verzik dies given the inputs
  percentage = verzik_deaths * 100 / iterations
  return percentage


# Used for optimisation in simulate_all()
def max_possible_damage(attack_dict):
    max_scythe_damage = attack_dict.get("S", 0) * scythe["cap"]
    max_claw_damage = attack_dict.get("C", 0) * dragon_claws["cap"]
    max_dawn_damage = attack_dict.get("D", 0) * 150
    max_blade_damage = attack_dict.get("B", 0) * swift_blade["cap"]
    max_sang_damage = attack_dict.get("T", 0) * sang_staff["cap"]

    max_damage = max_scythe_damage + max_claw_damage + max_dawn_damage + max_blade_damage + max_sang_damage
    return max_damage


# Returns correct Verzik hp
def get_verzik_hp(total_players):
  if (total_players == 4):
    return 1750
  elif (total_players == 5):
    return 2000
  else:
    return 1500


# MAIN FUNC AND MAIN OUTPUT
def simulate_all(all_attack_dictionaries, iterations, tick_increment, debug_mode = False):
  # Init vars
  num_of_attack_dictionaries = len(all_attack_dictionaries)
  total_players = all_attack_dictionaries[0]["players"]
  verzik_hp = get_verzik_hp(total_players)

  # Debugging
  if (debug_mode):
    print(f"Verzik Hitpoints: {verzik_hp}")
    print(f"Iterations Per Simulation: {iterations}")
    print(f"Total Attack Dictionaries: {num_of_attack_dictionaries}")
    print(f"Total Simulations Prior To Optimizations: {iterations * num_of_attack_dictionaries}")
    print("\n")

  # Used in optimisation checks
  prev_dict = {}
  prev_percentage = 0.0

  # Main Simulator Loop
  for i in range(num_of_attack_dictionaries):
    # Init loop vars
    current_dict = all_attack_dictionaries[i]
    time_in_seconds = round((current_dict['tick'] + 4) * 0.6, 1)

    # Skips sim if max possible damage from an attack dict is less than verzik's hp.
    if max_possible_damage(current_dict) < verzik_hp:
      print(f"Impossible to kill Verzik by tick {current_dict['tick'] + 1}.")

    # Skips sim if there was no change in attacks from the previous dictionary.
    elif (current_dict.get("_", 0) == prev_dict.get("_", 0) + tick_increment * total_players):
      print(f"{prev_percentage}% chance of killing by tick {current_dict['tick'] + 1}. ({time_in_seconds}s approx) (SKIPPED)")

    # Otherwise perform simulation
    else:
      percentage = simulate(current_dict, iterations, verzik_hp)
      # 3 ticks extra added to bring in line with some client timers
      print(f"{percentage}% chance of killing by tick {current_dict['tick'] + 1}. ({time_in_seconds}s approx)")
      prev_percentage = percentage

    prev_dict = current_dict
from collections import Counter

# MAIN FUNC (only func lol)
# Returns a list of dictionaries of all accumulated attacks from all players depending on the given tick increment. If no tick increment provided it defaults to 1.
def dictionary_maker(list_of_players, tick_increment, debug_mode = False):
  # Init vars
  all_attack_dictionaries = []
  final_dict_accumulator = Counter()
  
  # Finds number of players and total ticks.
  num_of_players = len(list_of_players)
  print(f"Number of Players: {num_of_players}")

  total_ticks = len(list_of_players[0])
  # Debugging
  if (debug_mode):
    print(f"Total Ticks: {total_ticks}")
    print(f"Tick Increment: {tick_increment}")
    print("\n")

  # Loops over ticks increasing by increment each time.
  for tick in range(tick_increment - 1, total_ticks, tick_increment):
    dict_accumulator = Counter()
    # Loops over number of players
    for player in range(0, num_of_players):
    
      dict_accumulator = dict_accumulator + Counter(list_of_players[player][:tick + 1])

      # range() will skip the last few ticks if it's tick increment goes above the total number of ticks. EG, trying to get the dictionaries for 12 ticks at an interval of 5 ticks will result in only 2 dictionaries being created because 5 + 5 = 10, and another 5 is 15 which is above the total ticks (12). The if statements here are used to collect any remaining ticks and their attacks, creating a special final dictionary and appending it to the list.
      if tick + 1 + tick_increment > total_ticks and tick_increment != 1:
          final_dict_accumulator = final_dict_accumulator + Counter(list_of_players[player][0:])
    dict_accumulator["players"] = num_of_players
    dict_accumulator["tick"] = tick + 1
    all_attack_dictionaries.append(dict_accumulator)
    # Debugging
    if (debug_mode):
      print(f"Tick {tick + 1} Dictionary: " + str(dict_accumulator))

    if tick + 1 + tick_increment > total_ticks and total_ticks % tick_increment != 0:
      final_dict_accumulator["players"] = num_of_players
      final_dict_accumulator["tick"] = total_ticks
      all_attack_dictionaries.append(final_dict_accumulator)
      # Debugging
      if (debug_mode):
        print(f"Tick {total_ticks} Dictionary: " + str(final_dict_accumulator))

  print("\n")
  return all_attack_dictionaries, total_ticks
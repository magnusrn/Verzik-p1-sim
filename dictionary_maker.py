from collections import Counter
# needs list_of_players and tick_increment


# Returns a list of dictionaries of all accumulated attacks from all players depending on the given tick increment. If no tick increment provided it defaults to 1.
def dictionary_maker(list_of_players, tick_increment = 1):
  # Uses the length of the first player list to find out the total number of ticks
  total_ticks = len(list_of_players[0])
  num_of_players = len(list_of_players)
  # Dictionaries get appended here
  all_attack_dictionaries = []
  # Used to count the final ticks as the range() may skip over the last few otherwise.
  final_dict_accumulator = Counter()
  print(f"Total Players: {num_of_players}")
  # Loops over ticks increasing by increment each time.
  for tick in range(tick_increment - 1, total_ticks, tick_increment):
    dict_accumulator = Counter()
    # Loops over number of players
    for player in range(0, num_of_players):
    
      dict_accumulator = dict_accumulator + Counter(list_of_players[player][:tick + 1])

      # range() will skip the last few ticks if it's tick increment goes above the total number of ticks. EG, trying to get the dictionaries for 12 ticks at an interval of 5 ticks will result in only 2 dictionaries being created because 5 + 5 = 10, and another 5 is 15 which is above the total ticks (12). The if statements here are used to collect any remaining ticks and their attacks, creating a special final dictionary and appending it to the list.
      if tick + 1 + tick_increment > total_ticks and tick_increment != 1:
          final_dict_accumulator = final_dict_accumulator + Counter(list_of_players[player][0:])

    dict_accumulator["tick"] = tick + 1
    all_attack_dictionaries.append(dict_accumulator)

    print(f"Tick {tick + 1} Dictionary: " + str(dict_accumulator))

    if tick + 1 + tick_increment > total_ticks and total_ticks % tick_increment != 0:
      final_dict_accumulator["tick"] = total_ticks
      all_attack_dictionaries.append(final_dict_accumulator)
      print(f"Tick {total_ticks} final Dictionary: " + str(final_dict_accumulator))

  print("\n")
  return all_attack_dictionaries

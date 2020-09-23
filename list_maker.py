# MAIN FUNC
# Returns a list of players and their actions. Output should be fed into dictionary_maker().
def list_maker(raw_string, debug_mode = False):
  unfiltered_list = create_unfiltered_list(raw_string)
  filtered_list = filter_list(unfiltered_list)
  list_of_players = list_splitter(filtered_list)
  # Debugging
  if (debug_mode):
    print("DEBUGGING MODE ON\n")
    for i in range(len(list_of_players)):
      print(f"Player {i + 1} attack list: {list_of_players[i]}")
    print("\n")
  return list_of_players


# Turns raw string into a list with tabs replaced with underscores.
def create_unfiltered_list(raw_string):
  raw_string = raw_string.replace("stay if hp", "") 
  replaced_string = raw_string.replace("\t", "_")
  unfiltered_list  = list(replaced_string)
  return unfiltered_list


# Removes excess underscores from list such that each index in the list = 1 tick.
def filter_list(unfiltered_list):
  # Values get appended to this list, unless appending is skipped.
  filtered_list = []
  # Loops over list and filters out extra underscores.
  for i, value in enumerate(unfiltered_list):
    try:
      # If the current index's value is a newline, append it and move to next iteration.
      if value == "\n":
        filtered_list.append(value)
        continue
      # If the next index's value is an underscore or newline, append the current value. Otherwise move to next to next iteration.
      if unfiltered_list[i + 1] == "_" or unfiltered_list[i + 1] == "\n":
        filtered_list.append(value)
    # Catches IndexError at end of loop, appends final value and returns filtered_list.
    except IndexError:
      filtered_list.append(value)
      return filtered_list
  
  
# Uses the newline character to split the filtered list into sublists, one for each player.
# This works with any number of players! The master_list contains a list of 'player lists',
# AKA sublists that can be assigned to their own player variables later.
def list_splitter(filtered_list):
  master_list = []
  sublist = []
  for i, value in enumerate(filtered_list):
    if value != "\n":
      sublist.append(value)
    if value == "\n" or i == len(filtered_list) - 1:
      master_list.append(sublist)
      sublist = []
  return master_list
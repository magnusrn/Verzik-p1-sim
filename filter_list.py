# kms
from collections import Counter


all_players = list('''D				S					S					S					T				S					S					
S					D				S					S					T				S					S					
S					S					D				S					T				S					S					D
S					S					S					D				D				D				S					S	'''.replace("\t", "_")) ##paste entire google sheet tick range here


#removes excess underscores from list
def filter_list(unfiltered_list):
  filtered_list = []
  # This is a loop
  for index, value in enumerate(unfiltered_list):
    if index + 1 == len(unfiltered_list):
      filtered_list.append(value)
      # break loop if it reaches the end of the list
      break
    if value == "\n":
      # best statement
      continue
    # filters it somehow
    if unfiltered_list[index + 1] == "_" or unfiltered_list[index + 1] == "\n":
      filtered_list.append(value)
  # fin
  return filtered_list



formatted_list=filter_list(all_players)

list_slice = int(len(formatted_list) / 4)

player1 = formatted_list[0:list_slice]
player2 = formatted_list[list_slice:list_slice * 2]
player3 = formatted_list[list_slice * 2:list_slice * 3]
player4 = formatted_list[list_slice * 3:list_slice * 4]

print(all_players)
print("\n")
print(player1)
print("\n")
print(player2)
print("\n")
print(player3)
print("\n")
print(player4)
for tick in range(0,30,10):
  print(Counter(player1[0:tick]))
  print(Counter(player2[0:tick]))
  print(Counter(player3[0:tick]))
  print(Counter(player4[0:tick]))
  print("\n")
# for tick in range (30):
#   player1[tick] do stuff
#   if player1[tick] == "D":
#     dawnbringer_hits.append()
#   player2[tick] do stuff...

# TO DO
#hAVE FUN!
#remove all the fucking formatted_lists

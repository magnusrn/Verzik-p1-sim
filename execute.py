from list_maker import list_maker
from dictionary_maker import dictionary_maker
from simulator import simulate_all
import time
start_time = time.time()

# execute(raw_google_docs_string, iterations, tick_increment)

def execute(raw_google_docs_string, iterations, tick_increment, debug_mode):
  # Bad Variable handling
  if iterations <= 0 or tick_increment <= 0:
    print("Cannot use numbers that are zero or less!")
    return

  player_list = list_maker(raw_google_docs_string, debug_mode)
  attack_dictionaries, total_ticks = dictionary_maker(player_list, tick_increment, debug_mode)

  # Error Handling
  if (tick_increment > total_ticks):
    print("Tick increment cannot be greater than the total number of ticks selected!")
    print("\nReduce the tick increment of select more ticks.")
    return
  
  simulate_all(attack_dictionaries, iterations, tick_increment, debug_mode)
  print("--- %s seconds ---" % round((time.time() - start_time), 2))
  print("Fin")

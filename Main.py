from execute import execute

# Paste Google Docs selection here!
raw_google_docs_string = \
'''INPUT GOOGLE SHEET TICK CONTENT'''

# Edit these variables to whatever you like.
iterations = 100000; 
tick_increment = 1;
debug_mode = False;


# Main execute function
execute(raw_google_docs_string, iterations, tick_increment, debug_mode)

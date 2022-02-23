from time import sleep
from loading import print_loading_bar 
from sys import platform


total_iterations = 167  # Arbitrary total number of iterations (for example purposes)

if platform == "linux" or platform == "linux2":
    sleeptime = 1e-2  # I don't know if this is suitable, because I don't have a linux machine.
elif platform == "darwin":
    sleeptime = 1e-2
elif platform == "win32":
    sleeptime = 1e-11

# Example #1 (most likely how you would want to use this function)
for i in range(total_iterations):
    print_loading_bar(i, total_iterations, title="Loading Example 1: ", no_newline=True)
    sleep(sleeptime)  # To make example work - this should not be in your for loop

# Example #2 
for i in range(1, total_iterations+1):
    print_loading_bar(i, total_iterations, title="Loading Example 2: ", first_iteration_is_zero=False)
    sleep(sleeptime)

# Example w/ Bigger Bar  
for i in range(total_iterations):
    print_loading_bar(i, total_iterations, title="Big Bar Example: ", size=100)
    sleep(sleeptime)
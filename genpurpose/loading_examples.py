from time import sleep
from loading import print_loading_bar 


total_iterations = 167  # Arbitrary total number of iterations (for example purposes)

# Example #1 (most likely how you would want to use this function)
for i in range(total_iterations):
    print_loading_bar(i, total_iterations, title="Loading Example 1: ")
    sleep(1e-11)  # To make example work - this should not be in your for loop

# Example #2 
for i in range(1, total_iterations+1):
    print_loading_bar(i, total_iterations, title="Loading Example 2: ", first_iteration_is_zero=False)
    sleep(1e-11)
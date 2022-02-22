from sys import stdout


def print_loading_bar(i, count, 
                        title="", size=50, 
                        first_iteration_is_zero=True, no_newline=False):
    
    if first_iteration_is_zero:
        i = i+1

    bar_inc = count/size
    bar_size = int(i/bar_inc)
    blank_size = size-bar_size
    bar_string = "[" + "="*bar_size + " "*blank_size + "]"

    perc_inc = count/100
    perc_size = round(i/perc_inc, 1)
    perc_string = " ("+str(perc_size)+" %)"

    if i == 1 and not no_newline:  # if it's the first iteration, print on newline 
        stdout.write("\n")
    elif i != 1:  # if not the first iteration, rewrite current line
        stdout.write("\r")

    stdout.write(title+bar_string+perc_string)
    stdout.flush()

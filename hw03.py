"""
Name: Violet McAuliffe
Peers: N/A
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros
 
# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    global grades
    for idx in range ( len(grades) ):
        # First, I create the input function
        read_five_ints = input("Give me the next grade in [0 to 10]: ")
        # Then, I create the first constraint, if the input isn't a number we exit the loop. 
        if read_five_ints.isdigit() == False:
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        # Then, I turn the grades into integers, storing them in ints
        ints = int(read_five_ints)
        # Then, I make the constraint that, if the input isn't between 0 and 10, we exit the loop. 
        if ints < 0 or ints > 10:
            print("Error in read_five_ints: input integer outside of range")
            exit()
        # Last, I change the global variable to hold our fully verified inputs. 
        else:
            grades[idx] = ints

     #Anything with this indentation is NO LONGER inside the loop

# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    # First, I create the loop for choosing the averaging method. 
    
    for method in range(len(grades)):
        # I create a variable that stores the input of what averaging method the user wants. 
        method = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
        # First conditional, note here that "a" is in quotations because it is a string. 
        if method == "a":
            print("picked: Mean")
            avg = statistics.mean(grades)
        # Using the elif condition, we use a multi-path conditional to then work through what happens if b or c are picked.
        # Note that any grade calculation is stored in the variable avg. 
        elif method == "b":
            print("picked: Median")
            avg = statistics.median(grades)
        elif method == "c":
            print("picked: Mode")
            avg = statistics.mode(grades)
        # If they don't give one of our desired responses, this statement is printed and we exit.
        else:
            print("Error in pick_averaging_method: incorrect option picked")
            exit()
        # Returning our variable avg  ensures that the grade calculation is not a global variable. 
        return avg
        
# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(avg):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    # creating my loop
    for elem in range(len(grades)):
        # assigning the our input to the variable elem. 
       elem = input("Pick '1' for print average, or '2' for plot average: ")
       # first condition, which calls on the function print_list_average
       if elem == "1":
           print_list_and_average(avg)
           # second condition, which calls on function plot_grades
       elif elem == "2":
           plot_grades(avg)
       #if user inputs something we didn't ask for, the system exits
       else:
           print("Error in pick_visualization: incorrect option picked")
           exit()
       exit()
       
       


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

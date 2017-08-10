def max_of_three(argument1, argument2, argument3):

    if argument1 >= argument2:
        max_value = argument1
    else:
        max_value = argument2

    if argument3 > max_value:
        max_value = argument3

    print("Max value is = " + str(max_value))
    return max_value

max_of_three(15, 10, 2)

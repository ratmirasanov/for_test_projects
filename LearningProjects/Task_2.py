import Task_1

def max_of_three(argument1, argument2, argument3):

    max_value = Task_1.max_func(argument1, argument2)

    return Task_1.max_func(argument3, max_value)


print("Max value is = {}".format(max_of_three(15, 3, 2)))

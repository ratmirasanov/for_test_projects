def length_of_string(argument1):

    length_of_str = 0
    for letter in argument1:
        length_of_str += 1

    print("Length of string is = " + str(length_of_str))
    return length_of_str


length_of_string("Test string.")

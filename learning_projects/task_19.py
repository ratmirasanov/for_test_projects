"""Task 19."""


import time


def song_99_bottles_of_beer():
    """Function capable of generating all the verses of the song."""

    number_of_bottles = 99

    while number_of_bottles >= 0:

        if number_of_bottles != 0 and number_of_bottles != 1:

            print("{} bottles of beer on the wall, {} bottles of beer."
                  .format(number_of_bottles, number_of_bottles))
            print("Take one down and pass it around, {} bottles of beer on the wall."
                  .format(number_of_bottles - 1))
            time.sleep(1)

        elif number_of_bottles == 1:

            print("{} bottles of beer on the wall, {} bottles of beer."
                  .format(number_of_bottles, number_of_bottles))
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            time.sleep(1)
        number_of_bottles -= 1

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")


song_99_bottles_of_beer()

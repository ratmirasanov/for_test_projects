"""Task 11."""


def generate_n_chars(number, char):
    """Check that function returns a string, n characters long, consisting only of c."""

    new_str = ""
    if int(number) and char.isalpha():
        for index in range(number):
            new_str += char

        return new_str


print("The string {}, {} characters long, consisting only of {}."
      .format(generate_n_chars(7, "f"), 7, "f"))

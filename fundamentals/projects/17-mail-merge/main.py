# TODO: Create a letter using starting_letter.txt

def write_letter(a_name, a_list):
    """
    Writes a text message to a file...
    :param a_name: personalized name for a latter
    :param a_list:  message to be written to file
    """
    with open(f"./Output/ReadyToSend/letter_for_{a_name}.txt", mode="w") as output_f:
        output_f.writelines(a_list)


def modify_letter(a_name):
    """
    Reads and modifies the first line of a file
    :param a_name: personalized name for a latter
    """
    with open("./Input/Letters/starting_letter.txt", mode="r") as input_file:
        lines = input_file.readlines()

    lines[0] = f"Dear {a_name[:-1]},\n"

    # write the modified text file to a new file
    write_letter(a_name, lines)


# send an invitation to all the names from invited_names.txt
with open("./Input/Names/invited_names.txt") as names_txt:
    for name in names_txt:
        modify_letter(name)

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list

def replace_value_in_list(value_old, value_new, list_name):
    for i in range(len(list_name)):
        if list_name[i] == value_old:
            list_name[i] = value_new

def num_value_in_list(value, list_name):
    count = 0
    for i in range(len(list_name)):
        if list_name[i] == value:
            count += 1
    return count

def main():
    # open file for reading, store contents in a list
    provinces = read_list("W09/provinces.txt")
    print(provinces)
    print()
    # remove first element from the list
    provinces.pop(0)
    # remove last element from the list
    provinces.pop() # if pop has no arguments passed, default is -1
    # replace all occurrences of "AB" in the list with "Alberta"
    replace_value_in_list('AB', 'Alberta', provinces)
    # count the number of elements that are "Alberta", then print it
    value_to_count = "Alberta"
    num_value_occurances = num_value_in_list(value_to_count, provinces)
    print(f"Number of times {value_to_count} shows up in the list: {num_value_occurances}")

# Call main to start this program.
if __name__ == "__main__":
    main()
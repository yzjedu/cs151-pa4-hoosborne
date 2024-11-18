# Programmers: Hazel Osborne
# Course:  CS151, Zelalem Yalew
# Due Date: 11/22/24
# Lab Assignment: PA 4
# Problem Statement: Create a program to analyze headlines from the Australian Broadcasting Company (ABC).
# Data In: File Names, Specific words, action choices, and continue choices
# Data Out: File data
# Input Files: Files of ABC headlines


import os

# Purpose: read information from a file to a table
# Parameters: file_name
# Return: table
def read_file_to_table(file_name):
    table = []
    with open(file_name, 'r') as input_file:
        table = input_file.readlines()
        return table
    print("Error reading file. Please restart program and try again.")
    return table

# Purpose: count the number of titles a specific word is used in
# Parameters: table,
# Return: none
def count_specific_word(table):
    count = 0
    word = str(input("Please enter the word you would like to search for: "))
    word = word.strip()
    for row in table:
        if word.lower() in row.lower():
            count += 1
    print("There are", count, "headlines with", word, "in them.")
    return

# Purpose: write headlines containing a specific word to another file named by user
# Parameters: table
# Return: none
def write_headlines_with_word(table):
    write_table = []
    word = str(input("Please enter the word you would like to search for: "))
    for row in table:
        if word in row:
            write_table.append(row)
    output_file = input("Please enter the name of the file: ")
    data_file = open(output_file, "w")
    for row in write_table:
        line = str(row) + "\n"
        data_file.write(row)

    data_file.close()
    print("Your data has been added to", output_file, ".")
    return

# Purpose: Determine the average number of characters per headline
# Parameters: table
# Return: none
def average_headline_characters(table):
    row_length = 0
    total_length = 0
    for row in table:
        total_length += len(row)
    average_characters = total_length / len(table)

    print("The average number of characters per line is", f"{average_characters:.2f}" , "characters.")
    return

# Purpose: Find and output the shortest and longest title in a file
# Parameters: table
# Return: none
def longest_shortest_headline(table):

    long_length = 0
    short_length = 2000
    longest_headline = []
    shortest_headline = []
    for row in table:
        row_length = len(row)
        if row_length > long_length:
            long_length = row_length
            longest_headline = row
        if row_length < short_length:
            short_length = row_length
            shortest_headline = row
    print("The longest shortest headline is:", longest_headline, long_length, "characters. \n")
    print("The shortest headline is:", shortest_headline, short_length, "characters.")
    return

# Purpose: Error check user input file name
# Parameters: none
# Return: file
def new_file_name():
    file = str(input("Please enter a file name: "))
    while not os.path.isfile(file):
        file = str(input("Please enter a valid file name: "))
    return file

# Purpose: Analyze headlines from the Australian Broadcasting Company
# Parameters: none
# Return: none
def main():
    continue_choice = 'yes'
    print("\nWelcome! This program analyzes headlines from the Australian Broadcasting Company (ABC).")
    print("-"*150)
    file_name = new_file_name()
    headline_table = read_file_to_table(file_name)
    while continue_choice == 'yes':


        print("-"*150)
        print("Below, enter which analyzing action you would like to do. "
              "\nEnter 1 to: Determine how many headlines have a particular word in it, for a single file."
              "\nEnter 2 to: Write headlines containing a specific word to a new file."
              "\nEnter 3 to: Determine the average number of characters per headline."
              "\nEnter 4 to: Output the longest and shortest headline."
              "\nEnter 5 to: Pick a new file to analyze.")
        print("-"*150)

        choice_action = input("Please enter your choice: ")
        while choice_action not in ["1", "2", "3", "4", "5"]:
            choice_action = (input("Please enter a valid choice: "))
        print("-"*150)


        if choice_action == "1":
            count_specific_word(headline_table)
            print("-"*150)

        elif choice_action == "2":
            write_headlines_with_word(headline_table)
            print("-" * 150)

        elif choice_action == "3":
            average_headline_characters(headline_table)
            print("-" * 150)

        elif choice_action == "4":
            longest_shortest_headline(headline_table)
            print("-" * 150)

        elif choice_action == "5":
            file_name = new_file_name()
            headline_table = read_file_to_table(file_name)
            print("-" * 150)

        print("Would you like to continue?")
        continue_choice = input("Please enter yes or no: ")
        while continue_choice.lower() != "yes" and continue_choice.lower() != "no":
            continue_choice = input("Please enter yes or no: ")
        print("-"*150)
    print("Thank you for using this program!")

main()
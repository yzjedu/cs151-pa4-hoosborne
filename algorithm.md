
* Name: read_file_to_table
* Purpose: read information from a file to a table
* Parameters: file_name
* Return: table 
* Algorithm: 
1. set table as an empty string
2. With open file_name to read as input file
   1. Set table to the read input file
   2. Return table
3. Output error message and return table

* Name: count_specific_word:
* Purpose: count the number of titles a specific word is used in 
* Parameters: table
* Return: none 
* Algorithm: 
1. Initialize count 
2. Prompt user to enter the word they would like to search for
2. For each row in table:
   3. If the word is in row:
      4. Increment count by one
3. Display count to user. 

* Name: write_headlines_with_word
* Purpose: write headlines containing a specific word to another file named by user
* Parameters: table
* Return: none 
* Algorithm: 
1. Prompt user to enter the word they would like to use 
2. Set write_table as empty
3. For each row in table:
   1. Check if word is in row:
      1. append row to write_table
4. Prompt user to enter a file name to write on, store as output_file
5. Open the file for writing
6. For row in write_table:
   1. write row to the output file. 
7. Close the file
8. Return

* Name: average_headline_characters
* Purpose: Determine the average number of characters per headline
* Parameters: table
* Return: none 
* Algorithm: 
1. Initialize row_length and total_length.
2. For each row in table:
   2. Concatenate row length with total_length:
3. Calculate average_characters by dividing total_length by len(table)
4. Output average characters to user
5. Return

* Name: longest_shortest_headline
* Purpose: Find and output the shortest and longest title in a file 
* Parameters: table
* Return: none 
* Algorithm: 
1. Initialize long_length and short_length
2. Set longest_headline and shortest_headline to empty lists
3. For row in table:
   1. Concatenate row_length with len(row)
   2. Check if row_length > long_length:
      1. Set long_length to equal row_length
      2. Set longest_headline to row
   3. Otherwise, check if row_length < short_length:
      1. Set short_length to equal row_length
      2. Set shortest_headline to equal row_length
4. Output the shortest headline and longest headline to user

* Name: new_file_name
* Purpose: Error check user input file name
* Parameters: none 
* Return: file
* Algorithm: 
1. Prompt user to input a file name, set as file.
2. While file does not exist,
   1. Prompt user to re_enter a valid file name, set as file.
3. return file

* Name: main
* Purpose: Analyze headlines from the Australian Broadcasting Company
* Parameters: none
* Return: none 
* Algorithm:
2. Set continue_choice to "yes"
1. Display welcome message to user
2. Call new_file_name, set as file_name
3. Call read_file_to_table using file_name, set as headline_table
3. While continue_choice equals "yes":
   4. Display action choices with their corresponding input 
   5. Prompt user to enter what analyzing action they would like to complete, store as choice_action.
   5. While choice_action is not 1-5, inclusive:
      6. Re-Prompt user to enter a valid input

   5. Check if action_choice equals 1:
      6. Run count_specific_word using headline_table

   6. Check if action_choice equals 2:
      7. Run write_headlines_with_word using headline_table

   7. Check if action_choice equals 3:
      8. Run average_headline_characters using headline_table

   8. Check if action_choice equals 4:
      9. run longest_shortest_headline using headline_table

   9. Check if action_choice equals 5:
      10. Run new_file_name, set as file_name
      11. Run read_file_to_table using file_name, set as headline_table

   10. Prompt user to enter whether they would like to continue, set as continue_choice (Yes/No)
   11. While continue_choice != "yes" or "no":
       12. reprompt user to enter a valid input.
   
5. Display Thank You Message
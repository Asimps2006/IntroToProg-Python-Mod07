# ------------------------------------------------- #
# Title: Assignment07, Script Showing How Pickle Works
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Andy Simpson, 03/03/2020,Created Script
# ------------------------------------------------- #
import pickle
import sys
import pathlib

# Data -------------------------------------------- #
strFileName = 'StudentData.dat'
lstTable = []  # A list that acts as a 'table' of rows
strPathExists = pathlib.Path(strFileName)  # Use the "pathlib.Path()" to see if the file exists


# Processing -------------------------------------- #
class DoStuff:
    """ Process and do things here"""
    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        """ Save list data to a Binary data file

        :param file_name: (string) Name of the Binary File to dump data into
        :param list_of_data: (list) list object (a dictionary) written to binary using Pickle
        :return: Nothing
        """
        # Create a File Object by opening and appending the input dictionary object into the StudentData.dat file
        # the "ab+" binary access mode is used below to first create the binary file if needed, otherwise just append
        # the data to the end of the existing file
        file = open(file_name, "ab+")
        # Use Pickle here to write list (dictionary) row to the binary file
        pickle.dump(list_of_data, file)
        # Close the file object here
        file.close()

    # noinspection SpellCheckingInspection
    @staticmethod
    def read_data_from_file(file_name):
        """ Read Binary data into a list

        :param file_name: (string) Name of the Binary File to load
        :return: Nothing
        """
        # Global List Variable here
        global lstTable
        # Use a with loop to open the StudentData.dat file here
        with (open(file_name, "rb")) as openfile:
            # Set a while loop here to append all of the dictionaries into a list object
            # Very similar to the .readlines method used for text files
            while True:
                # Set up a Try/Except block here so that I can get to the end of the .dat binary file
                try:
                    # Unpickle all of the data in the ,dat file and append it to a list here
                    lstTable.append(pickle.load(openfile))
                except EOFError:
                    # break out of the loop if the End of the file is reached
                    break

    @staticmethod
    def add_data_to_list(studentID, name, income, email):
        """ Add a task name and priority to the list

        :param studentID: (integer) Student ID:
        :param name: (string) Name of Student:
        :param income: (string) Enter Desired Income
        :param email: (string) Enter Email Address
        :return: 'success'
        """
        # Set access to Global Variables within this function here
        global lstTable
        # Create the dictionary row object using the user input values and the next ID value
        dicRow1 = {"ID": studentID, "Name": name, "Income": income, "Email": email}
        # Append the dictionary row to the List Table
        lstTable.append(dicRow1)
        # Super important here to save the dictionary to the .dat binary data file
        DoStuff.save_data_to_file(strFileName, dicRow1)
        return 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_intro():
        """  Display a menu of choices to the user

        :return: nothing
        """
        # Introduction, print script name, demonstrate print() statement formatting here
        print("""\t\t\t <<<<<<  New Student Information Database  >>>>>>
        Hello, this is a simple Student Information Database that uses the python
        pickle method for storing data.  Please enter a menu option below.  The Student 
        information database stores the following information: Student ID, Student Name,
        Desired Income and email address.
        """)

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        # Send the User a list of options here using a print statement and fancy formatting
        print('''Menu of Options:
        1) Add a New Student
        2) Print a Table of New Student Names   
        3) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        # User Choice Selection here
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_new_student():
        """ Get new student information here

        :return: nothing
        """
        intID = int(input("Enter Student ID: "))  # <<Enter/Get Student ID Here save as an integer
        strStudentName = str(input("Enter Student Name: "))  # <<Enter/Get Student Name Here as a string
        strIncome = str(input("Desired Income?  "))  # <<Enter/Get desired income as a string
        strEmail = str(input("Email address?  "))  # <<Enter/Get desired the Email as a string
        # Use this function below to add the new student info to the list and to the binary .dat file
        DoStuff.add_data_to_list(intID, strStudentName, strIncome, strEmail)

    @staticmethod
    def print_current_student_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Student List: *******")  # Title of Table
        # Added the following 3 print statements to build the table of task items
        print("     ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("       |   ID:     |   Name:         |   Email Address:   |   Desired Income:  ")
        print("     --------------------------------------------------------------------")
        # Use this for loop to print each row or dictionary into a table for the user
        for item in list_of_rows:
            # Use dictionary .get method to design the table and print for the end user
            print("    ", item.get("ID"), item.get("Name"), item.get("Email"), item.get("Income"), sep="   |  ")
        print("     ***********************************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(optional_message="Add another Student?(Y/N): "):
        """ Gets a yes or no choice from the user, pass in an optional message
        :param optional_message: Pass in a Yes/No Question message
        :return: string
        """
        # Use the Default Message or pass in an optional message, strip white spaces, and make lower case
        return str(input(optional_message)).strip().lower()


try:
    # print the intro to the Student Information Database here
    IO.print_intro()
    # Check to see if the StudentData.dat Binary file exists or not.
    if strPathExists.exists():
        # If the file does exist than read the data from the .dat binary file into a list
        DoStuff.read_data_from_file(strFileName)
    else:
        # If the file doesn't exist, create it using this function
        DoStuff.save_data_to_file(strFileName, lstTable)
    # Use this "while" loop for the main menu task selection
    while True:
        IO.print_menu_tasks()  # Shows menu
        strChoice = IO.input_menu_choice()  # Get menu option
        # Step 1 - Process user's menu choice
        if strChoice.strip() == '1':  # Enter New Student Information
            while True:  # Use a While loop to allow for continued data entry
                # Use this IO function to input new student information
                IO.input_new_student()
                # Evaluate the user choice and exit loop if "n" in response
                if "n" in IO.input_yes_no_choice():
                    print()  # Add a line here for readability
                    # Exit the loop and go to the Main Menu
                    break

        elif strChoice == '2':  # Print a table of students
            while True:  # Use a While loop to allow for printing the student list repeatedly
                # Get the current list of Students from the IO function below
                IO.print_current_student_list(lstTable)
                # Evaluate the user choice and exit loop if "n" in response
                if "n" in IO.input_yes_no_choice(
                        "Print Student list again? (y/n) - "):  # Use the user choice IO function here
                    print()  # Add a line here for readability
                    # Exit the loop and go to the Main Menu
                    break
        elif strChoice == '3':  # Exit Program
            print("Goodbye!")
            break  # and Exit
        else:
            # Use a print statement to send a reminder to the user
            print('Please choose only 1, 2, or 3!"')
            print()

# Error handling starts here
except Exception as e:

    # Print the following error handling statements
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    # Using the sys library here to get the line number of the line that failed
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # print the line number here
    print("Line No: " + str(exc_tb.tb_lineno))
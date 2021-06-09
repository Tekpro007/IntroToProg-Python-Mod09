# ------------------------------------------------------------------------ #
# Title: Main.py
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Kyle Gilpin, 6.8.2021, Wrote main function to print menu option
# Kyle Gilpin, 6.8.2021, Wrote main function to grab user input
# Kyle Gilpin, 6.8.2021, Wrote main function to print the current list and add data
# Kyle Gilpin, 6.8.2021, Wrote main function to save data and exit
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    import ProcessingClasses, IOClasses, DataClasses

else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# setup variables
strFileName = "EmployeeData.txt"
lstOfObjects = []

# Load data from file into a list of employee objects when script starts
lstOfObjects= ProcessingClasses.FileProcessor.read_file_data(strFileName, lstOfObjects)

#
while True:
    # Show user a menu of options
    IOClasses.EmployeeIO.print_menu_items()
    # Get user's menu option choice
    strChoice = IOClasses.EmployeeIO.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice.strip() == '1':
        IOClasses.EmployeeIO.print_current_list_items(lstOfObjects)
        continue

    # Let user add data to the list of employee objects
    elif strChoice.strip() == '2':
        objE1 = IOClasses.EmployeeIO.input_employee_data()
        lstOfObjects.append(objE1)
        continue

    # let user save current data to file
    elif strChoice.strip() == '3':
        ProcessingClasses.FileProcessor.save_data_to_file(strFileName, lstOfObjects)
        continue

    # Let user exit program
    elif strChoice.strip() == '4':
        print('Exitting program')
        exit()

# Main Body of Script  ---------------------------------------------------- #
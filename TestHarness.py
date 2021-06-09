# ---------------------------------------------------------- #
# Title: Listing 10
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kyle Gilpin, 6.8.2021, Wrote test functions for testing employee and person
# Kyle Gilpin, 6.8.2021, Wrote function to test menu options
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!
    from DataClasses import Person as Per  # Employee class only!
    from IOClasses import EmployeeIO as Eio
    import ProcessingClasses as P  # processing classes
else:
    raise Exception("This file was not created to be imported")

# # Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

#Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_file_data("EmployeeData.txt", lstTable)
lstTable.clear()
print(lstTable)

# Test data module
objP1 = Per("Bob", "Smith")
objP2 = Per("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

#Test processing module
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_file_person_data("PersonData.txt", lstTable)
print(lstTable)

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items_person(lstTable)
Eio.input_employee_data()
print(Eio.input_menu_options())


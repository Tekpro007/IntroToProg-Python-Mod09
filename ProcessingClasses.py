# ---------------------------------------------------------- #
# Title: ProcessingClasses.py
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kyle Gilpin, 6.8.2021, Imported data from listing stater file
# Kyle Gilpin, 6.8.2021, Wrote function to open data for person
# ---------------------------------------------------------- #
import dataclasses

import DataClasses

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_file_data(file_name, list_of_rows):
        """ Reads data from a file
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                employee_id, first_name, last_name = line.split(",")
                obj1 = DataClasses.Employee(employee_id.strip(), first_name.strip(), last_name.strip())
                list_of_rows.append(obj1)
            file.close()
            return list_of_rows

        except FileNotFoundError as e:
            print('File not found!')

    @staticmethod
    def read_file_person_data(file_name, list_of_rows):
        """ Reads data from a file
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                first_name, last_name = line.split(",")
                obj1 = DataClasses.Person(first_name.strip(), last_name.strip())
                list_of_rows.append(obj1)
            file.close()
            return list_of_rows

        except FileNotFoundError as e:
            print('File not found!')
"""
Author: Jurez Evans
Date: Dec 30 2023
"""
import sys
from datetime import datetime


class Scanner:
    """
    A class that reads a set of data, counting each occurrence of a job skill,
    and tracking new skill requirements.
    """
    outfile = "Summary.txt"
    outfile_b = "Prioritized_Summary"
    infile = "skill_set.txt"
    filter = [" (Required)"]

    @classmethod
    def QuickSort(cls, array, data=None, order="asc"):
        """
        Sort an array of elements in ascending order by default or in descending order if specified

        :param data: Dictionary of (key : count) pair.
        :param array: List of elements to sort
        :param order: Use "asc" to sort in ascending order and "dsc" to sort descending order.
        :return: a Sorted array
        """
        if len(array) <= 1:
            return array

        pivot = array[len(array)//2]

        if order.lower() == "asc":
            # Sort the keys in Alphabetical order
            smaller = [key for key in array if key < pivot]
            equals = [key for key in array if key == pivot]
            greater = [key for key in array if key > pivot]

            # left sub array: smaller + middle sub array: equals + right sub array: greater
            return cls.QuickSort(smaller) + equals + cls.QuickSort(greater)

        elif order.lower() == "dsc":
            # Sorts each key in descending order based on its corresponding "count" value
            smaller = [key for key in array if data[key] < data[pivot]]
            equals = [key for key in array if data[key] == data[pivot]]
            greater = [key for key in array if data[key] > data[pivot]]

            # left sub array: greater + middle sub array: equals + right sub array: smaller
            return cls.QuickSort(greater, data, order.lower()) + equals + cls.QuickSort(smaller, data, order.lower())
    @classmethod
    def read_data(cls):
        try:
            input_data = open(cls.infile, "r")
            out_data = open(cls.outfile, "w")
            out_data_b = open(cls.outfile_b, "w")

            # Read and Process data from file
            skills_data = {}
            out_data.write("Job market summary as of Date: "+datetime.today().strftime('%Y-%m-%d, Time: %H:%M:%S')+"\n")
            out_data_b.write(
                "Job market summary as of Date: " + datetime.today().strftime('%Y-%m-%d, Time: %H:%M:%S') + "\n")
            # for-loop reads data from skill_set file
            for x in input_data:
                skill = x.strip("\n")
                if skill in cls.filter:
                    continue
                # Assuming one skill per line
                unique_skills = skills_data.keys()
                if skill in unique_skills:
                    # This skill item was found previously, update count
                    updateCount = int(skills_data.get(skill)) + 1
                    #increment by 1
                    skills_data.update({skill: updateCount})
                else:
                    # This is a new skill item, update dictionary
                    skills_data.update({skill: 1})
            # Exit for-loop and format output files

            keys = skills_data.keys()
            # Sorting Algorithm : Sort skills in alphabetical order
            a_z_list = cls.QuickSort(list(skills_data))
            # Sorting Algorithm : Sort skills in descending order based on corresponding count value
            desc_list = cls.QuickSort(list(skills_data), skills_data, "dsc")

            # format out_data file into alphabetical order
            for found_skill in a_z_list:
                line = found_skill + " (" + str(skills_data[found_skill]) + ")\n"
                out_data.write(line)
            # format out_data_b file into descending order based on corresponding count value
            for found_skill in desc_list:
                line = found_skill + " (" + str(skills_data[found_skill]) + ")\n"
                out_data_b.write(line)

            input_data.close()
            out_data.close()
            out_data_b.close()


        except OSError:
            raise OSError("File does not exist.")



    def __init__(self):
        """stub method:
         No relevant instance fields or methods yet.
         """


def main():
    try:
        input_data = open(Scanner.infile, "x")
    except OSError:
        pass

    Scanner.read_data()
    """stub"""


if __name__ == '__main__':
    sys.exit(main())

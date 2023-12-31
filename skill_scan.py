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

    @classmethod
    def QuickSort(cls, array, order="asc"):
        """
        Sort an array of elements in ascending order by default or in descending order if specified

        :param array: List of elements to sort
        :param order: Use "asc" to sort in ascending order and "dsc" to sort descending order.
        :return: a Sorted array
        """
        if len(array) <= 1:
            return array

        pivot = array[len(array)//2]
        smaller = [x for x in array if x < pivot]
        equals = [x for x in array if x == pivot]
        greater = [x for x in array if x > pivot]

        if order.lower() == "asc":
            #Sort ascending order
            # left sub array: smaller + middle sub array: equals + right sub array: greater
            return smaller + equals + greater
        elif order.lower() == "dsc":
            #Sort descending order
            # left sub array: greater + middle sub array: equals + right sub array: smaller
            return greater + equals + smaller
    @classmethod
    def read_data(cls):
        try:
            input_data = open(cls.infile, "r")
            out_data = open(cls.outfile, "w")
            out_data_b = open(cls.outfile_b, "w")

            # Read and Process data from file
            skills_data = {}
            out_data.write("Job market summary as of Date: "+datetime.today().strftime('%Y-%m-%d, Time: %H:%M:%S')+"\n")
            # for-loop reads data from skill_set file
            for x in input_data:
                skill = x.strip("\n")
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
                # Sorting Algorithm : Sort skills in alphabetical order
                # a_z_list =
                # Sorting Algorithm : Sort skills in descending order
                # desc_list =

                # Exit for-loop and format output file
                for found_skill in skills_data:
                    line = found_skill + " (" + str(skills_data[found_skill]) + ")\n"
                    out_data.write(line)
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

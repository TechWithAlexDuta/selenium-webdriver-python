"""read files"""
import csv


def get_csv_data(file_path):
    """
    read csv file to a list of dict
    """
    data_list = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for line in reader:
            data_list.append(line)
    return data_list
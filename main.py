import csv

from sort_lst import sort_lst
from debug_double import debug_double
from open_csv import contacts_list


if __name__ == '__main__':
    contacts_list = sort_lst(contacts_list)
    contacts_list = debug_double(contacts_list)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

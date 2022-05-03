from phone_debug import pattern_phone, conf_phone
from open_csv import contacts_list

import re


def sort_lst(contact_list):
    for lst in contact_list:
        sorting_name = (lst[0] + ' ' + lst[1] + ' ' + lst[2]).strip().split(' ')
        if len(lst) > 7:
            del lst[7:]
        for id, name in enumerate(sorting_name):
            lst[id] = name
            lst[5] = re.sub(pattern_phone, conf_phone, lst[5])

    for lst in contacts_list:
        if not lst[2]:
            for contact_ in contacts_list[1:]:
                if lst[0] == contact_[0] and lst[1] == contact_[1] and contact_[2]:
                    lst[2] = contact_[2]
    return contact_list

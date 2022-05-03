def debug_double(contact_list: list):
    list_len = len(contact_list)
    i = 1
    while i < list_len - 1:

        j = i + 1
        while j < list_len:

            if contact_list[i][0] == contact_list[j][0] and contact_list[i][1] == contact_list[j][1] and \
                    contact_list[i][2] == contact_list[j][2]:
                if contact_list[j][3] != '':
                    contact_list[i][3] = contact_list[j][3]
                if contact_list[j][4] != '':
                    contact_list[i][4] = contact_list[j][4]
                if contact_list[j][5] != '':
                    contact_list[i][5] = contact_list[j][5]
                if contact_list[j][6] != '':
                    contact_list[i][6] = contact_list[j][6]
                contact_list.pop(j)
                list_len = list_len - 1
                continue
            j += 1

        i += 1
    return contact_list

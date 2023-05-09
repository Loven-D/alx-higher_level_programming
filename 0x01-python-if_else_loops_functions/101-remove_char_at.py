#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    count = 0
    str_cp = ""
    for element in str:
        if count == n:
            count += 1
            continue
        str_cp += str[count]
        count += 1
    return str_cp

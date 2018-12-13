#!/usr/bin/env python
# encoding: utf-8

"""
    barber
    ~~~~~~~~~~~~~

    a useless tool to cut the string with blank and line break.
"""

def cut(str, length = 4, group = 8, style = ' '):
    
    str = "".join([str[i] + style if (i  + 1) % length == 0 and not i == 0 else str[i] for i in range(len(str))])
    str = "".join([str[i] + "\n" if (i  + 1) % ((length + 1) * group) == 0 and not i == 0 else str[i] for i in range(len(str))])

    return str
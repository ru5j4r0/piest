import piest.type as ptype


def value_type(dic, key):
    return ((val := dic[key]), type(val)) if key in dic else (None, ptype.NONE)

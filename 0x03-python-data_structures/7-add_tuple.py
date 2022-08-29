#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)
    if len_tuple_a >= 2 and len_tuple_b >= 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len_tuple_a == 0 and len_tuple_b >= 2:
        return tuple_b[0], tuple_b[1]
    elif len_tuple_a == 1 and len_tuple_b >= 2:
        return tuple_a[0] + tuple_b[0], tuple_b[1]
    elif len_tuple_a == 1 and len_tuple_b == 1:
        return tuple_a[0] + tuple_b[0], 0
    elif len_tuple_a == 1 and len_tuple_b == 0:
        return tuple_a[0], 0
    elif len_tuple_a == 2 and len_tuple_b == 0:
        return tuple_a[0], tuple_a[1]
    elif len_tuple_a == 2 and len_tuple_b == 1:
        return tuple_a[0] + tuple_b[0], tuple_a[1]
    elif len_tuple_a == 0 and len_tuple_b == 1:
        return 0, tuple_b[0]
    elif len_tuple_a == 0 and len_tuple_b == 0:
        return 0, 0

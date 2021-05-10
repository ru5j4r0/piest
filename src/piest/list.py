from itertools import chain

def head_rest(l):
    return (l[0], l[1:]) if len(l) != 0 else (None, [])

def flat(l):
    return list(chain.from_iterable(l))

def split_map_flat(l):
    return flat(map(str.split, l))

def divide(l, v):
    return (l[:(i := l.index(v))], l[i+1:]) if v in l else (l, None)


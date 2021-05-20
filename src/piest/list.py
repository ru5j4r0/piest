from itertools import chain


def head_rest(li):
    return (li[0], li[1:]) if len(li) != 0 else (None, [])


def flat1_chain(li):
    return list(chain.from_iterable(li))


def splits(li):
    return list(map(str.split, li))


def flat_splits(l):
    return flat1_chain(splits(l))


def divide(l, v):
    return (l[:(i := l.index(v))], l[i+1:]) if v in l else (l, None)

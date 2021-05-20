from itertools import chain


def head_rest(li):
    return (li[0], li[1:]) if len(li) != 0 else (None, [])


def flat1_chain(li):
    return list(chain.from_iterable(li))


def splits(li):
    return list(map(str.split, li))


def flat_splits(li):
    return flat1_chain(splits(li))


def divide(li, val):
    return (li[:(i := li.index(val))], li[i+1:]) if val in li else (li, [])

from itertools import chain
from piest import type as ptype


def head_rest(seq):
    return (seq[0], seq[1:]) if len(seq) != 0 else (None, ptype.defval(seq))


def flat1_chain(li):
    return list(chain.from_iterable(li))


def splits(l):
    return map(str.split, l)


def flat_splits(l):
    return flat1_chain(splits(l))


def divide(l, v):
    return (l[:(i := l.index(v))], l[i+1:]) if v in l else (l, None)

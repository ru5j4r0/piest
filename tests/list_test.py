import pytest
import piest.list as plist


class TestList:
    @pytest.mark.parametrize('li, res', [
        ([], (None, [])),
        ([1], (1, [])),
        ([1, 2], (1, [2])),
        ([1, 2, 3], (1, [2, 3])),

        ((), (None, ())),
        ((1,), (1, ())),
        ((1, 2), (1, (2,))),
        ((1, 2, 3), (1, (2, 3))),

        ('', (None, '')),
        ('a', ('a', '')),
        ('ab', ('a', 'b')),
        ('abc', ('a', 'bc'))
    ])
    def test_head_rest(self, li, res):
        assert plist.head_rest(li) == res

    @pytest.mark.parametrize('li, res', [
        ([[], (), ''], []),
        ([[1], ('ab',), 'c'], [1, 'ab', 'c']),
        ([[1, 2], (3, 'ab'), 'cd'], [1, 2, 3, 'ab', 'c', 'd'])
    ])
    def test_flat1(self, li, res):
        assert plist.try_flat1(li) == res

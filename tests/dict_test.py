import pytest

import piest.dict as pdict


class TestDict:
    @pytest.mark.parametrize('dic, key, res', [
        ({}, None, (None, type(None))),
        ({1: 2}, 1, (2, int)),
        ({1: 2}, 2, (None, type(None))),
        ({1: 2, 'a': 'b'}, 'a', ('b', str)),
        ({1: 2, 'a': 'b'}, 'b', (None, type(None)))
    ])
    def test_value_type(self, dic, key, res):
        assert pdict.value_type(dic, key) == res

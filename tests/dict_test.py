import pytest
import piest.dict as pdict
import piest.type as ptype


class TestDict:
    @pytest.mark.parametrize('dic, key, res', [
        ({}, None, (None, ptype.NONE)),
        ({1: 2}, 1, (2, int)),
        ({1: 2}, 2, (None, ptype.NONE)),
        ({1: 2, 'a': 'b'}, 'a', ('b', str)),
        ({1: 2, 'a': 'b'}, 'b', (None, ptype.NONE))
    ])
    def test_value_type(self, dic, key, res):
        assert pdict.value_type(dic, key) == res

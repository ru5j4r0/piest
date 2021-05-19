import pytest
import piest.type as ptype


class TestList:
    @pytest.mark.parametrize('val, res', [
        ([1, 2, 3], []),
        ((1, 'a', 'cd'), ()),
        ('abc', '')
    ])
    def test_defval(self, val, res):
        assert ptype.defval(val) == res

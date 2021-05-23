import pytest

import piest.list as plist


class TestList:
    @pytest.mark.parametrize('li, res', [
        ([], (None, [])),
        ([1], (1, [])),
        ([1, 2], (1, [2])),
        ([1, 2, 3], (1, [2, 3]))
    ])
    def test_head_rest(self, li, res):
        assert plist.head_rest(li) == res

    @pytest.mark.parametrize('li, res', [
        ([[], []], []),
        ([[1], [[2]]], [1, [2]]),
        ([[1, 2], [[3, 4]]], [1, 2, [3, 4]])
    ])
    def test_flat1_chain(self, li, res):
        assert plist.flat1_chain(li) == res

    @pytest.mark.parametrize('li, res', [
        ([], []),
        ([''], [[]]),
        (['abc', 'de fg'], [['abc'], ['de', 'fg']])
    ])
    def test_splits(self, li, res):
        assert plist.splits(li) == res

    @pytest.mark.parametrize('li, res', [
        ([], []),
        ([''], []),
        (['abc', 'de fg'], ['abc', 'de', 'fg'])
    ])
    def test_flat_splits(self, li, res):
        assert plist.flat_splits(li) == res

    @pytest.mark.parametrize('li, val, res', [
        ([], None, ([], [])),
        ([1], 1, ([], [])),
        ([1, 2], 1, ([], [2])),
        ([1, 2], 2, ([1], [])),
        ([1, 2, 3], 2, ([1], [3])),
        ([1, 2, 3], 4, ([1, 2, 3], []))
    ])
    def test_divide(self, li, val, res):
        assert plist.divide(li, val) == res

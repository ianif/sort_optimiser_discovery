from sorter import sort_numbers

def test_empty():
    assert sort_numbers([]) == []

def test_single():
    assert sort_numbers([1]) == [1]

def test_sorted():
    assert sort_numbers([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert sort_numbers([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert sort_numbers([3, 1, 2, 1]) == [1, 1, 2, 3]

def test_does_not_mutate_input():
    original = [3, 1, 2]
    original_copy = original[:]
    sort_numbers(original)
    assert original == original_copy  # input list must not be modified by sort_numbers

def test_returns_new_list():
    original = [3, 1, 2]
    result = sort_numbers(original)
    assert result is not original  # must return a new list, not the same object
    assert result == [1, 2, 3]

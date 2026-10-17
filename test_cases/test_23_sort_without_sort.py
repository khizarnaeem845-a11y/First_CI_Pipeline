import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort

def test_normal_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([7]) == [7]

def test_negative_and_duplicate_values():
    assert bubble_sort([0, -2, 4, -2, 1]) == [-2, -2, 0, 1, 4]

def test_original_list_is_unchanged():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]

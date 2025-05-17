def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.

    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list

    Example:
    >>> rotate_list([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    '''
    k %= len(lst)  # Handle cases where k is larger than the list length
    return lst[-k:] + lst[:-k]

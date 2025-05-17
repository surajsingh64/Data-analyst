def swap_alternate_elements(t):
    '''Swap every alternate of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with alternate elements swapped.

    Examples:
    >>> swap_alternate_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_alternate_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    swapped_list = list(t)  # Convert the tuple to a list
    for i in range(0, len(swapped_list), 2):
        swapped_list[i], swapped_list[i + 1] = swapped_list[i + 1], swapped_list[i]
    return tuple(swapped_list)  # Convert the list back to a tuple
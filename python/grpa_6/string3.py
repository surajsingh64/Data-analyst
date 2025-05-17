def is_palindrome(n: int) -> bool:
    '''Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise

    Example:
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(1212)
    False
    '''
    return str(n) == str(n)[::-1]

def progress(a1: int, r: int, n: int) -> int:
    """
    Calculate the nth term of an arithmetic progression using recursion.

    An arithmetic progression is a sequence of numbers where each term after the first
    is obtained by adding a constant difference to the previous term.

    The formula for the nth term is: a_n = a1 + (n-1)*r

    This function implements the calculation recursively by repeatedly adding
    the common difference to reach the desired term.

    Args:
        a1 (int): The first term of the arithmetic progression
        r (int): The common difference between consecutive terms
        n (int): The position of the term to calculate (must be positive integer)

    Returns:
        int: The nth term of the arithmetic progression
    """
    if n == 1:
        return a1
    return progress(a1, r, n - 1) + r


if __name__ == '__main__':
    a1 = int(input('Enter the 1-st term of the progression: '))
    r = int(input('Enter the difference of the progression: '))
    n = int(
        input('Enter the number of progression term you need to find: ')
    )
    print(progress(a1, r, n))

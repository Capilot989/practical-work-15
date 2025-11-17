def count(a: int, b: int) -> int:
    """
       Counts the number of squares that can be cut from a rectangle of size AxB
       by always cutting the largest possible square using a recursive algorithm.

       Args:
           a (int): The length of the rectangle (natural number)
           b (int): The width of the rectangle (natural number)

       Returns:
           int: The number of squares that can be cut
       """
    min_len = min(a, b)
    max_len = max(a, b)

    if a == b:
        return 1
    if min_len == 0:
        return 0

    return max_len // min_len + count(max_len % min_len, min_len)


if __name__ == '__main__':
    a, b = map(int, input(
        'Enter side lenghts separated by spaces: '
    ).split())
    print(count(a, b))

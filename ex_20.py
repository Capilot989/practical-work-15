def comp(a: str, b: str, m: int, n: int) -> int:
    """
    Finds the length of the longest common contiguous subsequence
    between two strings using a recursive approach.

    Args:
        a (str): First string
        b (str): Second string
        m (int): Current position in first string (initially length of a)
        n (int): Current position in second string (initially length of b)

    Returns:
        int: Length of the longest common contiguous subsequence
    """
    if m == 0 or n == 0:
        return 0
    if a == b:
        return m
    if a[m-1] == b[n-1]:
        return 1 + comp(a, b, m-1, n-1)
    return max(
        comp(a, b, m, n-1), comp(a, b, m-1, n)
    )


if __name__ == '__main__':
    a, m = map(
        lambda x: int(x) if x.isdigit() else x,
        input('Enter the 1-st string and its length: ').split()
    )
    b, n = map(
        lambda x: int(x) if x.isdigit() else x,
        input('Enter the 2-nd string and its length: ').split()
    )
    print(comp(a, b, m, n))

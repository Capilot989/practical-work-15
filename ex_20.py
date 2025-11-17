def comp(a: str, b: str, m: int, n: int) -> int:
    """
        Finds the length of the longest common contiguous substring between two strings.

        Uses a recursive approach to find the maximum length of a contiguous sequence
        of characters that appears in both strings in the same order.

        Args:
            a (str): First input string
            b (str): Second input string
            m (int): Length of the first string (current position in recursion)
            n (int): Length of the second string (current position in recursion)

        Returns:
            int: Length of the longest common contiguous substring
        """
    def count_match(ind_a: int, ind_b: int) -> int:
        """
               Recursively counts the length of matching contiguous substring 
               starting from the current positions.

               Args:
                   ind_a (int): Current position in string a
                   ind_b (int): Current position in string b

               Returns:
                   int: Length of contiguous matching substring ending at current positions
               """
        if ind_a == 0 or ind_b == 0:
            return 0
        if a[ind_a-1] == b[ind_b-1]:
            return 1 + count_match(ind_a-1, ind_b-1)
        else:
            return 0

    if m == 0 or n == 0:
        return 0

    match_here = count_match(m, n)

    return max(
        match_here,
        comp(a, b, m-1, n),
        comp(a, b, m, n-1)
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

def combin(n: int, k: int) -> int:
    """
        Calculate the binomial coefficient C(n, k) using recursion.

        The binomial coefficient C(n, k) represents the number of ways to choose
        k elements from a set of n elements without regard to order.

        Args:
            n (int): Total number of elements (non-negative integer)
            k (int): Number of elements to choose (non-negative integer)

        Returns:
            int: The binomial coefficient C(n, k)
        """
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return combin(n - 1, k - 1) + combin(n - 1, k)


if __name__ == '__main__':
    while True:
        n, k = map(int, input
        ('Enter the numbers n and k separated by a space'
        ' to calculate the number of combinations of n by k.\n'
        'Note: k must be less than n.\n').split()
                   )
        if k <= n:
            break
        else:
            print('\n' * 10)
    print(combin(n, k))

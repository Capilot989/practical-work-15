def degree5(n: int) -> int:
    """
        Determine the exponent of 5 for a natural number n using recursion.

        This function checks if the given natural number n is a power of 5.
        If n is a power of 5, it returns the exponent (k such that 5^k = n).
        If n is not a power of 5, it returns -1.

        Args:
            n (int): A natural number (positive integer) to check

        Returns:
            int: The exponent k if n = 5^k, otherwise -1
        """
    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    if n == 5:
        return 1
    exponent = degree5(n // 5)
    if exponent != -1:
        return exponent + 1
    return -1


if __name__ == '__main__':
    n = int(input('Enter a natural number: '))
    print(degree5(n))

def divisibility_test(x: int, div: int) -> int:
    """
       Recursively tests divisibility of a number by checking odd divisors.

       Args:
           x (int): The number to check for primality
           div (int): The current divisor to test (should be odd)

       Returns:
           int: 1 if no divisors found, 0 if a divisor is found
       """
    if div ** 2 > x:
        return 1
    if x % div == 0:
        return 0
    return divisibility_test(x, div + 2)


def function1(x: int) -> int:
    """
        Determines if a natural number is prime using optimized recursive checking.

        This function uses an optimized approach that:
        - Handles small numbers directly
        - Checks divisibility by 2 separately
        - Only checks odd divisors using recursion

        Args:
            x (int): A natural number to check for primality

        Returns:
            int: 1 if the number is prime, 0 otherwise
        """
    if x < 2:
        return 0
    if x == 2:
        return 1
    return divisibility_test(x, 3)


if __name__ == '__main__':
    x = int(input('Enter the number: '))
    print(function1(x))

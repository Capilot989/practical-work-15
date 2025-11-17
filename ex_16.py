def ten_to_n(x: int, n: int) -> str:
    """
       Convert a natural number from decimal to base n (2 ≤ n ≤ 16)
       using recursion.

       Args:
           x (int): A natural number (positive integer) to convert
           n (int): The target base (2 to 16)

       Returns:
           str: The number representation in base n as a string
       """
    digits = '0123456789ABCDEF'
    if x < n:
        return digits[x]
    return ten_to_n(x // n, n) + digits[x % n]


if __name__ == '__main__':
    x = int(input('Enter the number to convert: '))
    n = int(input('Enter the target base: '))
    print(ten_to_n(x, n))

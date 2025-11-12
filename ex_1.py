def pownum(a: float, n: int) -> float:
    """
       Calculate the power of a real number raised to an integer degree using recursion.

       This function computes a^n by recursively multiplying the base number 'a'
       by itself 'n' times. The recursion continues until the degree reaches 1.

       Args:
           a (float): The base real number to be raised to a power
           n (int): The integer exponent (degree) to raise the base to

       Returns:
           float: The result of a raised to the power of n (a^n)
       """
    if n == 1:
        return a
    return pownum(a, n - 1) * a


if __name__ == '__main__':
    a = float(input('Enter the real number: '))
    n = int(
        input('Enter the degree to what you want raise the number: ')
    )
    print(pownum(a, n))

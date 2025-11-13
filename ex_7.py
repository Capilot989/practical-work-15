def nod(a: int, b: int) -> int:
    """
       Calculate the Greatest Common Divisor (GCD) of two natural numbers using recursion.

       This function uses the Euclidean algorithm to compute the GCD recursively.
       The Euclidean algorithm is based on the principle that the GCD of two numbers
       does not change if the larger number is replaced by its difference with the smaller number.

       Args:
           a (int): First natural number
           b (int): Second natural number

       Returns:
           int: The greatest common divisor of a and b
       """
    max_numb = max(a, b)
    min_numb = min(a, b)
    if min_numb == 0:
        return max_numb
    return nod(min_numb, max_numb % min_numb)


if __name__ == '__main__':
    a ,b = (map(int, (
        input('Enter 2 numbers separated '
              'by spaces to calculate GCD: ').split()))
            )
    print(nod(a, b))

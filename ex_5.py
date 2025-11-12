def mod_number(a: int, b: int) -> int:
    """
    Find the remainder of dividing natural number a by natural number b using recursion.

    This function calculates the remainder (modulus) of a divided by b by recursively
    subtracting b from a until a becomes less than b. The final value of a is the remainder.

    Args:
        a (int): The dividend (natural number, positive integer)
        b (int): The divisor (natural number, positive integer)

    Returns:
        int: The remainder of a divided by b
    """
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    if a < b:
        return a
    return mod_number(a - b, b)


if __name__ == '__main__':
    a = int(input('Enter the natural dividend: '))
    b = int(input('Enter the natural divisor: '))
    print(mod_number(a, b))

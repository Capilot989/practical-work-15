def numbers(x: int) -> None:
    """
     Recursively prints the digits of a natural number in reverse order.

     Each digit is printed on a separate line, starting from the last digit
     and moving to the first.

     Args:
         x (int): A natural number whose digits will be printed
     """
    if x <= 9:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


if __name__ == '__main__':
    x = int(input('Enter the natural number: '))
    numbers(x)

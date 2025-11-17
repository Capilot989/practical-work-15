def ten_to_bin(x: int) -> str:
    """
      Convert a natural number from decimal to binary using recursion.

      Args:
          x (int): A natural number to convert to binary

      Returns:
          str: Binary representation of the number as a string
      """
    if x == 0:
        return '0'
    if x == 1:
        return '1'
    return ten_to_bin(x // 2) + str(x % 2)


if __name__ == '__main__':
    x = int(input('Enter the number which you need to convert: '))
    print(ten_to_bin(x))

def fib(k: int) -> int:
    """
      Calculate the k-th term of the Fibonacci sequence using recursion.

      This function uses a recursive approach to compute the k-th Fibonacci number.

      Args:
          k (int): The position in the Fibonacci sequence

      Returns:
          int: The k-th Fibonacci number
      """
    if k == 1 or k == 2:
        return 1
    return fib(k - 1) + fib(k - 2)


if __name__ == '__main__':
    k = int(input('Enter the position in the Fibonacci sequence: '))
    print(fib(k))

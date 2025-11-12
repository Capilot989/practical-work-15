def sum_progress(a1: int, r: int, n: int) -> int:
    """
      Calculate the sum of the first n terms of an arithmetic progression using recursion.

      An arithmetic progression is a sequence where each term after the first is obtained
      by adding a constant difference to the previous term.

      This function recursively calculates the sum of the first n terms by:
      - Base case: when n = 1, the sum is just the first term a1
      - Recursive case: sum of first n terms = sum of first (n-1) terms + nth term

      Args:
          a1 (int): The first term of the arithmetic progression
          r (int): The common difference between consecutive terms
          n (int): The number of terms to sum (must be non-negative integer)

      Returns:
          int: The sum of the first n terms of the arithmetic progression
      """
    if n == 1:
        return a1
    return  sum_progress(a1, r, n - 1) + (a1 + (n - 1) * r)


if __name__ == '__main__':
    a1 = int(input('Enter the 1-st term of the progression: '))
    r = int(input('Enter the difference of the progression: '))
    n = int(
        input('Enter the number of terms to sum: ')
    )
    print(sum_progress(a1, r, n))

def simmetr(s: str, i: int, j: int) -> bool:
    """
      Determines if the substring of s from i to j is symmetric (a palindrome).

      The function checks if the substring reads the same forwards and backwards using recursion.

      Args:
          s (str): The string to check
          i (int): Starting number of char of the substring (>= 1)
          j (int): Ending number of char of the substring (>= 1)

      Returns:
          bool: True if the substring is symmetric, False otherwise
      """
    if s[i - 1] != s[j - 1]:
        return False
    if i == j:
        return True
    return simmetr(s, i + 1, j - 1)


if __name__ == '__main__':
    s = input('Enter string to check: ')
    i = int(input('Enter starting number of char of the substring: '))
    j = int(input('Enter starting number of char of the substring: '))
    print(simmetr(s, i, j))

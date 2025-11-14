def maxlist(a: list) -> int:
    """
      Recursively finds the maximum element in a list of integers.

      Args:
          a: List of integers to search through

      Returns:
          The maximum integer value in the list
      """
    if len(a) == 1:
        return a[0]
    
    max_cut = maxlist(a[1:])
    return max_cut if max_cut > a[0] else a[0]


if __name__ == '__main__':
    a = list(map(int, input(
        'Enter the terms of list separeted by spaces: ').split()
                 ))
    print(maxlist(a))

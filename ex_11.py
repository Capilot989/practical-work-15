def ind_maxlist(a: list) -> int:
    """
          Recursively finds index of maximum element in a list of integers.

          Args:
              a: List of integers to search through

          Returns:
              The maximum integer value in the list
          """
    if len(a) == 1:
        return 0
    ind_max_cut = ind_maxlist(a[1:])
    return (ind_max_cut + 1) if a[ind_max_cut + 1] > a[0] else 0


if __name__ == '__main__':
    a = list(map(int, input(
        'Enter the terms of list separeted by spaces: ').split()
                 ))
    print(ind_maxlist(a))

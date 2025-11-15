def search(a: list, x: int) -> int:
    """
        Recursively searches for an element in a list.

        Args:
            a (list): The list to search through
            x (int): The element to search for

        Returns:
            int: 1 if the element is found, 0 otherwise
        """
    if len(a) == 1 and a[0] != x:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)


if __name__ == '__main__':
    a = list(map(int,
                 input('Enter the terms of list'
                       ' separated by spaces: ').split())
             )
    x = int(input('Enter the numb which we search: '))
    print(search(a, x))

def odd_list(a: list, n: int) -> list:
    """
       Recursively extracts even numbers from a list.

       This function processes the list from the end to the beginning, checking
       each element and building a new list containing only even numbers.

       Args:
           a (list): The input list containing integer elements
           n (int): The number of elements to process from the beginning of the list

       Returns:
           list: A new list containing only the even numbers from the input list
       """
    if n == 0:
        return []
    if a[n - 1] % 2 == 0:
        return odd_list(a, n - 1) + [a[n - 1]]
    return odd_list(a, n - 1)


if __name__ == '__main__':
    a = list(map(int,
                 input('Enter the terms of list'
                       ' separated by spaces: ').split())
             )
    n = int(input('Enter number of terms: '))
    print(odd_list(a, n))

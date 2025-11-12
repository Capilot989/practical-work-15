def count(n: int) -> int:
    """
        Recursively count the number of digits in a natural number.

        This function calculates the number of digits in a positive integer
        by recursively dividing the number by 10 until it becomes less than 10.

        Args:
            n (int): A natural number (positive integer) whose digits need to be counted

        Returns:
            int: The number of digits in the given natural number
        """
    if n < 10:
        return 1
    return count(n // 10) + 1


if __name__ == '__main__':
    n = int(input('Enter the number: '))
    print(count(n))

"""Module"""
def find_sum(spisok: list[int]) -> int:
    """Function"""
    return sum(spisok)

if __name__ == '__main__':
    assert find_sum([2,4,6]) == 12
    print('Test passed')

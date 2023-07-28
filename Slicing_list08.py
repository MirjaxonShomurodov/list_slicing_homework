def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1=['a', 1, 'b', 2, 'c', 3, 'd', 4]
    return list1[::-n]
print(main("list1",-1))
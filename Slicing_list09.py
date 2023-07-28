def main(list1,n):
    """
    A list of several elements is given. Return all items except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1=["a","s","d","f","g","h","j"]
    return list1[n:]
print(main("list1",3))
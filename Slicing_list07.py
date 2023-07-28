def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1=["a","s","d","f","g","h","j","k","l"]
    return list1[::n]
print(main("list1",2))
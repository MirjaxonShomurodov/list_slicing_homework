def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1=["a","s","d","f","g","h","j","k","l","q"]
    return list1[:n:-1]
print(main("list1",3))
def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    list1=["a","d","f","b","k","l"]
    list=list1+list1[5::-1]
    return list
print(main(list))
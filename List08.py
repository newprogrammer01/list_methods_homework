def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    ans=[]
    while fruits:
        x=fruits.pop()
        if x!="apple":
            ans.append(x)
    return ans
print(main(["apple","orange","banaana"]))



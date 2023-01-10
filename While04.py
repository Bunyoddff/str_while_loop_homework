def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    d=0
    while i<=len(s)-1:
        if s[i].isupper():
            d+=1
        i+=1
    return d
print(main('PythOn 2022'))
from string import punctuation
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    d=0
    while i<=len(s)-1:
        if not s[i].strip(punctuation):
            d+=1
        i+=1
    return d
print(main('asdkjfk@h!jfs%'))
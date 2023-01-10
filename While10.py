def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """

    i=0
    sum=0
    while i<=len(s)-1:
        if int(s[i])%2!=0:
            sum+=int(s[i])
        i+=1
    return sum
print(main('234567892'))
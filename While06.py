def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    d=0
    i=0
    while i<=len(s)-1:

        if not (s[i] == 'a'or s[i]== 'e'or s[i]== 'i'or s[i]== 'o'or s[i]== 'u' or s[i]== 'A'or s[i]== 'E'or s[i]== 'I'or s[i]== 'O'or s[i]== 'U' ):
            if s[i].isalpha():

                d+=1
        i+=1
    return d
print(main('CodeschoolUz 5256650650650'))    
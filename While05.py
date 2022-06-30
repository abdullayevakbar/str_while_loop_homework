def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    while i < len(s):
        if(s[i] >= 'a' and s[i] <= 'z'):
            x += 1
        i += 1
    return x

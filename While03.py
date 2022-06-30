def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    while i < len(s):
        if(s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            x += 1
        i += 1
    i = 0
    while i < len(s):
        if(s[i] >= '0' and s[i] <= '9'):
            x += 1
        i += 1
    return len(s)-x

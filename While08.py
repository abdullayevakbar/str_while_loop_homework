def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    while i < len(s):
        if s[i] >= 0 and s[i] <= '9' and (s[i]-'0') % 2 == 1:
            x += 1
        i += 1
    return x

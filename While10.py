def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    while i < len(s):
        if s[i] >= 0 and s[i] <= '9' and (s[i]-'0') % 2 == 1:
            x += (s[i]-'0')
        i += 1
    return x

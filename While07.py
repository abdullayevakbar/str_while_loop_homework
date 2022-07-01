def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9' and (int(s[i])) % 2 == 0:
            x = x + 1
        i += 1
    return x


print(main("12345"))

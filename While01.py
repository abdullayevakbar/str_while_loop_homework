def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    while i < len(s):
        if (s[i]).isdigit:
            x += 1
        i += 1
    return x


print(main("5465789"))

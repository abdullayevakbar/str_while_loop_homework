def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i = 0
    x = 0
    y = 0
    s.lower()
    while i < len(s):
        if s[i].isalpha():
            y += 1
        if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            x += 1
        i += 1
    return y-x


print(main("codeschooluz"))

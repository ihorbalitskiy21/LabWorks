def reverse(s):
    if len(s) == 1:
        return arr[0]
    return s[-1:] + reverse(s[:-1])


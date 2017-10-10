class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


while True:
    try:
        s = input()
        if len(s) < 6:
            raise ValueTooSmallError
        break
    except ValueTooSmallError:
        print("введённая строка слишком короткая!")

print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], len(s), sep='\n')
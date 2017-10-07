def repeat(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    result = (a**2 + b ** 2) ** 0.5
    return result


if __name__ == "__main__":
    print("Test1: " + str(repeat(2, 3)))

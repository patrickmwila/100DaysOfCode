def add(n1, n2):
    """
    This is an addition function
    :param n1: operand
    :param n2: operand
    :return: The sum of n1 and n2
    """
    return n1 + n2


def subtract(n1, n2):
    """
    This is a subtraction function
    :param n1: operand
    :param n2: operand
    :return: The difference of n1 and n2
    """
    return n1 - n2


def multiply(n1, n2):
    """
    This is a multiplication function
    :param n1: operand
    :param n2: operand
    :return: The product of n1 and n2
    """
    return n1 * n2


def divide(n1, n2):
    """
    This is a division function
    :param n1: operand
    :param n2: operand
    :return: The quotient n1 and n2
    """
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

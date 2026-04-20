from sympy import symbols, sympify
from types import *



def str_to_func(function_str: str):
    x = symbols('x')

    function = sympify(function_str)
    return lambda val: function.subs(x, val)


def Secant_method(function, x0, x1):
    f = str_to_func(function)
    """
    Finds an approximation of a root using the Secant method.

    :param function: A string representing the function (e.g., "x**2 - 2")
    :param x0: First initial guess
    :param x1: Second initial guess
    :return: An approximate root or the best approximation after 30 iterations
    """

    eps = 0.001
    i = 0

    while i < 30:
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            return x1

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        if abs(x2 - x1) < eps:
            return x2

        x0 = x1
        x1 = x2
        i = i + 1

    return x1

def ge(matrix: list[list[float]]) -> list[list[float]]:
    """
    Gaussian elimination with while‑loops only.
    Increment statements rewritten in full form.
    """

    var = len(matrix[0])
    row = len(matrix)

    i = 0
    while i < row:  # we will go through each line in the matrix
        if matrix[i][i] == 0:  # if we find a row where the argument in the
            # main diagonal is 0, we will search for a row where the argument in the same
            # spot is NOT zero, and switch between them
            j = i + 1
            while j < row and matrix[j][i] == 0:
                j = j + 1
            if j < row:
                matrix[i], matrix[j] = matrix[j], matrix[i]

        lead = matrix[i][i]

        runner = 0  # we will change the argument  on the main diagonal to be 1
        # and divide every argument in this row by the main digonal argument
        while runner < var:
            matrix[i][runner] = matrix[i][runner] / lead
            runner = runner + 1

        j = i + 1  # making sure every argument under the one on the main
        # diagonal will be zero
        while j < row:
            mult = matrix[j][i]
            runner = 0
            while runner < var:
                matrix[j][runner] = matrix[j][runner] - mult * matrix[i][runner]
                runner = runner + 1
            j = j + 1

        i = i + 1

    return matrix

    pass



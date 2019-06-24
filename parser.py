import re
import sys

from Error_handler import ParserError
from Polynomial import PolyRows


def _check_argv() -> list:
    """
    Check the verbose of the argvs

    :return: list of the argv to parse
    """
    if len(sys.argv) < 2:
        raise ParserError("Not enough argument")

    # A changer.
    exception_char = re.compile(r"[a-zA-VY-Z]+")
    for av in sys.argv[1:]:
        bad_char = exception_char.findall(av)
        if bad_char:
            raise ParserError("Bad characters in the equation(s) : {}".format(bad_char))
    return sys.argv[1:]


def _parse_equation(norm_regex, equation: str):
    if equation.count('=') != 1:
        raise ParserError("The equation isn't mathematics: there's {} much \'=\'".format(equation.count('=') - 1))

    token_equations = norm_regex.findall(equation)[:-1]
    for i, token in enumerate(token_equations):
        token_equations[i] = [t for t in token if t]

    for token in token_equations:
        right = 1 if '=' in equation else 0
        if len(set(token)) == 1:
            raise ParserError("The equation isn't mathematics: their can only have 2 signs next each other")
        token = PolyRows(token, right)
        print(token)


def parser(norm_regex) -> list:
    equations_list = _check_argv()

    for equation in equations_list:
        equation = _parse_equation(norm_regex, equation)

    return equations_list

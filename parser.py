import re
import sys

from typing import List

from Error_handler import ParserError
from Polynomial import PolyRows


def _check_argv() -> list:
    """
    Check the verbose of the argvs

    :return: list of the argv to parse
    """
    if len(sys.argv) < 2:
        raise ParserError("Not enough argument")

    print("WARNING: A changer le re.compile.\n * et // ne fonxtionne pas")
    exception_char = re.compile(r"[a-zA-VY-Z]+")
    for av in sys.argv[1:]:
        bad_char = exception_char.findall(av)
        if bad_char:
            raise ParserError("Bad characters in the equation(s) : {}".format(bad_char))
    return sys.argv[1:]


def _check_coef(tokens_list: List[PolyRows]):
    for token in tokens_list:
        if token.degree > 2:
            raise ParserError("The coefficient of the variable 'X' is superior as '2' : {}".format(token))


def _parse_equation(norm_regex, equation: str):
    if equation.count('=') != 1:
        raise ParserError("The equation isn't mathematics: there's {} much \'=\'".format(equation.count('=') - 1))

    token_equations = norm_regex.findall(equation)[:-1]
    for i, token in enumerate(token_equations):
        token_equations[i] = [t for t in token if t]
    for t in token_equations:
        print(t)
    print("\n\n")
    parse_tokens = []
    right = False
    for token in token_equations:
        equal = True if '=' in token else False
        if equal:
            right = True
        if len(set(token)) == 1:
            raise ParserError("The equation isn't mathematics: their can only have 2 signs next each other")
        parse_tokens.append(PolyRows(token, right, equal))
    _check_coef(parse_tokens)
    return parse_tokens


def parser(norm_regex) -> List[List[PolyRows]]:
    equations_list = _check_argv()

    parsed_equations = []
    for equation in equations_list:
        parsed_equations.append(_parse_equation(norm_regex, equation))

    return parsed_equations

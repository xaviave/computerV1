import re
import sys

from Polynomial import PolyRows
from Error_handler import ParserError


def __check_argv():
    """
    Check the verbose of the argvs

    :return: list of the argv to parse
    """
    graph = 0
    if len(sys.argv) < 2:
        raise ParserError("Not enough argument")

    exception_char = re.compile(r"[\s\dX\+\-\/\*\=\^\.]+")
    for av in sys.argv[1:]:
        bad_char = exception_char.match(av)
        print("---- ", bad_char)
        if av == "-g":
            graph = 1
            sys.argv.remove("-g")
        elif not bad_char:
            raise ParserError(f"Bad characters in the equation : '{av}' | Only number, 'X', '/', '*', '+', '-', '.', '^' and '=' are authorized")
        elif av.count('=') != 1:
            raise ParserError(f"The equation isn't mathematics: there's {av.count('=') - 1} much \'=\' in the arg: {av}")
    return sys.argv[1:], graph


def __parse_equation(norm_regex, equation: str) -> list:
    right = False
    tokens_equation = []
    tokens_tuple = norm_regex.findall(equation)[:-1]
    for i, token in enumerate(tokens_tuple):
        equal = True if '=' in token else False
        if equal:
            right = True
        if len(set(token)) == 1:
            raise ParserError("The equation isn't mathematics: their can only have 2 signs next each other")
        tokens_equation.append(PolyRows(token, right, equal, i))
    return tokens_equation


def parser():
    equations_list, graph = __check_argv()

    equations_token_list = []
    norm_regex = re.compile(r"\s*(?P<signe>[\*\/\+\-\=\s])?\s*(?:(?P<coef>(?:-\s*)?\d+(?:\.\d+)?)?\s*(?:(?:\*)?\s*(?P<x>X)\s*(?:\^\s*(?P<degree>(?:-\s*)?\d+(?:\.\d+)?))?)?)")
    for equation in equations_list:
        equations_token_list.append(__parse_equation(norm_regex, equation))
    return equations_token_list, graph

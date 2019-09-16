from typing import List

from Error_handler import ParserError
from Polynomial import PolyRows


def __pgcd(number1: int, number2: int) -> int:
    if number2 == 0:
        return number1
    else:
        r = number1 % number2
        return __pgcd(number2, r)


def __opti_fraction(number: float) -> str:
    sign = "" if number > 0 else "- "
    number = abs(round(number, 5))
    number2 = 10
    for i in range(len(str(number)[str(number).find('.'):]) - 1):
        number2 *= 10
    number *= number2
    p = __pgcd(int(number), number2)
    number /= p
    number2 /= p
    return '\033[91m' + f"{sign}{int(number)}/{int(number2)}" + '\033[0m' if number2 != 1.0 else '\033[91m' + f"{sign}{int(number)}" + '\033[0m'


def __find_simple_solution(b: float, c: float):
    if b == 0 and c == 0:
        print("The solution of the equation is : 0 = 0, every rational number are solution")
    elif b == 0:
        print(f"The equation is False, {__opti_fraction(c)} != 0")
    elif c == 0:
        print("The solution of the equation is : X = 0")
    else:
        print(f"The solution of the equation is : X = {__opti_fraction(-1 * c / b)} ({-1 * c / b})")


def __delta_process(a: float, b: float, c: float) -> float:
    return (b * b) - (4 * a * c)


def __square_root(number: float) -> float:
    if not number:
        return 0

    g = number / 2.0
    g2 = g + 1
    while g != g2:
        n = number / g
        g2 = g
        g = (g + n) / 2
    return g


def __find_complexe_solution(a: float, b: float, c: float):
    delta = __delta_process(a, b, c)
    if delta < 0:
        sol1 = f"(- {b} - i√{delta}) / {2 * a}"
        sol2 = f"(- {b} + i√{delta}) / {2 * a}"
        print(f"Delta = {delta} < 0 so there's two solutions.\nThe solutions of the equation are : X1 = {sol1} and X2 = {sol2}")
    elif delta == 0:
        print(f"Delta = 0 so there's one solution.\nThe solution of the equation is : X = {__opti_fraction(-b / (2 * a))}")
    else:
        sol1 = __opti_fraction((-b + __square_root(delta)) / (2 * a))
        sol2 = __opti_fraction((-b - __square_root(delta)) / (2 * a))
        print(f"Delta = {delta} > 0 so there's two solutions.\nThe solutions of the equation are : X1 = {sol1} ({round((-b + __square_root(delta)) / (2 * a), 5)}) and X2 = {sol2} ({round((-b - __square_root(delta)) / (2 * a), 5)})")


def __check_degree(tokens_list: List[PolyRows]):
    for token in tokens_list:
        if token.degree > 2 or token.degree < 0 or "." in str(token.degree):
            token.create_term(token.position)
            raise ParserError(
                f"The degree must be inferior or equal to 2, here : {token.degree} in this term: '{token.term}'")


def resolver(tokens_list: List[PolyRows]) -> list:
    __check_degree(tokens_list)
    a = 0
    b = 0
    c = 0
    for token in tokens_list:
        if token.degree == 2:
            a = token.coef if token.operator == "+" else -1 * token.coef
        elif token.degree == 1:
            b = token.coef if token.operator == "+" else -1 * token.coef
        else:
            c = token.coef if token.operator == "+" else -1 * token.coef

    if a:
        __find_complexe_solution(a, b, c)
    else:
        __find_simple_solution(b, c)
    return [a, b, c]

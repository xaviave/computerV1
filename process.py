from typing import List

from Polynomial import PolyRows
from resolver import resolver


def __change_equation(tokens_equations: List[PolyRows]) -> bool:
    for token in tokens_equations:
        if token.change:
            return True
    return False


def __print_row_equation(message: str, token_equations: List[PolyRows], end=" = 0.0"):
    if not __change_equation(token_equations):
        return
    color = ['\033[0m', '\033[91m', '\033[92m', '\033[94m']
    if end == "red":
        end = color[1] + " = 0.0"
    print(color[3] + f"{message} :\n" + color[0], end='\t' * 3)
    for i, token in enumerate(token_equations):
        print(color[token.change] + f"{token.equal}{token}" + color[0],
              end=' ' if i != len(token_equations) - 1 else f'{end}\n\n')
        token_equations[i].change = 0


def __reset_position(tokens_list: List[PolyRows]) -> List[PolyRows]:
    for i in range(len(tokens_list)):
        if tokens_list[i].position != i:
            tokens_list[i].position = i
            tokens_list[i].change = 2
    return tokens_list


def __operator_finder(tokens_list: List[PolyRows], operator: List[str]) -> bool:
    for token in tokens_list:
        if token.operator in operator:
            return True
    return False


def __definitive_form_checker(tokens_list: List[PolyRows]) -> bool:
    degree = []
    for token in tokens_list:
        degree.append(token.degree)
    if len(degree) == len(set(degree)):
        return True
    return False


def __refactor_list(tokens_list, len_tmp, calculate_token):
    tokens_list.insert(calculate_token.position, calculate_token)
    tokens_list = __reset_position(tokens_list)
    for i in range(len_tmp):
        tokens_list.pop(calculate_token.position + 1)
    tokens_list = __reset_position(tokens_list)
    return tokens_list


def __calculate_multiplication(multiplications_list: List[PolyRows]) -> PolyRows:
    coef = 0
    degree = 0
    operator = []
    for i, m in enumerate(multiplications_list):
        if m.operator == '-':
            operator.append(m.operator)
        if i == 0:
            degree = m.degree
            coef = m.coef
            right = m.right
            equal = True if m.equal else False
            position = m.position
        else:
            degree += m.degree
            if m.operator == "*":
                coef *= m.coef
            else:
                coef /= m.coef
    if coef < 0:
        operator.append('-')
    return PolyRows(["+" if len(operator) % 2 == 0 else "-", str(abs(coef)), "X", str(degree)], right, equal, position)


def __calculate_addition(additions_list: List[PolyRows]) -> PolyRows:
    coef = 0
    degree = 0
    for i, m in enumerate(additions_list):
        if m.operator == '-':
            m.coef = -1 * m.coef
        if i == 0:
            coef = m.coef
            degree = m.degree
            position = m.position
        else:
            coef += m.coef
    return PolyRows(["+" if coef >= 0 else "-", str(abs(coef)), "X", str(degree)], False, "", position)


def calculate_operator(tokens_list: List[PolyRows], option) -> List[PolyRows]:
    i = 0
    while i < len(tokens_list) - 1:
        tmp = [i]
        if option == 0:
            while i + 1 < len(tokens_list) and tokens_list[i + 1].operator in ["*", "/"]:
                i += 1
                tmp.append(i)
        else:
            while i + 1 < len(tokens_list) and tokens_list[i + 1].operator in ["+", "-"] \
                    and tokens_list[i + 1].degree == tokens_list[i].degree:
                i += 1
                tmp.append(i)
        i += 1
        if len(tmp) > 1:
            calculate_token = __calculate_multiplication(
                [tokens_list[t] for t in tmp]) if option == 0 else __calculate_addition([tokens_list[t] for t in tmp])
            tokens_list = __refactor_list(tokens_list, len(tmp), calculate_token)
            break
    return tokens_list


def process_equation(tokens_list: List[PolyRows]):
    __print_row_equation("The full equation refactored", tokens_list, "")

    tokens_list = [token for token in tokens_list if token.coef != 0]
    tokens_list = __reset_position(tokens_list)
    for i, token in enumerate(tokens_list):
        token.create_term(i)
    __print_row_equation("The equation without all the null degree and coefficient and the signs simplified",
                         tokens_list, "")

    while __operator_finder(tokens_list, ["*", "/"]):
        calculate_operator(tokens_list, 0)
    __print_row_equation("The equation with all the multiplication's term simplified", tokens_list, "")

    for i, token in enumerate(tokens_list):
        token.change_sign_form_equal(i)
        token.change = True
    __print_row_equation("The equation with all term in the same side", tokens_list, "red")

    tokens_list = sorted(tokens_list, key=lambda token: token.degree, reverse=True)
    tokens_list = __reset_position(tokens_list)
    for i, token in enumerate(tokens_list):
        token.create_term(i)
    __print_row_equation("The equation sorted by degree", tokens_list)

    while __operator_finder(tokens_list, ["+", "-"]) and not __definitive_form_checker(tokens_list):
        calculate_operator(tokens_list, 1)
    __print_row_equation("The equation with all the addition's term simplified", tokens_list)

    tokens_list = [token for token in tokens_list if token.coef != 0]
    tokens_list = __reset_position(tokens_list)
    for i, token in enumerate(tokens_list):
        token.create_term(i)
    __print_row_equation("The equation without all the null degree and coefficient and the signs simplified",
                         tokens_list)

    return resolver(tokens_list)

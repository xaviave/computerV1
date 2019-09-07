from typing import List

from Polynomial import PolyRows
from operator import itemgetter, attrgetter


def __print_row_equation(message: str, token_equations: List[PolyRows], end=" = 0.0"):
    print(f"{message} :\n", end='\t' * 3)

    for i, token in enumerate(token_equations):
        print(f"{token.equal}{token}",
              end=' ' if i != len(token_equations) - 1 else f'{end}\n\n')


def __calculate_degree(l):
    return


def calculate(tokens_list: List[PolyRows]) -> List[PolyRows]:
    final_tokens = []
    for i in range(3):
        tmp = [token for token in tokens_list if token.degree == i]
        if len(tmp) > 0:
            final_tokens.append(__calculate_degree(tmp))


def process_equation(tokens_list: List[PolyRows]):
    __print_row_equation("The full equation is", tokens_list, "")

    tokens_list = [token for token in tokens_list if token.coef != 0 or (token.coef2 != 0 and token.sign2)]
    for i, token in enumerate(tokens_list):
        token.create_term(i)
    __print_row_equation("The equation with all the null degree and coefficient", tokens_list, "")

    for i, token in enumerate(tokens_list):
        token.change_sign(i)
    __print_row_equation("The equation with all the sign simplified", tokens_list, "")

    for i, token in enumerate(tokens_list):
        if token.right:
            token.change_sign_form_equal(i)
    __print_row_equation("The equation with all the term on the same side", tokens_list)

    tokens_list = sorted(tokens_list, key=lambda token: token.degree, reverse=True)
    __print_row_equation("The equation sorted by degree", tokens_list)

    final_token = calculate(tokens_list)

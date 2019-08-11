from typing import List

from Polynomial import PolyRows


def _print_row_equation(message: str, token_equations: List[PolyRows]):
    print(f"{message} :\n", end='\t' * 3)

    for i, token in enumerate(token_equations):
        print(f"{token.equal}{token}",
              end=' ' if i != len(token_equations) - 1 else '\n')


def process_equation(tokens_list: List[PolyRows]):
    _print_row_equation("The full equation is", tokens_list)

    for i, token in enumerate(tokens_list):
        token.change_sign(i)
    _print_row_equation("The equation with all the sign simplified", tokens_list)

    for i, token in enumerate(tokens_list):
        if token.right:
            token.change_sign_form_equal(i)
    tokens_list.insert(len(tokens_list), PolyRows(["= 0", "=", "0", "X", "0"], True, True))
    tokens_list[len(tokens_list) - 1].create_term(len(tokens_list) - 1)
    _print_row_equation("The equation with all the term on the same side", tokens_list)

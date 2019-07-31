from typing import List

from Polynomial import PolyRows


def _print_row_equation(token_equations: List[PolyRows]):
    print("The full equation is :\n", end='\t' * 3)
    for i, token in enumerate(token_equations):
        print(f"{token}", end=' ' if i != len(token_equations) - 1 else '\n')


def process_equation(tokens_list: List[PolyRows]):
    _print_row_equation(tokens_list)
    for token in tokens_list:
        if token.right == True:
            token.change_sign_form_equal()

    print("The equation with all the term on the same side :\n", end='\t' * 3)
    for i, token in enumerate(tokens_list):
        print(token, end=' ' if i != len(tokens_list) - 1 else '\n')
        token.change_sign()

    print("The equation with all the sign simplified : \n", end='\t' * 3)

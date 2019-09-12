import re

from typing import List

from Error_handler import ParserError


class PolyRows:
    """
    term: complete form
    coef: number that compose the form
    degree: 'power' of X
    right: True if the form is in the right side of '='
    """
    term: str
    operator: str
    coef: float
    degree: int
    right: bool
    equal: str
    position: int
    change: int

    def __get_degree(self, tokens_tuple: List[str]):
        if not tokens_tuple[1] and tokens_tuple[2] == "X":
            self.coef = 1
        else:
            self.coef = float(re.sub(r"\s*", "", tokens_tuple[1]))

        try:
            if '.' in tokens_tuple[3]:
                raise ParserError(f"The degree is a float, it musts be an integer : {tokens_tuple}")
            self.degree = int(re.sub(r"\s*", "", tokens_tuple[3]))
            if self.degree > 2:
                self.create_term(self.position)
                raise ParserError(f"The degree must be inferior or equal to 2, here : {self.degree} in this term: '{self.term}'")
        except ValueError:
            self.degree = 1

    def __init__(self, tokens_tuple, right: bool, equal: bool, position: int):
        self.change = 1
        self.term = ""
        self.operator = "+"
        self.coef = 0
        self.degree = 0
        self.right = right
        self.position = position
        self.equal = "= " if equal else ""

        if (tokens_tuple[0] in ["=", "*", "/"] and position == 0) or (not tokens_tuple[0] and position > 0):
            raise ParserError(f"The equation can't start with this operator : '{tokens_tuple[0]}', '{tokens_tuple[1]}{tokens_tuple[2]}{tokens_tuple[3]}'")
        if tokens_tuple[0] not in ["-", "+", "=", "*", "/", ""]:
            raise ParserError(f"Bad or absent operator at position {position * 4}")
        elif tokens_tuple[0] in ["=", ""]:
            self.operator = "+"
        else:
            self.operator = tokens_tuple[0]

        if tokens_tuple[2] == "X":
            self.__get_degree(tokens_tuple)
        elif tokens_tuple[2] or tokens_tuple[3]:
            raise ParserError(f"Bad or absent operator at position {position * 4 + position}")
        else:
            self.coef = float(re.sub(r"\s*", "", tokens_tuple[1]))

        self.create_term(position)
        #print(f"equal = '{self.equal}', operator = '{self.operator}', coef = '{self.coef}', degree = '{self.degree}' | '{self.term}'")

    def __str__(self):
        return self.term

    def __get_operator(self):
        if (self.coef < 0 and self.operator == "-") or self.coef == 0:
            self.operator = "+"
            self.coef = abs(self.coef)
        elif self.coef > 0 and self.operator == "-":
            self.operator = "-"
            self.coef = abs(self.coef)

    def create_term(self, position):
        term = self.term
        self.__get_operator()
        self.term = ""
        if (position == 0 or self.equal == "= ") and self.operator == '+':
            self.term = ""
        elif self.operator:
            self.term = self.operator + " "
        self.term += str(self.coef)
        if self.degree != 0:
            self.term += " * X^" + str(self.degree)
        if self.term != term:
            self.change = True

    def change_sign_form_equal(self, position):
        self.equal = ''
        if self.right:
            if self.operator == "-":
                self.operator = "+"
            else:
                self.operator = "-"
        self.right = False
        self.create_term(position)


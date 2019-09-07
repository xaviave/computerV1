from typing import List

from Error_handler import ParserError


class PolyRows:
    """
    term: complete form
    coef: number that compose the form
    coef2: number that compose the form but after the Xm can only be '*' or '/'
    degree: 'power' of X
    right: True if the form is in the right side of '='
    """
    term: str
    sign: str
    coef: float
    coef2: float
    degree: int
    right: bool
    equal: str

    def __get_degree(self, tokens_list: List[str]):
        if not self.coef and tokens_list[1] == "X":
            tokens_list.insert(1, "1")
            self.coef = 1
        else:
            self.coef = float(tokens_list[1])
        try:
            if '.' in tokens_list[3]:
                raise ParserError("The degree is a float, it musts be an integer : {}".format(tokens_list))
            if tokens_list[3] in ["/", "*"]:
                self.degree = 1
            else:
                self.degree = int(tokens_list[3])
        except IndexError:
            self.degree = 0

    def __get_coef2(self, tokens_list: List[str]):
        try:
            i = tokens_list.index("*")
            print(tokens_list)
            self.coef2 = float(tokens_list[i + 1])
            self.sign2 = "*"
        except ValueError:
            i = tokens_list.index("/")
            self.coef2 = float(tokens_list[i + 1])
            self.sign2 = "/"

    def __init__(self, tokens_list: List[str], right: bool, equal: bool):
        self.sign = "+"
        self.sign2 = ""
        self.coef = 0
        self.coef2 = 0
        self.degree = 0
        self.right = right
        self.equal = "= " if equal else ""

        if tokens_list[1] == '=':
            tokens_list.pop(1)
            tokens_list[0] = tokens_list[0][1:]
        self.term = tokens_list.pop(0).strip()

        if tokens_list[0] not in ["+", "-"]:
            tokens_list.insert(0, "+")
        self.sign = tokens_list[0]
        if "X" in tokens_list:
            self.__get_degree(tokens_list)
        else:
            self.coef = float(tokens_list[1])
        if any(["*" in tokens_list, "/" in tokens_list]):
            self.__get_coef2(tokens_list)

        # print(f"sign = {self.sign}, coef = {self.coef}, degree = {self.degree}, coef2 = {self.coef2}, sign2 = {self.sign2} | {self.term}")

    def __str__(self):
        return self.term

    @staticmethod
    def __get_sign(coef, sign) -> str:
        if coef < 0 and sign == "-":
            return "+"
        else:
            return sign

    def create_term(self, position):
        self.term = "" if (position == 0 or self.equal == "= ") and self.sign == '+' else self.sign + " "
        self.term += str(self.coef)
        if self.coef2:
            self.term += " " + self.sign2 + " " + str(self.coef2)
        if self.degree != 0:
            self.term += " * X^" + str(self.degree)

    def change_sign(self, position):
        self.sign = self.__get_sign(self.coef, self.sign)
        self.sign2 = self.__get_sign(self.coef2, self.sign2)
        self.coef = abs(self.coef)
        self.create_term(position)

    def change_sign_form_equal(self, position):
        self.right = False
        self.equal = ''
        self.change_sign(position)

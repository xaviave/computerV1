from Error_handler import ParserError


class PolyRows:
    """
    term: complete form
    coef: number that compose the form
    degree: 'power' of X
    right: True if the form is in the right side of '='
    """
    term: str
    sign: str
    coef: float
    degree: int
    right: bool
    equal: str

    def __init__(self, tokens_list, right, equal):
        if tokens_list[1] == '=':
            tokens_list.pop(1)
            tokens_list[0] = tokens_list[0][1:]
        if tokens_list[1] not in ["+", "-", "*", "/"]:
            tokens_list.insert(1, "+")
        if tokens_list[2] == 'X':
            tokens_list.insert(2, "1")
        self.term = tokens_list[0].strip()
        self.sign = tokens_list[1]
        self.coef = float(tokens_list[2])
        try:
            if '.' in tokens_list[4]:
                raise ParserError("The degree is a float, it musts be an integer : {}".format(tokens_list))
            self.degree = int(tokens_list[4])
        except IndexError:
            self.degree = 0
        self.right = right
        self.equal = "= " if equal else ""

    def __str__(self):
        return self.term

    def __get_sign(self) -> str:
        if self.coef > 0 and self.sign == "-":
            return "-"
        elif self.coef < 0 and self.sign == "-":
            return "+"
        else:
            return self.sign

    def create_term(self, position):
        self.term = "" if (position == 0 or self.equal == "= ") and self.sign == '+' else self.sign + " "
        self.term += str(self.coef) + " * X^" + str(self.degree)

    def change_sign(self, position):
        self.sign = self.__get_sign()
        self.coef = abs(self.coef)
        self.create_term(position)

    def change_sign_form_equal(self, position):
        self.right = False
        self.equal = ''
        self.change_sign(position)

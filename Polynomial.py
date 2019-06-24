class PolyRows:
    """
    term: complete form
    coef: number that compose the form
    degree: 'power' of X
    right: True if the form is in the right side of '='
    """
    term: str
    coef: float
    degree: int
    right: bool

    def __init__(self, tokens_list, right):
        print(tokens_list)
        if tokens_list[1] not in ["+", "-", "=", "*", "/"]:
            tokens_list.insert(1, "+")
        if tokens_list[2] == 'X':
            tokens_list.insert(2, "1")
        self.term = tokens_list[0]
        self.coef = - float(tokens_list[2]) if tokens_list[1] == "-" else float(tokens_list[2])
        try:
            self.degree = tokens_list[4]
        except IndexError:
            self.degree = 0
        self.right = right

    def __str__(self):
        return "{: ^20} | {} * X ^ {}".format(self.term, self.coef, self.degree)

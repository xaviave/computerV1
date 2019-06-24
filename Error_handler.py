class ParserError(Exception):
    def __init__(self, value):
        self.__value = value

    def __str_(self):
        return repr(self.value)

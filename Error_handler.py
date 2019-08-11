class ParserError(Exception):
    def __init__(self, value):
        self.__value = value

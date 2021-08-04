from Lexer import Lexer


class YAPI:
    def __init__(self, g):
        self.__group = g
        pass

    def execute(self, statement):
        lexer = Lexer(self.__group, statement)
        print(lexer.tokens)
    pass

from token_data import *


class ParserSchema:
    def __init__(self, name, *data):
        self.name = name
        self.data = data
        pass
    pass


p1 = ParserSchema("Bedingte Definitionen",
                  Token("FRAGEZEICHEN", "?"),
                  "*",
                  Token("PIPE", "|"),
                  "*",
                  Token("PIPE", "|"),
                  "*",
                  Token("FRAGEZEICHEN", "?"))
p2 = ParserSchema("Bedingter Aufruf",
                  Token("FRAGEZEICHEN", "?"),
                  "*",
                  Token("FRAGEZEICHEN", "?"))

from token_data import *
from Lexer import *
from yapi import YAPI


group = YAPIGroup(
    keywords=[
        Token("SET"),
        Token("TO"),
        Token("COUNTER"),
        Token("ITERATOR")
    ],
    operators=[
        Token("SLASH", "/"),
        Token("BACKSLASH", "\\"),
        Token("KLEINER", "<"),
        Token("GROESSER", ">"),
        Token("FRAGEZEICHEN", "?"),
        Token("DOPPELPUNKT", ":"),
        Token("PIPE", "|")
    ],
    other=[
        TokenGroup("Charset", [
            Token("DIGITS")
        ])
    ]
)

t = TokenGruppen(group)
y = YAPI(t)
y.execute(r"SET <abc?1:2|2|var?.txt> TO <?var?.txt>")

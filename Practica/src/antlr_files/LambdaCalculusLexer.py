# Generated from LambdaCalculus.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,
        8,1,9,4,9,46,8,9,11,9,12,9,47,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,1,0,5,1,0,65,90,2,0,48,57,65,90,1,0,97,
        122,2,0,92,92,955,955,2,0,9,10,32,32,52,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,28,1,0,0,0,5,
        30,1,0,0,0,7,32,1,0,0,0,9,34,1,0,0,0,11,36,1,0,0,0,13,38,1,0,0,0,
        15,40,1,0,0,0,17,42,1,0,0,0,19,45,1,0,0,0,21,25,7,0,0,0,22,24,7,
        1,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,
        2,1,0,0,0,27,25,1,0,0,0,28,29,5,43,0,0,29,4,1,0,0,0,30,31,5,8801,
        0,0,31,6,1,0,0,0,32,33,5,61,0,0,33,8,1,0,0,0,34,35,5,41,0,0,35,10,
        1,0,0,0,36,37,5,40,0,0,37,12,1,0,0,0,38,39,5,46,0,0,39,14,1,0,0,
        0,40,41,7,2,0,0,41,16,1,0,0,0,42,43,7,3,0,0,43,18,1,0,0,0,44,46,
        7,4,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,49,1,0,0,0,49,50,6,9,0,0,50,20,1,0,0,0,3,0,25,47,1,6,0,0
    ]

class LambdaCalculusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MACRO_VAR = 1
    INFIX_MACRO_VAR = 2
    EQUIV = 3
    EQUAL = 4
    RPAR = 5
    LPAR = 6
    DOT = 7
    VAR = 8
    LAMBDA = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'\\u2261'", "'='", "')'", "'('", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "MACRO_VAR", "INFIX_MACRO_VAR", "EQUIV", "EQUAL", "RPAR", "LPAR", 
            "DOT", "VAR", "LAMBDA", "WS" ]

    ruleNames = [ "MACRO_VAR", "INFIX_MACRO_VAR", "EQUIV", "EQUAL", "RPAR", 
                  "LPAR", "DOT", "VAR", "LAMBDA", "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



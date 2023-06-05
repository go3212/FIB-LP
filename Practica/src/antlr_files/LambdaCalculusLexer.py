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
        4,0,12,59,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,4,11,54,8,11,11,11,12,
        11,55,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,1,0,5,1,0,65,90,2,0,48,57,65,90,1,0,97,122,2,0,92,
        92,955,955,2,0,9,10,32,32,60,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,
        32,1,0,0,0,5,34,1,0,0,0,7,36,1,0,0,0,9,38,1,0,0,0,11,40,1,0,0,0,
        13,42,1,0,0,0,15,44,1,0,0,0,17,46,1,0,0,0,19,48,1,0,0,0,21,50,1,
        0,0,0,23,53,1,0,0,0,25,29,7,0,0,0,26,28,7,1,0,0,27,26,1,0,0,0,28,
        31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,2,1,0,0,0,31,29,1,0,0,
        0,32,33,5,43,0,0,33,4,1,0,0,0,34,35,5,8801,0,0,35,6,1,0,0,0,36,37,
        5,61,0,0,37,8,1,0,0,0,38,39,5,41,0,0,39,10,1,0,0,0,40,41,5,40,0,
        0,41,12,1,0,0,0,42,43,5,125,0,0,43,14,1,0,0,0,44,45,5,123,0,0,45,
        16,1,0,0,0,46,47,5,46,0,0,47,18,1,0,0,0,48,49,7,2,0,0,49,20,1,0,
        0,0,50,51,7,3,0,0,51,22,1,0,0,0,52,54,7,4,0,0,53,52,1,0,0,0,54,55,
        1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,6,11,0,0,
        58,24,1,0,0,0,3,0,29,55,1,6,0,0
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
    RCURL = 7
    LCURL = 8
    DOT = 9
    VAR = 10
    LAMBDA = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'\\u2261'", "'='", "')'", "'('", "'}'", "'{'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "MACRO_VAR", "INFIX_MACRO_VAR", "EQUIV", "EQUAL", "RPAR", "LPAR", 
            "RCURL", "LCURL", "DOT", "VAR", "LAMBDA", "WS" ]

    ruleNames = [ "MACRO_VAR", "INFIX_MACRO_VAR", "EQUIV", "EQUAL", "RPAR", 
                  "LPAR", "RCURL", "LCURL", "DOT", "VAR", "LAMBDA", "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



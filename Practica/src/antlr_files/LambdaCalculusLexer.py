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
        4,0,11,55,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,10,4,10,50,8,10,11,10,12,10,51,1,10,1,10,0,
        0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,5,1,
        0,65,90,2,0,48,57,65,90,1,0,97,122,2,0,92,92,955,955,2,0,9,10,32,
        32,56,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,1,23,1,0,0,0,3,30,1,0,0,0,5,32,1,0,0,0,7,34,1,0,0,
        0,9,36,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,42,1,0,0,0,17,44,1,
        0,0,0,19,46,1,0,0,0,21,49,1,0,0,0,23,27,7,0,0,0,24,26,7,1,0,0,25,
        24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,2,1,0,0,
        0,29,27,1,0,0,0,30,31,5,8801,0,0,31,4,1,0,0,0,32,33,5,61,0,0,33,
        6,1,0,0,0,34,35,5,41,0,0,35,8,1,0,0,0,36,37,5,40,0,0,37,10,1,0,0,
        0,38,39,5,125,0,0,39,12,1,0,0,0,40,41,5,123,0,0,41,14,1,0,0,0,42,
        43,5,46,0,0,43,16,1,0,0,0,44,45,7,2,0,0,45,18,1,0,0,0,46,47,7,3,
        0,0,47,20,1,0,0,0,48,50,7,4,0,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,6,10,0,0,54,22,1,0,0,0,
        3,0,27,51,1,6,0,0
    ]

class LambdaCalculusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MACRO_VAR = 1
    EQUIV = 2
    EQUAL = 3
    RPAR = 4
    LPAR = 5
    RCURL = 6
    LCURL = 7
    DOT = 8
    VAR = 9
    LAMBDA = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\u2261'", "'='", "')'", "'('", "'}'", "'{'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "MACRO_VAR", "EQUIV", "EQUAL", "RPAR", "LPAR", "RCURL", "LCURL", 
            "DOT", "VAR", "LAMBDA", "WS" ]

    ruleNames = [ "MACRO_VAR", "EQUIV", "EQUAL", "RPAR", "LPAR", "RCURL", 
                  "LCURL", "DOT", "VAR", "LAMBDA", "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



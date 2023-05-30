# Generated from LambdaCalculus.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,26,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,12,8,0,
        1,0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
        0,2,0,2,0,1,2,0,3,3,5,5,26,0,11,1,0,0,0,2,20,1,0,0,0,4,5,6,0,-1,
        0,5,12,3,2,1,0,6,12,5,6,0,0,7,8,5,1,0,0,8,9,3,0,0,0,9,10,5,2,0,0,
        10,12,1,0,0,0,11,4,1,0,0,0,11,6,1,0,0,0,11,7,1,0,0,0,12,17,1,0,0,
        0,13,14,10,1,0,0,14,16,3,0,0,2,15,13,1,0,0,0,16,19,1,0,0,0,17,15,
        1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,17,1,0,0,0,20,21,7,0,0,0,21,
        22,5,6,0,0,22,23,5,4,0,0,23,24,3,0,0,0,24,3,1,0,0,0,2,11,17
    ]

class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\'", "'.'", "'\\u03BB'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LAMBDA", "VARIABLE", "WS" ]

    RULE_expression = 0
    RULE_lambda = 1

    ruleNames =  [ "expression", "lambda" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    LAMBDA=5
    VARIABLE=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambda_(self):
            return self.getTypedRuleContext(LambdaCalculusParser.LambdaContext,0)


        def VARIABLE(self):
            return self.getToken(LambdaCalculusParser.VARIABLE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LambdaCalculusParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5]:
                self.state = 5
                self.lambda_()
                pass
            elif token in [6]:
                self.state = 6
                self.match(LambdaCalculusParser.VARIABLE)
                pass
            elif token in [1]:
                self.state = 7
                self.match(LambdaCalculusParser.T__0)
                self.state = 8
                self.expression(0)
                self.state = 9
                self.match(LambdaCalculusParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LambdaCalculusParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 13
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 14
                    self.expression(2) 
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LambdaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(LambdaCalculusParser.VARIABLE, 0)

        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)


        def LAMBDA(self):
            return self.getToken(LambdaCalculusParser.LAMBDA, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_lambda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda" ):
                listener.enterLambda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda" ):
                listener.exitLambda(self)




    def lambda_(self):

        localctx = LambdaCalculusParser.LambdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lambda)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not(_la==3 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 21
            self.match(LambdaCalculusParser.VARIABLE)
            self.state = 22
            self.match(LambdaCalculusParser.T__3)
            self.state = 23
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         





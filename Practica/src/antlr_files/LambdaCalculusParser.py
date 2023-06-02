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
        4,1,9,23,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,0,1,0,1,0,0,0,24,
        0,12,1,0,0,0,2,3,6,0,-1,0,3,4,5,3,0,0,4,5,3,0,0,0,5,6,5,2,0,0,6,
        13,1,0,0,0,7,13,5,7,0,0,8,9,5,8,0,0,9,10,5,7,0,0,10,11,5,6,0,0,11,
        13,3,0,0,1,12,2,1,0,0,0,12,7,1,0,0,0,12,8,1,0,0,0,13,19,1,0,0,0,
        14,15,10,2,0,0,15,16,5,1,0,0,16,18,3,0,0,3,17,14,1,0,0,0,18,21,1,
        0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,19,1,0,0,0,2,12,
        19
    ]

class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "')'", "'('", "'}'", "'{'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "RPAR", "LPAR", "RCURL", 
                      "LCURL", "DOT", "VAR", "LAMBDA", "WS" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    T__0=1
    RPAR=2
    LPAR=3
    RCURL=4
    LCURL=5
    DOT=6
    VAR=7
    LAMBDA=8
    WS=9

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


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ApplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)


    class AbstractionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(LambdaCalculusParser.LAMBDA, 0)
        def VAR(self):
            return self.getToken(LambdaCalculusParser.VAR, 0)
        def DOT(self):
            return self.getToken(LambdaCalculusParser.DOT, 0)
        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LambdaCalculusParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(LambdaCalculusParser.LPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)

        def RPAR(self):
            return self.getToken(LambdaCalculusParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LambdaCalculusParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = LambdaCalculusParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(LambdaCalculusParser.LPAR)
                self.state = 4
                self.expression(0)
                self.state = 5
                self.match(LambdaCalculusParser.RPAR)
                pass
            elif token in [7]:
                localctx = LambdaCalculusParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(LambdaCalculusParser.VAR)
                pass
            elif token in [8]:
                localctx = LambdaCalculusParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(LambdaCalculusParser.LAMBDA)
                self.state = 9
                self.match(LambdaCalculusParser.VAR)
                self.state = 10
                self.match(LambdaCalculusParser.DOT)
                self.state = 11
                self.expression(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LambdaCalculusParser.ApplicationContext(self, LambdaCalculusParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    self.match(LambdaCalculusParser.T__0)
                    self.state = 16
                    self.expression(3) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 2)
         





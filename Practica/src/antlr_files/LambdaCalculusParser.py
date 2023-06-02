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
        4,1,11,36,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,3,0,20,8,0,1,0,1,0,1,0,1,0,1,0,5,0,
        27,8,0,10,0,12,0,30,9,0,1,1,1,1,1,1,1,1,1,1,0,1,0,2,0,2,0,1,1,0,
        2,3,39,0,19,1,0,0,0,2,31,1,0,0,0,4,5,6,0,-1,0,5,6,5,5,0,0,6,7,3,
        0,0,0,7,8,5,4,0,0,8,20,1,0,0,0,9,20,5,9,0,0,10,20,5,1,0,0,11,13,
        5,10,0,0,12,14,5,9,0,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,8,0,0,18,20,3,0,0,2,19,4,1,0,
        0,0,19,9,1,0,0,0,19,10,1,0,0,0,19,11,1,0,0,0,20,28,1,0,0,0,21,22,
        10,3,0,0,22,27,3,0,0,4,23,24,10,1,0,0,24,25,5,1,0,0,25,27,3,0,0,
        2,26,21,1,0,0,0,26,23,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,
        1,0,0,0,29,1,1,0,0,0,30,28,1,0,0,0,31,32,5,1,0,0,32,33,7,0,0,0,33,
        34,3,0,0,0,34,3,1,0,0,0,4,15,19,26,28
    ]

class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\u2261'", "'='", "')'", 
                     "'('", "'}'", "'{'", "'.'" ]

    symbolicNames = [ "<INVALID>", "MACRO_VAR", "EQUIV", "EQUAL", "RPAR", 
                      "LPAR", "RCURL", "LCURL", "DOT", "VAR", "LAMBDA", 
                      "WS" ]

    RULE_expression = 0
    RULE_macroDefinition = 1

    ruleNames =  [ "expression", "macroDefinition" ]

    EOF = Token.EOF
    MACRO_VAR=1
    EQUIV=2
    EQUAL=3
    RPAR=4
    LPAR=5
    RCURL=6
    LCURL=7
    DOT=8
    VAR=9
    LAMBDA=10
    WS=11

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


    class InfixMacroContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,i)

        def MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.MACRO_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixMacro" ):
                listener.enterInfixMacro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixMacro" ):
                listener.exitInfixMacro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixMacro" ):
                return visitor.visitInfixMacro(self)
            else:
                return visitor.visitChildren(self)


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
        def DOT(self):
            return self.getToken(LambdaCalculusParser.DOT, 0)
        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(LambdaCalculusParser.VAR)
            else:
                return self.getToken(LambdaCalculusParser.VAR, i)

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


    class MacroVarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.MACRO_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacroVar" ):
                listener.enterMacroVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacroVar" ):
                listener.exitMacroVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroVar" ):
                return visitor.visitMacroVar(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LambdaCalculusParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = LambdaCalculusParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(LambdaCalculusParser.LPAR)
                self.state = 6
                self.expression(0)
                self.state = 7
                self.match(LambdaCalculusParser.RPAR)
                pass
            elif token in [9]:
                localctx = LambdaCalculusParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LambdaCalculusParser.VAR)
                pass
            elif token in [1]:
                localctx = LambdaCalculusParser.MacroVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(LambdaCalculusParser.MACRO_VAR)
                pass
            elif token in [10]:
                localctx = LambdaCalculusParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(LambdaCalculusParser.LAMBDA)
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 12
                    self.match(LambdaCalculusParser.VAR)
                    self.state = 15 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9):
                        break

                self.state = 17
                self.match(LambdaCalculusParser.DOT)
                self.state = 18
                self.expression(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 26
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = LambdaCalculusParser.ApplicationContext(self, LambdaCalculusParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 21
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 22
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = LambdaCalculusParser.InfixMacroContext(self, LambdaCalculusParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 24
                        self.match(LambdaCalculusParser.MACRO_VAR)
                        self.state = 25
                        self.expression(2)
                        pass

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MacroDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.MACRO_VAR, 0)

        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)


        def EQUIV(self):
            return self.getToken(LambdaCalculusParser.EQUIV, 0)

        def EQUAL(self):
            return self.getToken(LambdaCalculusParser.EQUAL, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_macroDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacroDefinition" ):
                listener.enterMacroDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacroDefinition" ):
                listener.exitMacroDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroDefinition" ):
                return visitor.visitMacroDefinition(self)
            else:
                return visitor.visitChildren(self)




    def macroDefinition(self):

        localctx = LambdaCalculusParser.MacroDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_macroDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(LambdaCalculusParser.MACRO_VAR)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 33
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         





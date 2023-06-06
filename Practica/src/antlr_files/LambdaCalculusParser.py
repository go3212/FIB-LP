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
        4,1,10,33,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,0,1,0,1,0,1,0,1,0,
        5,0,28,8,0,10,0,12,0,31,9,0,1,0,0,1,0,1,0,0,2,1,0,1,2,1,0,3,4,38,
        0,20,1,0,0,0,2,3,6,0,-1,0,3,4,5,6,0,0,4,5,3,0,0,0,5,6,5,5,0,0,6,
        21,1,0,0,0,7,21,5,8,0,0,8,21,7,0,0,0,9,11,5,9,0,0,10,12,5,8,0,0,
        11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,
        0,0,0,15,16,5,7,0,0,16,21,3,0,0,2,17,18,7,0,0,0,18,19,7,1,0,0,19,
        21,3,0,0,1,20,2,1,0,0,0,20,7,1,0,0,0,20,8,1,0,0,0,20,9,1,0,0,0,20,
        17,1,0,0,0,21,29,1,0,0,0,22,23,10,6,0,0,23,24,5,2,0,0,24,28,3,0,
        0,7,25,26,10,3,0,0,26,28,3,0,0,4,27,22,1,0,0,0,27,25,1,0,0,0,28,
        31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,29,1,0,0,
        0,4,13,20,27,29
    ]

class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'\\u2261'", "'='", 
                     "')'", "'('", "'.'" ]

    symbolicNames = [ "<INVALID>", "MACRO_VAR", "INFIX_MACRO_VAR", "EQUIV", 
                      "EQUAL", "RPAR", "LPAR", "DOT", "VAR", "LAMBDA", "WS" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    MACRO_VAR=1
    INFIX_MACRO_VAR=2
    EQUIV=3
    EQUAL=4
    RPAR=5
    LPAR=6
    DOT=7
    VAR=8
    LAMBDA=9
    WS=10

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

        def INFIX_MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.INFIX_MACRO_VAR, 0)

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
        def INFIX_MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.INFIX_MACRO_VAR, 0)

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


    class MacroDefinitionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaCalculusParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)

        def MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.MACRO_VAR, 0)
        def INFIX_MACRO_VAR(self):
            return self.getToken(LambdaCalculusParser.INFIX_MACRO_VAR, 0)
        def EQUIV(self):
            return self.getToken(LambdaCalculusParser.EQUIV, 0)
        def EQUAL(self):
            return self.getToken(LambdaCalculusParser.EQUAL, 0)

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
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
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

            elif la_ == 2:
                localctx = LambdaCalculusParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(LambdaCalculusParser.VAR)
                pass

            elif la_ == 3:
                localctx = LambdaCalculusParser.MacroVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                localctx = LambdaCalculusParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LambdaCalculusParser.LAMBDA)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 10
                    self.match(LambdaCalculusParser.VAR)
                    self.state = 13 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==8):
                        break

                self.state = 15
                self.match(LambdaCalculusParser.DOT)
                self.state = 16
                self.expression(2)
                pass

            elif la_ == 5:
                localctx = LambdaCalculusParser.MacroDefinitionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 27
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = LambdaCalculusParser.InfixMacroContext(self, LambdaCalculusParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 22
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 23
                        self.match(LambdaCalculusParser.INFIX_MACRO_VAR)
                        self.state = 24
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = LambdaCalculusParser.ApplicationContext(self, LambdaCalculusParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 25
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 26
                        self.expression(4)
                        pass

             
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         





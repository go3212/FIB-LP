grammar LambdaCalculus;


expression          :   LPAR expression RPAR                    #parenExpression
                    |   VAR                                     #variable
                    |   MACRO_VAR                               #macroVar
                    |   expression expression                   #application
                    |   LAMBDA VAR+ DOT expression              #abstraction
                    |   expression MACRO_VAR expression         #infixMacro
                    ;

macroDefinition    : MACRO_VAR (EQUIV | EQUAL) expression;

MACRO_VAR         : [A-Z][A-Z0-9]*;
EQUIV             : '≡';
EQUAL             : '=';

RPAR        :   ')';
LPAR        :   '(';
RCURL       :   '}';
LCURL       :   '{';

DOT         :   '.';

VAR         :   [a-z];

LAMBDA      :   'λ' | '\\' ;
WS          :   [ \t\n]+ -> skip ;
grammar LambdaCalculus;


expression          :   LPAR expression RPAR                    #parenExpression
                    |   expression INFIX_MACRO_VAR expression   #infixMacro
                    |   VAR                                     #variable
                    |   (MACRO_VAR | INFIX_MACRO_VAR)           #macroVar
                    |   expression expression                   #application
                    |   LAMBDA VAR+ DOT expression              #abstraction
                    |   (MACRO_VAR | INFIX_MACRO_VAR) (EQUIV | EQUAL) expression    #macroDefinition
                    ;

MACRO_VAR         : [A-Z][A-Z0-9]*;
INFIX_MACRO_VAR   : '+';
EQUIV             : '≡';
EQUAL             : '=';

RPAR        :   ')';
LPAR        :   '(';

DOT         :   '.';

VAR         :   [a-z];

LAMBDA      :   'λ' | '\\' ;
WS          :   [ \t\n]+ -> skip ;

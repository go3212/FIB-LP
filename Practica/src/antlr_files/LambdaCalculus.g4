grammar LambdaCalculus;


expression          :   LPAR expression RPAR            #parenExpression
                    |   VAR                             #variable
                    |   expression ' ' expression       #application
                    |   LAMBDA VAR DOT expression        #abstraction
                    ;

RPAR        :   ')';
LPAR        :   '(';
RCURL       :   '}';
LCURL       :   '{';

DOT         :   '.';

VAR         :   [a-z];

LAMBDA      :   'λ' | '\\' ;
WS          :   [ \t\n]+ -> skip ;
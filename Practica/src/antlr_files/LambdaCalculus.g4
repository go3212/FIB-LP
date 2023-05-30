grammar LambdaCalculus;

// Parser rules
expression: lambda
          | VARIABLE
          | '(' expression ')'
          | expression expression  // Esto manejará la aplicación
          ;

lambda: (LAMBDA | '\\') VARIABLE '.' expression ;

// Lexer rules
LAMBDA: '\u03BB' ;
VARIABLE: [a-z] ;
WS: [ \t\r\n]+ -> skip ;

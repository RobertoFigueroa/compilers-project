lexer grammar Lex;

@members {

    self.self.linenum = 0
    self.self.inComment = False
    self.inString = False
    self.self.initial = True
    self.self.nesting = 0
}


NEWLINE: '\r'? '\n' {self.self.linenum+=1} -> skip;
WS:  [ \t\f\r\n]+ -> skip;

LINECOMMENT: '--' (~ '\n')* '\n' {self.self.linenum+=1} -> skip;
LINECOMMENTEOF: '--' (~ '\n')* EOF {print("Line: " + self.self.linenum)} -> skip;

BEGINCOMMENT: '(*' {self.self.initial}? 
{self.self.inComment = True
self.self.initial = False
self.self.nesting+=1
print("Start comment")} -> skip ;

// About the nestable comments

BEGINCOMMENTNEST: '(*' {self.inComment}? {self.nesting+=1} -> skip;
ENDCOMMENT:  '*)' {self.inComment}?
{self.nesting-=1
if (self.nesting == 0): 
  self.inComment = False
  self.initial = True
  print("End comment")
} -> skip;
IGNOREINCOMMENT: ~[*(\n]+  {self.inComment}?  {print("Discarding chars: " + localctx.getText())} -> skip;
IGNOREINCOMMENTLPAREN : '(' {self.inComment}?  {print("Discarding lparen")}  -> skip;
IGNOREINCOMMENTSTAR : '*' {self.inComment}?  {print("Discarding star")}  -> skip;
IGNOREINCOMMENTNEWLINE: '\n' {self.inComment}?  
{self.linenum+=1
print("Line: " + self.linenum)} -> skip;

BADENDCOMMENT:  '*)' {self.initial}?  
{print("Bad end comment")
raise Exception("Bad end ")};


TRUE: 'true';
FALSE: 'false';

CLASS: [cC][lL][aA][sS][sS];
FI: [fF][iI];
IF: [iI][fF];
IN: [iI][nN];
INHERITS: [iI][nN][hH][eE][rR][iI][tT][sS];
ISVOID: [iI][sS][vV][oO][iI][dD];
LET: [lL][eE][tT];
LOOP: [lL][oO][oO][pP];
POOL: [pP][oO][oO][lL];
THEN: [tT][hH][eE][nN];
ELSE: [eE][lL][sS][eE];
WHILE: [wW][hH][iI][lL][eE];
CASE: [cC][aA][sS][eE];
ESAC: [eE][sS][aA][cC];
NEW: [nN][eE][wW];
OF: [oO][fF];
NOT: [nN][oO][tT];

TYPE: [A-Z][_A-Za-z0-9]*;
ID:  [a-z][_A-Za-z0-9]*;
INT_CONST: [0-9][0-9]*;

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COLON: ':';
ASSIGN: '<-';
DARROW: '=>';
NEG: '~';
COMMA: ',';
PERIOD: '.';
AT: '@';
MUL: '*';
ADD: '+';
MINUS: '-';
DIV: '/';
LT: '<';
LEQ: '<=';
EQ: '=';
ERROR: . ;


fragment
ESC: '\\"' | '\\\\' ;

STR_CONST:   '"' ( ESC | .)*? '"';

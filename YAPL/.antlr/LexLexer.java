// Generated from /home/roberto/Desktop/UVG2022C2/COMPILERS/compilers-project/YAPL/Lex.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LexLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NEWLINE=1, WS=2, LINECOMMENT=3, LINECOMMENTEOF=4, BEGINCOMMENT=5, BEGINCOMMENTNEST=6, 
		ENDCOMMENT=7, IGNOREINCOMMENT=8, IGNOREINCOMMENTLPAREN=9, IGNOREINCOMMENTSTAR=10, 
		IGNOREINCOMMENTNEWLINE=11, BADENDCOMMENT=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NEWLINE", "WS", "LINECOMMENT", "LINECOMMENTEOF", "BEGINCOMMENT", "BEGINCOMMENTNEST", 
			"ENDCOMMENT", "IGNOREINCOMMENT", "IGNOREINCOMMENTLPAREN", "IGNOREINCOMMENTSTAR", 
			"IGNOREINCOMMENTNEWLINE", "BADENDCOMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NEWLINE", "WS", "LINECOMMENT", "LINECOMMENTEOF", "BEGINCOMMENT", 
			"BEGINCOMMENTNEST", "ENDCOMMENT", "IGNOREINCOMMENT", "IGNOREINCOMMENTLPAREN", 
			"IGNOREINCOMMENTSTAR", "IGNOREINCOMMENTNEWLINE", "BADENDCOMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	    
	    # YOU CAN ADD YOUR MEMBER VARIABLES AND METHODS HERE

	    linenum = 0
	    inComment = False
	    inString = False
	    initial = True
	    nesting = 0


	public LexLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Lex.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 0:
			NEWLINE_action((RuleContext)_localctx, actionIndex);
			break;
		case 2:
			LINECOMMENT_action((RuleContext)_localctx, actionIndex);
			break;
		case 3:
			LINECOMMENTEOF_action((RuleContext)_localctx, actionIndex);
			break;
		case 4:
			BEGINCOMMENT_action((RuleContext)_localctx, actionIndex);
			break;
		case 5:
			BEGINCOMMENTNEST_action((RuleContext)_localctx, actionIndex);
			break;
		case 6:
			ENDCOMMENT_action((RuleContext)_localctx, actionIndex);
			break;
		case 7:
			IGNOREINCOMMENT_action((RuleContext)_localctx, actionIndex);
			break;
		case 8:
			IGNOREINCOMMENTLPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 9:
			IGNOREINCOMMENTSTAR_action((RuleContext)_localctx, actionIndex);
			break;
		case 10:
			IGNOREINCOMMENTNEWLINE_action((RuleContext)_localctx, actionIndex);
			break;
		case 11:
			BADENDCOMMENT_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void NEWLINE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:

			    linenum+=1
			    print("Line: " + linenum)
			break;
		}
	}
	private void LINECOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:

			    linenum+=1
			    print("Line: " + linenum)
			break;
		}
	}
	private void LINECOMMENTEOF_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			print("Line: " + linenum)
			break;
		}
	}
	private void BEGINCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:

			    inComment = True
			    initial = False
			    nesting+=1
			    print("Start comment")
			break;
		}
	}
	private void BEGINCOMMENTNEST_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			nesting+=1
			break;
		}
	}
	private void ENDCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:
			nesting-=1
			        if (nesting == 0):
			            inComment = False
			            initial = True
			            print("End comment")
			      
			break;
		}
	}
	private void IGNOREINCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 6:
			print("Discarding chars: " + getText())
			break;
		}
	}
	private void IGNOREINCOMMENTLPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 7:
			print("Discarding lparen")
			break;
		}
	}
	private void IGNOREINCOMMENTSTAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 8:
			print("Discarding star")
			break;
		}
	}
	private void IGNOREINCOMMENTNEWLINE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 9:
			linenum+=1
			print("Line: " + linenum)
			break;
		}
	}
	private void BADENDCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 10:

			print("Bad end comment")
			if True : raise Exception("Bad code)
			};


			TRUE: 'true';
			FALSE: 'false';

			CLASS: 'class';
			FI: 'fi';
			IF: 'if';
			IN: 'in';
			INHERITS: 'inherits';
			ISVOID: 'isvoid';
			LET: 'let';
			LOOP: 'loop';
			POOL: 'pool';
			THEN: 'then';
			ELSE: 'else';
			WHILE: 'while';
			CASE: 'case';
			ESAC: 'esac';
			NEW: 'new';
			OF: 'of';
			NOT: 'not';

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

			STR_CONST:   '"' ( ESC | .)*? '"' {
			    String text = getText();    
			    //write your code to test strings here
			    
			    StringBuilder str = new StringBuilder(0);
			    int len = text.length();
			    int len_count = 0;
			    /* boolean flags each for one kind of error */
			    boolean nullflag = false;
			    boolean esc_nullflag = false;
			    boolean unescaped = false;
			    boolean eof = false;
			    boolean toolong = false;
			    boolean backslash = false;
			    /* check for eof, unescaped, backslash errors but don't report yet */
			    if ((text.charAt(len - 1) != '\"' && text.charAt(len - 1) != '\n' && text.charAt(len - 1) != '\\') || len == 1)
			        eof = true;
			    else if (text.charAt(len - 1) == '\n') 
			        unescaped = true;
			    /* assume the last backslash is unescaped */
			    else if (text.charAt(len - 1) == '\\')
			        backslash = true;
			    /* process special escaped characters, and make semantically equivalent string */
			    for (int i = 1; i < len - 1; ) {
			        if (text.charAt(i) == '\\') {
			            if (i + 1 < len && text.charAt(i+1) == 'n')
			                str.append('\n');
			            else if (i + 1 < len && text.charAt(i+1) == 't')
			                str.append('\t');
			            else if (i + 1 < len && text.charAt(i+1) == 'f')
			                str.append('\f');
			            else if (i + 1 < len && text.charAt(i+1) == 'b')
			                str.append('\b');
			            else if (i + 1 < len && text.charAt(i+1) == '\"'){
			                str.append('\"');
			                if (i == len - 2) {
			                    eof = true;
			                }
			            }
			            else if (i + 1 < len && text.charAt(i+1) == '\\'){
			                str.append('\\');
			                /* last backslash is not unescaped */
			                if (i == len - 2) {
			                    eof = true;
			                    backslash = false;
			                }
			            }
			            else if (i + 1 < len && text.charAt(i+1) == '\n'){
			                str.append('\n');
			                if (i == len - 2) {
			                    eof = true;
			                    unescaped = false;
			                }
			            }
			            else if (i + 1 < len && text.charAt(i+1) == '\u0000' && nullflag == false){
			                esc_nullflag = true;
			                break;
			            }
			            else if (i + 1 < len)
			                str.append(text.charAt(i+1));
			            i += 2;
			        }
			        else if (text.charAt(i) == '\u0000' && esc_nullflag == false){
			            nullflag = true;
			            break;
			        }
			        else {
			            str.append(text.charAt(i));
			            i++;
			        }
			        len_count += 1;
			        if (len_count > 1024)
			            toolong = true;
			    }

			    /* reporting errors according to the preference */
			    if (nullflag) {
			        setText("String contains null character.");
			        setType(ERROR);
			        return;
			    }
			    if (esc_nullflag) {
			        setText("String contains escaped null character.");
			        setType(ERROR);
			        return;
			    }
			    if (backslash && len_count < 1026) {
			        setText("Backslash at end of file");
			        setType(ERROR);
			        return;
			    }
			    if (unescaped && len_count < 1026)  {
			        setText("Unterminated string constant");
			        setType(ERROR);
			        return;
			    }
			    if (toolong) {
			        setText("String constant too long");
			        setType(ERROR);
			        return;
			    }
			    if (eof) {
			        setText("EOF in string constant");
			        setType(ERROR);
			        return;
			    }

			    String fstr = str.toString();
			    setText(fstr);

			break;
		}
	}
	@Override
	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return BEGINCOMMENT_sempred((RuleContext)_localctx, predIndex);
		case 5:
			return BEGINCOMMENTNEST_sempred((RuleContext)_localctx, predIndex);
		case 6:
			return ENDCOMMENT_sempred((RuleContext)_localctx, predIndex);
		case 7:
			return IGNOREINCOMMENT_sempred((RuleContext)_localctx, predIndex);
		case 8:
			return IGNOREINCOMMENTLPAREN_sempred((RuleContext)_localctx, predIndex);
		case 9:
			return IGNOREINCOMMENTSTAR_sempred((RuleContext)_localctx, predIndex);
		case 10:
			return IGNOREINCOMMENTNEWLINE_sempred((RuleContext)_localctx, predIndex);
		case 11:
			return BADENDCOMMENT_sempred((RuleContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean BEGINCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return initial;
		}
		return true;
	}
	private boolean BEGINCOMMENTNEST_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return inComment;
		}
		return true;
	}
	private boolean ENDCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENTLPAREN_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return  inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENTSTAR_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return  inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENTNEWLINE_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return inComment;
		}
		return true;
	}
	private boolean BADENDCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return initial;
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16\u0080\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\3\2\5\2\35\n\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3%\n"+
		"\3\r\3\16\3&\3\3\3\3\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5=\n\5\f\5\16\5@\13\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\6\t`\n\t\r\t\16\ta\3\t\3\t\3\t\3\t\3"+
		"\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17"+
		"\t\21\n\23\13\25\f\27\r\31\16\3\2\5\5\2\13\f\16\17\"\"\3\2\f\f\5\2\f\f"+
		"**,,\2\u0084\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2"+
		"\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2"+
		"\27\3\2\2\2\2\31\3\2\2\2\3\34\3\2\2\2\5$\3\2\2\2\7*\3\2\2\2\t8\3\2\2\2"+
		"\13F\3\2\2\2\rN\3\2\2\2\17V\3\2\2\2\21_\3\2\2\2\23h\3\2\2\2\25n\3\2\2"+
		"\2\27t\3\2\2\2\31z\3\2\2\2\33\35\7\17\2\2\34\33\3\2\2\2\34\35\3\2\2\2"+
		"\35\36\3\2\2\2\36\37\7\f\2\2\37 \b\2\2\2 !\3\2\2\2!\"\b\2\3\2\"\4\3\2"+
		"\2\2#%\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\b"+
		"\3\3\2)\6\3\2\2\2*+\7/\2\2+,\7/\2\2,\60\3\2\2\2-/\n\3\2\2.-\3\2\2\2/\62"+
		"\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\60\3\2\2\2\63\64\7"+
		"\f\2\2\64\65\b\4\4\2\65\66\3\2\2\2\66\67\b\4\3\2\67\b\3\2\2\289\7/\2\2"+
		"9:\7/\2\2:>\3\2\2\2;=\n\3\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2"+
		"?A\3\2\2\2@>\3\2\2\2AB\7\2\2\3BC\b\5\5\2CD\3\2\2\2DE\b\5\3\2E\n\3\2\2"+
		"\2FG\7*\2\2GH\7,\2\2HI\3\2\2\2IJ\6\6\2\2JK\b\6\6\2KL\3\2\2\2LM\b\6\3\2"+
		"M\f\3\2\2\2NO\7*\2\2OP\7,\2\2PQ\3\2\2\2QR\6\7\3\2RS\b\7\7\2ST\3\2\2\2"+
		"TU\b\7\3\2U\16\3\2\2\2VW\7,\2\2WX\7+\2\2XY\3\2\2\2YZ\6\b\4\2Z[\b\b\b\2"+
		"[\\\3\2\2\2\\]\b\b\3\2]\20\3\2\2\2^`\n\4\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2"+
		"\2\2ab\3\2\2\2bc\3\2\2\2cd\6\t\5\2de\b\t\t\2ef\3\2\2\2fg\b\t\3\2g\22\3"+
		"\2\2\2hi\7*\2\2ij\6\n\6\2jk\b\n\n\2kl\3\2\2\2lm\b\n\3\2m\24\3\2\2\2no"+
		"\7,\2\2op\6\13\7\2pq\b\13\13\2qr\3\2\2\2rs\b\13\3\2s\26\3\2\2\2tu\7\f"+
		"\2\2uv\6\f\b\2vw\b\f\f\2wx\3\2\2\2xy\b\f\3\2y\30\3\2\2\2z{\7,\2\2{|\7"+
		"+\2\2|}\3\2\2\2}~\6\r\t\2~\177\b\r\r\2\177\32\3\2\2\2\b\2\34&\60>a\16"+
		"\3\2\2\b\2\2\3\4\3\3\5\4\3\6\5\3\7\6\3\b\7\3\t\b\3\n\t\3\13\n\3\f\13\3"+
		"\r\f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
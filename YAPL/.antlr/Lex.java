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
public class Lex extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NEWLINE=1, WS=2, LINECOMMENT=3, LINECOMMENTEOF=4, BEGINCOMMENT=5, BEGINCOMMENTNEST=6, 
		ENDCOMMENT=7, IGNOREINCOMMENT=8, IGNOREINCOMMENTLPAREN=9, IGNOREINCOMMENTSTAR=10, 
		IGNOREINCOMMENTNEWLINE=11, BADENDCOMMENT=12, TRUE=13, FALSE=14, CLASS=15, 
		FI=16, IF=17, IN=18, INHERITS=19, ISVOID=20, LET=21, LOOP=22, POOL=23, 
		THEN=24, ELSE=25, WHILE=26, CASE=27, ESAC=28, NEW=29, OF=30, NOT=31, TYPE=32, 
		ID=33, INT_CONST=34, LPAREN=35, RPAREN=36, LBRACE=37, RBRACE=38, SEMI=39, 
		COLON=40, ASSIGN=41, DARROW=42, NEG=43, COMMA=44, PERIOD=45, AT=46, MUL=47, 
		ADD=48, MINUS=49, DIV=50, LT=51, LEQ=52, EQ=53, ERROR=54, STR_CONST=55;
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
			"IGNOREINCOMMENTNEWLINE", "BADENDCOMMENT", "TRUE", "FALSE", "CLASS", 
			"FI", "IF", "IN", "INHERITS", "ISVOID", "LET", "LOOP", "POOL", "THEN", 
			"ELSE", "WHILE", "CASE", "ESAC", "NEW", "OF", "NOT", "TYPE", "ID", "INT_CONST", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "COLON", "ASSIGN", "DARROW", 
			"NEG", "COMMA", "PERIOD", "AT", "MUL", "ADD", "MINUS", "DIV", "LT", "LEQ", 
			"EQ", "ERROR", "ESC", "STR_CONST"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "'true'", "'false'", null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "'('", "')'", "'{'", "'}'", "';'", "':'", "'<-'", "'=>'", "'~'", 
			"','", "'.'", "'@'", "'*'", "'+'", "'-'", "'/'", "'<'", "'<='", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NEWLINE", "WS", "LINECOMMENT", "LINECOMMENTEOF", "BEGINCOMMENT", 
			"BEGINCOMMENTNEST", "ENDCOMMENT", "IGNOREINCOMMENT", "IGNOREINCOMMENTLPAREN", 
			"IGNOREINCOMMENTSTAR", "IGNOREINCOMMENTNEWLINE", "BADENDCOMMENT", "TRUE", 
			"FALSE", "CLASS", "FI", "IF", "IN", "INHERITS", "ISVOID", "LET", "LOOP", 
			"POOL", "THEN", "ELSE", "WHILE", "CASE", "ESAC", "NEW", "OF", "NOT", 
			"TYPE", "ID", "INT_CONST", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", 
			"COLON", "ASSIGN", "DARROW", "NEG", "COMMA", "PERIOD", "AT", "MUL", "ADD", 
			"MINUS", "DIV", "LT", "LEQ", "EQ", "ERROR", "STR_CONST"
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



	    self.self.linenum = 0
	    self.self.inComment = False
	    self.inString = False
	    self.self.initial = True
	    self.self.nesting = 0


	public Lex(CharStream input) {
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
			self.self.linenum+=1
			break;
		}
	}
	private void LINECOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			self.self.linenum+=1
			break;
		}
	}
	private void LINECOMMENTEOF_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			print("Line: " + self.self.linenum)
			break;
		}
	}
	private void BEGINCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			self.self.inComment = True
			self.self.initial = False
			self.self.nesting+=1
			print("Start comment")
			break;
		}
	}
	private void BEGINCOMMENTNEST_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			self.nesting+=1
			break;
		}
	}
	private void ENDCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:
			self.nesting-=1
			if (self.nesting == 0): 
			  self.inComment = False
			  self.initial = True
			  print("End comment")

			break;
		}
	}
	private void IGNOREINCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 6:
			print("Discarding chars: " + localctx.getText())
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
			self.linenum+=1
			print("Line: " + self.linenum)
			break;
		}
	}
	private void BADENDCOMMENT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 10:
			print("Bad end comment")
			raise Exception("Bad end ")
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
			return self.self.initial;
		}
		return true;
	}
	private boolean BEGINCOMMENTNEST_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return self.inComment;
		}
		return true;
	}
	private boolean ENDCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return self.inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return self.inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENTLPAREN_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return self.inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENTSTAR_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return self.inComment;
		}
		return true;
	}
	private boolean IGNOREINCOMMENTNEWLINE_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return self.inComment;
		}
		return true;
	}
	private boolean BADENDCOMMENT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return self.initial;
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29\u0185\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\5\2u\n\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\3\6\3}\n\3\r\3\16\3~\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0087\n\4"+
		"\f\4\16\4\u008a\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u0095\n\5"+
		"\f\5\16\5\u0098\13\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t"+
		"\6\t\u00b8\n\t\r\t\16\t\u00b9\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3"+
		"\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3"+
		"\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3"+
		"\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3"+
		"\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\7!\u0138\n!\f"+
		"!\16!\u013b\13!\3\"\3\"\7\"\u013f\n\"\f\"\16\"\u0142\13\"\3#\3#\7#\u0146"+
		"\n#\f#\16#\u0149\13#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3"+
		"+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63"+
		"\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\58\u017a\n8"+
		"\39\39\39\79\u017f\n9\f9\169\u0182\139\39\39\3\u0180\2:\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2q9\3\2\31\5"+
		"\2\13\f\16\17\"\"\3\2\f\f\5\2\f\f**,,\4\2EEee\4\2NNnn\4\2CCcc\4\2UUuu"+
		"\4\2HHhh\4\2KKkk\4\2PPpp\4\2JJjj\4\2GGgg\4\2TTtt\4\2VVvv\4\2XXxx\4\2Q"+
		"Qqq\4\2FFff\4\2RRrr\4\2YYyy\3\2C\\\6\2\62;C\\aac|\3\2c|\3\2\62;\2\u018e"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2"+
		"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3"+
		"\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2"+
		"\2\2q\3\2\2\2\3t\3\2\2\2\5|\3\2\2\2\7\u0082\3\2\2\2\t\u0090\3\2\2\2\13"+
		"\u009e\3\2\2\2\r\u00a6\3\2\2\2\17\u00ae\3\2\2\2\21\u00b7\3\2\2\2\23\u00c0"+
		"\3\2\2\2\25\u00c6\3\2\2\2\27\u00cc\3\2\2\2\31\u00d2\3\2\2\2\33\u00d8\3"+
		"\2\2\2\35\u00dd\3\2\2\2\37\u00e3\3\2\2\2!\u00e9\3\2\2\2#\u00ec\3\2\2\2"+
		"%\u00ef\3\2\2\2\'\u00f2\3\2\2\2)\u00fb\3\2\2\2+\u0102\3\2\2\2-\u0106\3"+
		"\2\2\2/\u010b\3\2\2\2\61\u0110\3\2\2\2\63\u0115\3\2\2\2\65\u011a\3\2\2"+
		"\2\67\u0120\3\2\2\29\u0125\3\2\2\2;\u012a\3\2\2\2=\u012e\3\2\2\2?\u0131"+
		"\3\2\2\2A\u0135\3\2\2\2C\u013c\3\2\2\2E\u0143\3\2\2\2G\u014a\3\2\2\2I"+
		"\u014c\3\2\2\2K\u014e\3\2\2\2M\u0150\3\2\2\2O\u0152\3\2\2\2Q\u0154\3\2"+
		"\2\2S\u0156\3\2\2\2U\u0159\3\2\2\2W\u015c\3\2\2\2Y\u015e\3\2\2\2[\u0160"+
		"\3\2\2\2]\u0162\3\2\2\2_\u0164\3\2\2\2a\u0166\3\2\2\2c\u0168\3\2\2\2e"+
		"\u016a\3\2\2\2g\u016c\3\2\2\2i\u016e\3\2\2\2k\u0171\3\2\2\2m\u0173\3\2"+
		"\2\2o\u0179\3\2\2\2q\u017b\3\2\2\2su\7\17\2\2ts\3\2\2\2tu\3\2\2\2uv\3"+
		"\2\2\2vw\7\f\2\2wx\b\2\2\2xy\3\2\2\2yz\b\2\3\2z\4\3\2\2\2{}\t\2\2\2|{"+
		"\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081"+
		"\b\3\3\2\u0081\6\3\2\2\2\u0082\u0083\7/\2\2\u0083\u0084\7/\2\2\u0084\u0088"+
		"\3\2\2\2\u0085\u0087\n\3\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088"+
		"\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0088\3\2"+
		"\2\2\u008b\u008c\7\f\2\2\u008c\u008d\b\4\4\2\u008d\u008e\3\2\2\2\u008e"+
		"\u008f\b\4\3\2\u008f\b\3\2\2\2\u0090\u0091\7/\2\2\u0091\u0092\7/\2\2\u0092"+
		"\u0096\3\2\2\2\u0093\u0095\n\3\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2"+
		"\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098"+
		"\u0096\3\2\2\2\u0099\u009a\7\2\2\3\u009a\u009b\b\5\5\2\u009b\u009c\3\2"+
		"\2\2\u009c\u009d\b\5\3\2\u009d\n\3\2\2\2\u009e\u009f\7*\2\2\u009f\u00a0"+
		"\7,\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\6\6\2\2\u00a2\u00a3\b\6\6\2\u00a3"+
		"\u00a4\3\2\2\2\u00a4\u00a5\b\6\3\2\u00a5\f\3\2\2\2\u00a6\u00a7\7*\2\2"+
		"\u00a7\u00a8\7,\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\6\7\3\2\u00aa\u00ab"+
		"\b\7\7\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\b\7\3\2\u00ad\16\3\2\2\2\u00ae"+
		"\u00af\7,\2\2\u00af\u00b0\7+\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\6\b\4"+
		"\2\u00b2\u00b3\b\b\b\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b\b\3\2\u00b5\20"+
		"\3\2\2\2\u00b6\u00b8\n\4\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9"+
		"\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\6\t"+
		"\5\2\u00bc\u00bd\b\t\t\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b\t\3\2\u00bf"+
		"\22\3\2\2\2\u00c0\u00c1\7*\2\2\u00c1\u00c2\6\n\6\2\u00c2\u00c3\b\n\n\2"+
		"\u00c3\u00c4\3\2\2\2\u00c4\u00c5\b\n\3\2\u00c5\24\3\2\2\2\u00c6\u00c7"+
		"\7,\2\2\u00c7\u00c8\6\13\7\2\u00c8\u00c9\b\13\13\2\u00c9\u00ca\3\2\2\2"+
		"\u00ca\u00cb\b\13\3\2\u00cb\26\3\2\2\2\u00cc\u00cd\7\f\2\2\u00cd\u00ce"+
		"\6\f\b\2\u00ce\u00cf\b\f\f\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\b\f\3\2\u00d1"+
		"\30\3\2\2\2\u00d2\u00d3\7,\2\2\u00d3\u00d4\7+\2\2\u00d4\u00d5\3\2\2\2"+
		"\u00d5\u00d6\6\r\t\2\u00d6\u00d7\b\r\r\2\u00d7\32\3\2\2\2\u00d8\u00d9"+
		"\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7g\2\2\u00dc"+
		"\34\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7n\2\2\u00e0"+
		"\u00e1\7u\2\2\u00e1\u00e2\7g\2\2\u00e2\36\3\2\2\2\u00e3\u00e4\t\5\2\2"+
		"\u00e4\u00e5\t\6\2\2\u00e5\u00e6\t\7\2\2\u00e6\u00e7\t\b\2\2\u00e7\u00e8"+
		"\t\b\2\2\u00e8 \3\2\2\2\u00e9\u00ea\t\t\2\2\u00ea\u00eb\t\n\2\2\u00eb"+
		"\"\3\2\2\2\u00ec\u00ed\t\n\2\2\u00ed\u00ee\t\t\2\2\u00ee$\3\2\2\2\u00ef"+
		"\u00f0\t\n\2\2\u00f0\u00f1\t\13\2\2\u00f1&\3\2\2\2\u00f2\u00f3\t\n\2\2"+
		"\u00f3\u00f4\t\13\2\2\u00f4\u00f5\t\f\2\2\u00f5\u00f6\t\r\2\2\u00f6\u00f7"+
		"\t\16\2\2\u00f7\u00f8\t\n\2\2\u00f8\u00f9\t\17\2\2\u00f9\u00fa\t\b\2\2"+
		"\u00fa(\3\2\2\2\u00fb\u00fc\t\n\2\2\u00fc\u00fd\t\b\2\2\u00fd\u00fe\t"+
		"\20\2\2\u00fe\u00ff\t\21\2\2\u00ff\u0100\t\n\2\2\u0100\u0101\t\22\2\2"+
		"\u0101*\3\2\2\2\u0102\u0103\t\6\2\2\u0103\u0104\t\r\2\2\u0104\u0105\t"+
		"\17\2\2\u0105,\3\2\2\2\u0106\u0107\t\6\2\2\u0107\u0108\t\21\2\2\u0108"+
		"\u0109\t\21\2\2\u0109\u010a\t\23\2\2\u010a.\3\2\2\2\u010b\u010c\t\23\2"+
		"\2\u010c\u010d\t\21\2\2\u010d\u010e\t\21\2\2\u010e\u010f\t\6\2\2\u010f"+
		"\60\3\2\2\2\u0110\u0111\t\17\2\2\u0111\u0112\t\f\2\2\u0112\u0113\t\r\2"+
		"\2\u0113\u0114\t\13\2\2\u0114\62\3\2\2\2\u0115\u0116\t\r\2\2\u0116\u0117"+
		"\t\6\2\2\u0117\u0118\t\b\2\2\u0118\u0119\t\r\2\2\u0119\64\3\2\2\2\u011a"+
		"\u011b\t\24\2\2\u011b\u011c\t\f\2\2\u011c\u011d\t\n\2\2\u011d\u011e\t"+
		"\6\2\2\u011e\u011f\t\r\2\2\u011f\66\3\2\2\2\u0120\u0121\t\5\2\2\u0121"+
		"\u0122\t\7\2\2\u0122\u0123\t\b\2\2\u0123\u0124\t\r\2\2\u01248\3\2\2\2"+
		"\u0125\u0126\t\r\2\2\u0126\u0127\t\b\2\2\u0127\u0128\t\7\2\2\u0128\u0129"+
		"\t\5\2\2\u0129:\3\2\2\2\u012a\u012b\t\13\2\2\u012b\u012c\t\r\2\2\u012c"+
		"\u012d\t\24\2\2\u012d<\3\2\2\2\u012e\u012f\t\21\2\2\u012f\u0130\t\t\2"+
		"\2\u0130>\3\2\2\2\u0131\u0132\t\13\2\2\u0132\u0133\t\21\2\2\u0133\u0134"+
		"\t\17\2\2\u0134@\3\2\2\2\u0135\u0139\t\25\2\2\u0136\u0138\t\26\2\2\u0137"+
		"\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2"+
		"\2\2\u013aB\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u0140\t\27\2\2\u013d\u013f"+
		"\t\26\2\2\u013e\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2"+
		"\u0140\u0141\3\2\2\2\u0141D\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0147\t"+
		"\30\2\2\u0144\u0146\t\30\2\2\u0145\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147"+
		"\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148F\3\2\2\2\u0149\u0147\3\2\2\2"+
		"\u014a\u014b\7*\2\2\u014bH\3\2\2\2\u014c\u014d\7+\2\2\u014dJ\3\2\2\2\u014e"+
		"\u014f\7}\2\2\u014fL\3\2\2\2\u0150\u0151\7\177\2\2\u0151N\3\2\2\2\u0152"+
		"\u0153\7=\2\2\u0153P\3\2\2\2\u0154\u0155\7<\2\2\u0155R\3\2\2\2\u0156\u0157"+
		"\7>\2\2\u0157\u0158\7/\2\2\u0158T\3\2\2\2\u0159\u015a\7?\2\2\u015a\u015b"+
		"\7@\2\2\u015bV\3\2\2\2\u015c\u015d\7\u0080\2\2\u015dX\3\2\2\2\u015e\u015f"+
		"\7.\2\2\u015fZ\3\2\2\2\u0160\u0161\7\60\2\2\u0161\\\3\2\2\2\u0162\u0163"+
		"\7B\2\2\u0163^\3\2\2\2\u0164\u0165\7,\2\2\u0165`\3\2\2\2\u0166\u0167\7"+
		"-\2\2\u0167b\3\2\2\2\u0168\u0169\7/\2\2\u0169d\3\2\2\2\u016a\u016b\7\61"+
		"\2\2\u016bf\3\2\2\2\u016c\u016d\7>\2\2\u016dh\3\2\2\2\u016e\u016f\7>\2"+
		"\2\u016f\u0170\7?\2\2\u0170j\3\2\2\2\u0171\u0172\7?\2\2\u0172l\3\2\2\2"+
		"\u0173\u0174\13\2\2\2\u0174n\3\2\2\2\u0175\u0176\7^\2\2\u0176\u017a\7"+
		"$\2\2\u0177\u0178\7^\2\2\u0178\u017a\7^\2\2\u0179\u0175\3\2\2\2\u0179"+
		"\u0177\3\2\2\2\u017ap\3\2\2\2\u017b\u0180\7$\2\2\u017c\u017f\5o8\2\u017d"+
		"\u017f\13\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3"+
		"\2\2\2\u0180\u0181\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0183\3\2\2\2\u0182"+
		"\u0180\3\2\2\2\u0183\u0184\7$\2\2\u0184r\3\2\2\2\16\2t~\u0088\u0096\u00b9"+
		"\u0139\u0140\u0147\u0179\u017e\u0180\16\3\2\2\b\2\2\3\4\3\3\5\4\3\6\5"+
		"\3\7\6\3\b\7\3\t\b\3\n\t\3\13\n\3\f\13\3\r\f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
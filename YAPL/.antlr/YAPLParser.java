// Generated from /home/roberto/Desktop/UVG2022C2/COMPILERS/compilers-project/YAPL/YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		CLASS=10, ELSE=11, FALSE=12, FI=13, IF=14, IN=15, INHERITS=16, ISVOID=17, 
		LET=18, LOOP=19, POOL=20, THEN=21, WHILE=22, CASE=23, ESAC=24, NEW=25, 
		OF=26, NOT=27, TRUE=28, STRING=29, INT=30, TYPEID=31, OBJECTID=32, ASSIGNMENT=33, 
		CASE_ARROW=34, ADD=35, MINUS=36, MULTIPLY=37, DIVISION=38, LESS_THAN=39, 
		LESS_EQUAL=40, EQUAL=41, INTEGER_NEGATIVE=42, OPEN_COMMENT=43, CLOSE_COMMENT=44, 
		COMMENT=45, ONE_LINE_COMMENT=46, WHITESPACE=47;
	public static final int
		RULE_program = 0, RULE_programBlocks = 1, RULE_classDefine = 2, RULE_feature = 3, 
		RULE_formal = 4, RULE_expression = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "programBlocks", "classDefine", "feature", "formal", "expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'@'", "'.'", 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "'<-'", 
			"'=>'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'='", "'~'", "'(*'", 
			"'*)'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "CLASS", 
			"ELSE", "FALSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LET", "LOOP", 
			"POOL", "THEN", "WHILE", "CASE", "ESAC", "NEW", "OF", "NOT", "TRUE", 
			"STRING", "INT", "TYPEID", "OBJECTID", "ASSIGNMENT", "CASE_ARROW", "ADD", 
			"MINUS", "MULTIPLY", "DIVISION", "LESS_THAN", "LESS_EQUAL", "EQUAL", 
			"INTEGER_NEGATIVE", "OPEN_COMMENT", "CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", 
			"WHITESPACE"
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

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramBlocksContext programBlocks() {
			return getRuleContext(ProgramBlocksContext.class,0);
		}
		public TerminalNode EOF() { return getToken(YAPLParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			programBlocks();
			setState(13);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgramBlocksContext extends ParserRuleContext {
		public ProgramBlocksContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programBlocks; }
	 
		public ProgramBlocksContext() { }
		public void copyFrom(ProgramBlocksContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ClassesContext extends ProgramBlocksContext {
		public ClassDefineContext classDefine() {
			return getRuleContext(ClassDefineContext.class,0);
		}
		public ProgramBlocksContext programBlocks() {
			return getRuleContext(ProgramBlocksContext.class,0);
		}
		public ClassesContext(ProgramBlocksContext ctx) { copyFrom(ctx); }
	}
	public static class EofContext extends ProgramBlocksContext {
		public TerminalNode EOF() { return getToken(YAPLParser.EOF, 0); }
		public EofContext(ProgramBlocksContext ctx) { copyFrom(ctx); }
	}

	public final ProgramBlocksContext programBlocks() throws RecognitionException {
		ProgramBlocksContext _localctx = new ProgramBlocksContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programBlocks);
		try {
			setState(20);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLASS:
				_localctx = new ClassesContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				classDefine();
				setState(16);
				match(T__0);
				setState(17);
				programBlocks();
				}
				break;
			case EOF:
				_localctx = new EofContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				match(EOF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDefineContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(YAPLParser.CLASS, 0); }
		public List<TerminalNode> TYPEID() { return getTokens(YAPLParser.TYPEID); }
		public TerminalNode TYPEID(int i) {
			return getToken(YAPLParser.TYPEID, i);
		}
		public TerminalNode INHERITS() { return getToken(YAPLParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public ClassDefineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDefine; }
	}

	public final ClassDefineContext classDefine() throws RecognitionException {
		ClassDefineContext _localctx = new ClassDefineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_classDefine);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(CLASS);
			setState(23);
			match(TYPEID);
			setState(26);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(24);
				match(INHERITS);
				setState(25);
				match(TYPEID);
				}
			}

			setState(28);
			match(T__1);
			setState(34);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OBJECTID) {
				{
				{
				setState(29);
				feature();
				setState(30);
				match(T__0);
				}
				}
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(37);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	 
		public FeatureContext() { }
		public void copyFrom(FeatureContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MethodContext extends FeatureContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public MethodContext(FeatureContext ctx) { copyFrom(ctx); }
	}
	public static class PropertyContext extends FeatureContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public PropertyContext(FeatureContext ctx) { copyFrom(ctx); }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_feature);
		int _la;
		try {
			setState(65);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				_localctx = new MethodContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(OBJECTID);
				setState(40);
				match(T__3);
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OBJECTID) {
					{
					setState(41);
					formal();
					setState(46);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(42);
						match(T__4);
						setState(43);
						formal();
						}
						}
						setState(48);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(51);
				match(T__5);
				setState(52);
				match(T__6);
				setState(53);
				match(TYPEID);
				setState(54);
				match(T__1);
				setState(55);
				expression(0);
				setState(56);
				match(T__2);
				}
				break;
			case 2:
				_localctx = new PropertyContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(58);
				match(OBJECTID);
				setState(59);
				match(T__6);
				setState(60);
				match(TYPEID);
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGNMENT) {
					{
					setState(61);
					match(ASSIGNMENT);
					setState(62);
					expression(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(OBJECTID);
			setState(68);
			match(T__6);
			setState(69);
			match(TYPEID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LetInContext extends ExpressionContext {
		public TerminalNode LET() { return getToken(YAPLParser.LET, 0); }
		public List<TerminalNode> OBJECTID() { return getTokens(YAPLParser.OBJECTID); }
		public TerminalNode OBJECTID(int i) {
			return getToken(YAPLParser.OBJECTID, i);
		}
		public List<TerminalNode> TYPEID() { return getTokens(YAPLParser.TYPEID); }
		public TerminalNode TYPEID(int i) {
			return getToken(YAPLParser.TYPEID, i);
		}
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> ASSIGNMENT() { return getTokens(YAPLParser.ASSIGNMENT); }
		public TerminalNode ASSIGNMENT(int i) {
			return getToken(YAPLParser.ASSIGNMENT, i);
		}
		public LetInContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MinusContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(YAPLParser.MINUS, 0); }
		public MinusContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class StringContext extends ExpressionContext {
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public StringContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IsvoidContext extends ExpressionContext {
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IsvoidContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class WhileContext extends ExpressionContext {
		public TerminalNode WHILE() { return getToken(YAPLParser.WHILE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LOOP() { return getToken(YAPLParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YAPLParser.POOL, 0); }
		public WhileContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class DivisionContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode DIVISION() { return getToken(YAPLParser.DIVISION, 0); }
		public DivisionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NegativeContext extends ExpressionContext {
		public TerminalNode INTEGER_NEGATIVE() { return getToken(YAPLParser.INTEGER_NEGATIVE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NegativeContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class BoolNotContext extends ExpressionContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BoolNotContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LessThanContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LESS_THAN() { return getToken(YAPLParser.LESS_THAN, 0); }
		public LessThanContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class BlockContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BlockContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExpressionContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public IdContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MultiplyContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MULTIPLY() { return getToken(YAPLParser.MULTIPLY, 0); }
		public MultiplyContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IfContext extends ExpressionContext {
		public TerminalNode IF() { return getToken(YAPLParser.IF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode THEN() { return getToken(YAPLParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YAPLParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YAPLParser.FI, 0); }
		public IfContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CaseContext extends ExpressionContext {
		public TerminalNode CASE() { return getToken(YAPLParser.CASE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OF() { return getToken(YAPLParser.OF, 0); }
		public TerminalNode ESAC() { return getToken(YAPLParser.ESAC, 0); }
		public List<TerminalNode> OBJECTID() { return getTokens(YAPLParser.OBJECTID); }
		public TerminalNode OBJECTID(int i) {
			return getToken(YAPLParser.OBJECTID, i);
		}
		public List<TerminalNode> TYPEID() { return getTokens(YAPLParser.TYPEID); }
		public TerminalNode TYPEID(int i) {
			return getToken(YAPLParser.TYPEID, i);
		}
		public List<TerminalNode> CASE_ARROW() { return getTokens(YAPLParser.CASE_ARROW); }
		public TerminalNode CASE_ARROW(int i) {
			return getToken(YAPLParser.CASE_ARROW, i);
		}
		public CaseContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class OwnMethodCallContext extends ExpressionContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public OwnMethodCallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AddContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ADD() { return getToken(YAPLParser.ADD, 0); }
		public AddContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NewContext extends ExpressionContext {
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public NewContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ParenthesesContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParenthesesContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AssignmentContext extends ExpressionContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class FalseContext extends ExpressionContext {
		public TerminalNode FALSE() { return getToken(YAPLParser.FALSE, 0); }
		public FalseContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends ExpressionContext {
		public TerminalNode INT() { return getToken(YAPLParser.INT, 0); }
		public IntContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class EqualContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQUAL() { return getToken(YAPLParser.EQUAL, 0); }
		public EqualContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class TrueContext extends ExpressionContext {
		public TerminalNode TRUE() { return getToken(YAPLParser.TRUE, 0); }
		public TrueContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LessEqualContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LESS_EQUAL() { return getToken(YAPLParser.LESS_EQUAL, 0); }
		public LessEqualContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MethodCallContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public MethodCallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				_localctx = new OwnMethodCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(72);
				match(OBJECTID);
				setState(73);
				match(T__3);
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << FALSE) | (1L << IF) | (1L << ISVOID) | (1L << LET) | (1L << WHILE) | (1L << CASE) | (1L << NEW) | (1L << NOT) | (1L << TRUE) | (1L << STRING) | (1L << INT) | (1L << OBJECTID) | (1L << INTEGER_NEGATIVE))) != 0)) {
					{
					setState(74);
					expression(0);
					setState(79);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(75);
						match(T__4);
						setState(76);
						expression(0);
						}
						}
						setState(81);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(84);
				match(T__5);
				}
				break;
			case 2:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(85);
				match(IF);
				setState(86);
				expression(0);
				setState(87);
				match(THEN);
				setState(88);
				expression(0);
				setState(89);
				match(ELSE);
				setState(90);
				expression(0);
				setState(91);
				match(FI);
				}
				break;
			case 3:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(93);
				match(WHILE);
				setState(94);
				expression(0);
				setState(95);
				match(LOOP);
				setState(96);
				expression(0);
				setState(97);
				match(POOL);
				}
				break;
			case 4:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(99);
				match(T__1);
				setState(103); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(100);
					expression(0);
					setState(101);
					match(T__0);
					}
					}
					setState(105); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << FALSE) | (1L << IF) | (1L << ISVOID) | (1L << LET) | (1L << WHILE) | (1L << CASE) | (1L << NEW) | (1L << NOT) | (1L << TRUE) | (1L << STRING) | (1L << INT) | (1L << OBJECTID) | (1L << INTEGER_NEGATIVE))) != 0) );
				setState(107);
				match(T__2);
				}
				break;
			case 5:
				{
				_localctx = new LetInContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(109);
				match(LET);
				setState(110);
				match(OBJECTID);
				setState(111);
				match(T__6);
				setState(112);
				match(TYPEID);
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGNMENT) {
					{
					setState(113);
					match(ASSIGNMENT);
					setState(114);
					expression(0);
					}
				}

				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(117);
					match(T__4);
					setState(118);
					match(OBJECTID);
					setState(119);
					match(T__6);
					setState(120);
					match(TYPEID);
					setState(123);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==ASSIGNMENT) {
						{
						setState(121);
						match(ASSIGNMENT);
						setState(122);
						expression(0);
						}
					}

					}
					}
					setState(129);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(130);
				match(IN);
				setState(131);
				expression(20);
				}
				break;
			case 6:
				{
				_localctx = new CaseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(132);
				match(CASE);
				setState(133);
				expression(0);
				setState(134);
				match(OF);
				setState(142); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(135);
					match(OBJECTID);
					setState(136);
					match(T__6);
					setState(137);
					match(TYPEID);
					setState(138);
					match(CASE_ARROW);
					setState(139);
					expression(0);
					setState(140);
					match(T__0);
					}
					}
					setState(144); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==OBJECTID );
				setState(146);
				match(ESAC);
				}
				break;
			case 7:
				{
				_localctx = new NewContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(148);
				match(NEW);
				setState(149);
				match(TYPEID);
				}
				break;
			case 8:
				{
				_localctx = new NegativeContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(150);
				match(INTEGER_NEGATIVE);
				setState(151);
				expression(17);
				}
				break;
			case 9:
				{
				_localctx = new IsvoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(152);
				match(ISVOID);
				setState(153);
				expression(16);
				}
				break;
			case 10:
				{
				_localctx = new BoolNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(154);
				match(NOT);
				setState(155);
				expression(8);
				}
				break;
			case 11:
				{
				_localctx = new ParenthesesContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(156);
				match(T__3);
				setState(157);
				expression(0);
				setState(158);
				match(T__5);
				}
				break;
			case 12:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(160);
				match(OBJECTID);
				}
				break;
			case 13:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(161);
				match(INT);
				}
				break;
			case 14:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(162);
				match(STRING);
				}
				break;
			case 15:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(163);
				match(TRUE);
				}
				break;
			case 16:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(164);
				match(FALSE);
				}
				break;
			case 17:
				{
				_localctx = new AssignmentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(165);
				match(OBJECTID);
				setState(166);
				match(ASSIGNMENT);
				setState(167);
				expression(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(212);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(210);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new MultiplyContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(170);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(171);
						match(MULTIPLY);
						setState(172);
						expression(16);
						}
						break;
					case 2:
						{
						_localctx = new DivisionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(173);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(174);
						match(DIVISION);
						setState(175);
						expression(15);
						}
						break;
					case 3:
						{
						_localctx = new AddContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(176);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(177);
						match(ADD);
						setState(178);
						expression(14);
						}
						break;
					case 4:
						{
						_localctx = new MinusContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(179);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(180);
						match(MINUS);
						setState(181);
						expression(13);
						}
						break;
					case 5:
						{
						_localctx = new LessThanContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(182);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(183);
						match(LESS_THAN);
						setState(184);
						expression(12);
						}
						break;
					case 6:
						{
						_localctx = new LessEqualContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(185);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(186);
						match(LESS_EQUAL);
						setState(187);
						expression(11);
						}
						break;
					case 7:
						{
						_localctx = new EqualContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(188);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(189);
						match(EQUAL);
						setState(190);
						expression(10);
						}
						break;
					case 8:
						{
						_localctx = new MethodCallContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(191);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(194);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__7) {
							{
							setState(192);
							match(T__7);
							setState(193);
							match(TYPEID);
							}
						}

						setState(196);
						match(T__8);
						setState(197);
						match(OBJECTID);
						setState(198);
						match(T__3);
						setState(207);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << FALSE) | (1L << IF) | (1L << ISVOID) | (1L << LET) | (1L << WHILE) | (1L << CASE) | (1L << NEW) | (1L << NOT) | (1L << TRUE) | (1L << STRING) | (1L << INT) | (1L << OBJECTID) | (1L << INTEGER_NEGATIVE))) != 0)) {
							{
							setState(199);
							expression(0);
							setState(204);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__4) {
								{
								{
								setState(200);
								match(T__4);
								setState(201);
								expression(0);
								}
								}
								setState(206);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(209);
						match(T__5);
						}
						break;
					}
					} 
				}
				setState(214);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 5:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 10);
		case 6:
			return precpred(_ctx, 9);
		case 7:
			return precpred(_ctx, 25);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61\u00da\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3"+
		"\3\5\3\27\n\3\3\4\3\4\3\4\3\4\5\4\35\n\4\3\4\3\4\3\4\3\4\7\4#\n\4\f\4"+
		"\16\4&\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62\13\5\5\5"+
		"\64\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5B\n\5\5\5D"+
		"\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7P\n\7\f\7\16\7S\13\7\5"+
		"\7U\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\6\7j\n\7\r\7\16\7k\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7"+
		"v\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7~\n\7\7\7\u0080\n\7\f\7\16\7\u0083\13"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7\u0091\n\7\r\7\16"+
		"\7\u0092\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ab\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7"+
		"\u00c5\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00cd\n\7\f\7\16\7\u00d0\13\7\5"+
		"\7\u00d2\n\7\3\7\7\7\u00d5\n\7\f\7\16\7\u00d8\13\7\3\7\2\3\f\b\2\4\6\b"+
		"\n\f\2\2\2\u00fc\2\16\3\2\2\2\4\26\3\2\2\2\6\30\3\2\2\2\bC\3\2\2\2\nE"+
		"\3\2\2\2\f\u00aa\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22"+
		"\5\6\4\2\22\23\7\3\2\2\23\24\5\4\3\2\24\27\3\2\2\2\25\27\7\2\2\3\26\21"+
		"\3\2\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31\7\f\2\2\31\34\7!\2\2\32\33\7"+
		"\22\2\2\33\35\7!\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36$\7\4"+
		"\2\2\37 \5\b\5\2 !\7\3\2\2!#\3\2\2\2\"\37\3\2\2\2#&\3\2\2\2$\"\3\2\2\2"+
		"$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7\5\2\2(\7\3\2\2\2)*\7\"\2\2*\63\7"+
		"\6\2\2+\60\5\n\6\2,-\7\7\2\2-/\5\n\6\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2"+
		"\2\60\61\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\63+\3\2\2\2\63\64\3\2\2\2"+
		"\64\65\3\2\2\2\65\66\7\b\2\2\66\67\7\t\2\2\678\7!\2\289\7\4\2\29:\5\f"+
		"\7\2:;\7\5\2\2;D\3\2\2\2<=\7\"\2\2=>\7\t\2\2>A\7!\2\2?@\7#\2\2@B\5\f\7"+
		"\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2C)\3\2\2\2C<\3\2\2\2D\t\3\2\2\2EF\7\""+
		"\2\2FG\7\t\2\2GH\7!\2\2H\13\3\2\2\2IJ\b\7\1\2JK\7\"\2\2KT\7\6\2\2LQ\5"+
		"\f\7\2MN\7\7\2\2NP\5\f\7\2OM\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RU\3"+
		"\2\2\2SQ\3\2\2\2TL\3\2\2\2TU\3\2\2\2UV\3\2\2\2V\u00ab\7\b\2\2WX\7\20\2"+
		"\2XY\5\f\7\2YZ\7\27\2\2Z[\5\f\7\2[\\\7\r\2\2\\]\5\f\7\2]^\7\17\2\2^\u00ab"+
		"\3\2\2\2_`\7\30\2\2`a\5\f\7\2ab\7\25\2\2bc\5\f\7\2cd\7\26\2\2d\u00ab\3"+
		"\2\2\2ei\7\4\2\2fg\5\f\7\2gh\7\3\2\2hj\3\2\2\2if\3\2\2\2jk\3\2\2\2ki\3"+
		"\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\5\2\2n\u00ab\3\2\2\2op\7\24\2\2pq\7\"\2"+
		"\2qr\7\t\2\2ru\7!\2\2st\7#\2\2tv\5\f\7\2us\3\2\2\2uv\3\2\2\2v\u0081\3"+
		"\2\2\2wx\7\7\2\2xy\7\"\2\2yz\7\t\2\2z}\7!\2\2{|\7#\2\2|~\5\f\7\2}{\3\2"+
		"\2\2}~\3\2\2\2~\u0080\3\2\2\2\177w\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177"+
		"\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084"+
		"\u0085\7\21\2\2\u0085\u00ab\5\f\7\26\u0086\u0087\7\31\2\2\u0087\u0088"+
		"\5\f\7\2\u0088\u0090\7\34\2\2\u0089\u008a\7\"\2\2\u008a\u008b\7\t\2\2"+
		"\u008b\u008c\7!\2\2\u008c\u008d\7$\2\2\u008d\u008e\5\f\7\2\u008e\u008f"+
		"\7\3\2\2\u008f\u0091\3\2\2\2\u0090\u0089\3\2\2\2\u0091\u0092\3\2\2\2\u0092"+
		"\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7\32"+
		"\2\2\u0095\u00ab\3\2\2\2\u0096\u0097\7\33\2\2\u0097\u00ab\7!\2\2\u0098"+
		"\u0099\7,\2\2\u0099\u00ab\5\f\7\23\u009a\u009b\7\23\2\2\u009b\u00ab\5"+
		"\f\7\22\u009c\u009d\7\35\2\2\u009d\u00ab\5\f\7\n\u009e\u009f\7\6\2\2\u009f"+
		"\u00a0\5\f\7\2\u00a0\u00a1\7\b\2\2\u00a1\u00ab\3\2\2\2\u00a2\u00ab\7\""+
		"\2\2\u00a3\u00ab\7 \2\2\u00a4\u00ab\7\37\2\2\u00a5\u00ab\7\36\2\2\u00a6"+
		"\u00ab\7\16\2\2\u00a7\u00a8\7\"\2\2\u00a8\u00a9\7#\2\2\u00a9\u00ab\5\f"+
		"\7\3\u00aaI\3\2\2\2\u00aaW\3\2\2\2\u00aa_\3\2\2\2\u00aae\3\2\2\2\u00aa"+
		"o\3\2\2\2\u00aa\u0086\3\2\2\2\u00aa\u0096\3\2\2\2\u00aa\u0098\3\2\2\2"+
		"\u00aa\u009a\3\2\2\2\u00aa\u009c\3\2\2\2\u00aa\u009e\3\2\2\2\u00aa\u00a2"+
		"\3\2\2\2\u00aa\u00a3\3\2\2\2\u00aa\u00a4\3\2\2\2\u00aa\u00a5\3\2\2\2\u00aa"+
		"\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2\u00ab\u00d6\3\2\2\2\u00ac\u00ad\f\21"+
		"\2\2\u00ad\u00ae\7\'\2\2\u00ae\u00d5\5\f\7\22\u00af\u00b0\f\20\2\2\u00b0"+
		"\u00b1\7(\2\2\u00b1\u00d5\5\f\7\21\u00b2\u00b3\f\17\2\2\u00b3\u00b4\7"+
		"%\2\2\u00b4\u00d5\5\f\7\20\u00b5\u00b6\f\16\2\2\u00b6\u00b7\7&\2\2\u00b7"+
		"\u00d5\5\f\7\17\u00b8\u00b9\f\r\2\2\u00b9\u00ba\7)\2\2\u00ba\u00d5\5\f"+
		"\7\16\u00bb\u00bc\f\f\2\2\u00bc\u00bd\7*\2\2\u00bd\u00d5\5\f\7\r\u00be"+
		"\u00bf\f\13\2\2\u00bf\u00c0\7+\2\2\u00c0\u00d5\5\f\7\f\u00c1\u00c4\f\33"+
		"\2\2\u00c2\u00c3\7\n\2\2\u00c3\u00c5\7!\2\2\u00c4\u00c2\3\2\2\2\u00c4"+
		"\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\7\13\2\2\u00c7\u00c8\7"+
		"\"\2\2\u00c8\u00d1\7\6\2\2\u00c9\u00ce\5\f\7\2\u00ca\u00cb\7\7\2\2\u00cb"+
		"\u00cd\5\f\7\2\u00cc\u00ca\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2"+
		"\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1"+
		"\u00c9\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\7\b"+
		"\2\2\u00d4\u00ac\3\2\2\2\u00d4\u00af\3\2\2\2\u00d4\u00b2\3\2\2\2\u00d4"+
		"\u00b5\3\2\2\2\u00d4\u00b8\3\2\2\2\u00d4\u00bb\3\2\2\2\u00d4\u00be\3\2"+
		"\2\2\u00d4\u00c1\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6"+
		"\u00d7\3\2\2\2\u00d7\r\3\2\2\2\u00d8\u00d6\3\2\2\2\26\26\34$\60\63ACQ"+
		"Tku}\u0081\u0092\u00aa\u00c4\u00ce\u00d1\u00d4\u00d6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
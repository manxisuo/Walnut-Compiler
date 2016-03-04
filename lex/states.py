# -*- coding: UTF-8 -*-
import re

from lex import tokens

PUNC_PRE_1 = ['{', '}', '(', ')', '[', ']', '.', ';', ',', '<', '>', '=', '!', '+', '-', '*', '%', '&', '|', '^', '~', '?', ':']
PUNC_PRE_2 = ['<=', '>=', '==', '!=', '++', '--', '<<', '>>', '&&', '||', '+=', '-=', '*=', '%=', '&=', '|=', '^=']
PUNC_PRE_3 = ['===', '!==', '>>>', '<<=', '>>=']
PUNC_PRE_4 = ['>>>=']

def newState(c):
    for checker in stateCheckers:
        if checker['fn'](c):
            return checker['state'](c)
    return Empty()

# DFA的状态
class State:
    pass

# 空状态。不会生成token。
class Empty(State):
    def read(self, c):
        return newState(c)

    def toToken(self):
        return None

# 关键字(26个)
KEYWORDS = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally', 'for', 'function',
    'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try', 'typeof', 'var', 'void', 'while', 'with']

# 未来保留字(7个)
RESERVED_WORDS = ['class', 'const', 'enum', 'export', 'extends', 'import', 'super']

class ID(State):
    def __init__(self, start):
        self.val = start

    def read(self, c):
        if re.match('[a-zA-Z0-9$_]', c):
            self.val += c
            return self
        else:
            return newState(c)

    def toToken(self):
        if self.val in KEYWORDS or self.val in RESERVED_WORDS:
            return tokens.KeyWord(self.val)
        else:
            return tokens.ID(self.val)

class Number(State):
    def __init__(self, start):
        self.val = start

    def read(self, c):
        if re.match('[a-zA-Z0-9$_]', c):
            self.val += c
            return self
        else:
            return newState(c)

    def toToken(self):
        return tokens.Number(self.val)

# 转移字符映射关系
ESCAPE_MAP = {
    '\'': '\'',
    '"': '"',
    '\\': '\\',
    'n': '\n',
    'r': '\r',
    't': '\t',
    'b': '\b',
    'f': '\f'
}

class String(State):
    def __init__(self, start):
        self.wrapper = start
        self.val = ''
        self.escape = False

    def read(self, c):
        if self.escape:
            if c in ESCAPE_MAP:
                self.val += ESCAPE_MAP[c]
                self.escape = False
                return self
            else:
                raise Exception('不合法的字符串')
        else:
            if c == '\\':
                self.escape = True
                return self

            if c == self.wrapper:
                return Empty()
            else:
                self.val += c
                return self

    def toToken(self):
        return tokens.String(self.val)

# 标点符号到Token的映射。共48个。
PUNCTUATOR_TOKEN_MAP = {
    '{': tokens.OpenCurly(),
    '}': tokens.CloseCurly(),
    '(': tokens.OpenParen(),
    ')': tokens.CloseParen(),
    '[': tokens.OpenBracket(),
    ']': tokens.CloseBracket(),
    '<=': tokens.LessEqual(),
    '.': tokens.Dot(),
    ';': tokens.SemiColon(),
    ',': tokens.Comma(),
    '<': tokens.Less(),
    '>': tokens.More(),
    '>=': tokens.MoreEqual(),
    '==': tokens.Equal(),
    '!=': tokens.NotEqual(),
    '===': tokens.StrictEqual(),
    '!==': tokens.StrictNotEqual(),
    '+': tokens.Plus(),
    '-': tokens.Minus(),
    '*': tokens.Multiply(),
    '%': tokens.Percent(),
    '++': tokens.Increment(),
    '--': tokens.Decrement(),
    '<<': tokens.LeftShift(),
    '>>': tokens.RightShift(),
    '>>>': tokens.UnsignedRightShift(),
    '&': tokens.Ampersand(),
    '|': tokens.VerticalBar(),
    '^': tokens.Caret(),
    '!': tokens.Exclamation(),
    '~': tokens.Tilde(),
    '&&': tokens.And(),
    '||': tokens.Or(),
    '?': tokens.Question(),
    ':': tokens.Colon(),
    '=': tokens.Assign(),
    '+=': tokens.PlusAssign(),
    '-=': tokens.MinusAssign(),
    '*=': tokens.MultiplyAssign(),
    '%=': tokens.PercentAssign(),
    '<<=': tokens.LeftShiftAssign(),
    '>>=': tokens.RightShiftAssign(),
    '>>>=': tokens.UnsignedRightShiftAssign(),
    '&=': tokens.AmpersandAssign(),
    '|=': tokens.VerticalBarAssign(),
    '^=': tokens.CaretAssign()
    #'/': tokens.Divide(),
    #'/=': tokens.DivideAssign()
}

# 状态：标点符号(包括注释)
class Punctuator(State):
    def __init__(self, start):
        self.val = start

    def read(self, c):
        length = len(self.val)
        if length == 1:
            if self.val + c in PUNC_PRE_2:
                self.val += c
                return self

        elif length == 2:
            if self.val + c in PUNC_PRE_3:
                self.val += c
                return self
        elif length == 3:
            if self.val + c in PUNC_PRE_4:
                self.val += c
                return self
        return newState(c)

    def toToken(self):
        if self.val in PUNCTUATOR_TOKEN_MAP:
            return PUNCTUATOR_TOKEN_MAP[self.val]
        else:
            raise Exception('词法错误')

class SlashMode(State):
    def __init__(self, start):
        self.firstFlag = True
        self.token = None
        self.singleComment = False
        self.starFlag = False

    def read(self, c):
        if self.firstFlag:
            self.firstFlag = False
            if c == '=':
                self.token = tokens.DivideAssign()
                return Empty()
            elif c == '/':
                self.singleComment = True
                self.token = tokens.Comment()
                return self
            elif c == '*':
                self.token = tokens.Comment()
                return self
            else:
                self.token = tokens.Divide()
                return newState(c)
        else:
            if self.singleComment:
                if c == '\r' or c == '\n':
                    return LineTerminator()
            elif c == '*':
                self.starFlag = True
            elif c == '/' and self.starFlag:
                return Empty()
            else:
                self.starFlag = False
            return self

    def toToken(self):
        return self.token

class LineTerminator(State):
    def __init__(self, start=None):
        pass

    def read(self, c):
        return newState(c)

    def toToken(self):
        return tokens.LT()

stateCheckers = [{
    'state': ID,
    'fn': lambda c : re.match('[a-zA-Z$_]', c)
}, {
    'state': Number,
    'fn': lambda c : re.match('[0-9]', c)
}, {
    'state': String,
    'fn': lambda c : c == '"' or c == '\''
}, {
    'state': Punctuator,
    'fn': lambda c : c in PUNC_PRE_1
}, {
    'state': SlashMode,
    'fn': lambda c : c == '/'
}, {
    'state': LineTerminator,
    'fn': lambda c : c == '\r' or c == '\n'
}]

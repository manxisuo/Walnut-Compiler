# -*- coding: UTF-8 -*-
class Token:
    pass

# 标识符(变量名、函数名等)。
class ID(Token):
    def __init__(self, val):
        self.val = val

# 关键字。暂时使用同一个类表示。
class KeyWord(Token):
    def __init__(self, val):
        self.val = val

# 数字字面量。
class Number(Token):
    def __init__(self, val):
        self.val = val

# 字符串字面量。
class String(Token):
    def __init__(self, val):
        self.val = val

class OpenCurly(Token):
    def __init__(self):
        self.val = '{'

class CloseCurly(Token):
    def __init__(self):
        self.val = '}'

class OpenParen(Token):
    def __init__(self):
        self.val = '('

class CloseParen(Token):
    def __init__(self):
        self.val = ')'

class OpenBracket(Token):
    def __init__(self):
        self.val = '['

class CloseBracket(Token):
    def __init__(self):
        self.val = ']'

class LessEqual(Token):
    def __init__(self):
        self.val = '<='

class Dot(Token):
    def __init__(self):
        self.val = '.'

class SemiColon(Token):
    def __init__(self):
        self.val = ';'

class Comma(Token):
    def __init__(self):
        self.val = ','

class Less(Token):
    def __init__(self):
        self.val = '<'

class More(Token):
    def __init__(self):
        self.val = '>'

class MoreEqual(Token):
    def __init__(self):
        self.val = '>='

class Equal(Token):
    def __init__(self):
        self.val = '=='

class NotEqual(Token):
    def __init__(self):
        self.val = '!='

class StrictEqual(Token):
    def __init__(self):
        self.val = '==='

class StrictNotEqual(Token):
    def __init__(self):
        self.val = '!=='

class Plus(Token):
    def __init__(self):
        self.val = '+'

class Minus(Token):
    def __init__(self):
        self.val = '-'

class Multiply(Token):
    def __init__(self):
        self.val = '*'

class Percent(Token):
    def __init__(self):
        self.val = '%'

class Increment(Token):
    def __init__(self):
        self.val = '++'

class Decrement(Token):
    def __init__(self):
        self.val = '--'

class LeftShift(Token):
    def __init__(self):
        self.val = '<<'

class RightShift(Token):
    def __init__(self):
        self.val = '>>'

class UnsignedRightShift(Token):
    def __init__(self):
        self.val = '>>>'

class Ampersand(Token):
    def __init__(self):
        self.val = '&'

class VerticalBar(Token):
    def __init__(self):
        self.val = '|'

class Caret(Token):
    def __init__(self):
        self.val = '^'

class Exclamation(Token):
    def __init__(self):
        self.val = '!'

class Tilde(Token):
    def __init__(self):
        self.val = '~'

class And(Token):
    def __init__(self):
        self.val = '&&'

class Or(Token):
    def __init__(self):
        self.val = '||'

class Question(Token):
    def __init__(self):
        self.val = '?'

class Colon(Token):
    def __init__(self):
        self.val = ':'

class Assign(Token):
    def __init__(self):
        self.val = '='

class PlusAssign(Token):
    def __init__(self):
        self.val = '+='

class MinusAssign(Token):
    def __init__(self):
        self.val = '-='

class MultiplyAssign(Token):
    def __init__(self):
        self.val = '*='

class PercentAssign(Token):
    def __init__(self):
        self.val = '%='

class LeftShiftAssign(Token):
    def __init__(self):
        self.val = '<<='

class RightShiftAssign(Token):
    def __init__(self):
        self.val = '>>='

class UnsignedRightShiftAssign(Token):
    def __init__(self):
        self.val = '>>>='

class AmpersandAssign(Token):
    def __init__(self):
        self.val = '&='

class VerticalBarAssign(Token):
    def __init__(self):
        self.val = '|='

class CaretAssign(Token):
    def __init__(self):
        self.val = '^='

class Divide(Token):
    def __init__(self):
        self.val = '/'

class DivideAssign(Token):
    def __init__(self):
        self.val = '/='

# TODO
# 行终结符(\n或\r\n或其他)
class LT(Token):
    def __init__(self):
        self.val = '[LT]'

# 文件终结符(EOF)
class EOF(Token):
    def __init__(self):
        self.val = '[EOF]'

# 注释
class Comment(Token):
    def __init__(self):
        self.val = '[Comment]'

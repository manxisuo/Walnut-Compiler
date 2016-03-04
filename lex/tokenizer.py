# -*- coding: UTF-8 -*-
from lex import states

class Stream:
    '''表示源文件中的字符流'''

    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.cur = 0

    def nextChar(self):
        '''
        获取字符流中的下一个字符。
        当没有可用字符时，返回None。
        '''

        if self.cur >= self.length:
            return None
        else:
            c = self.data[self.cur]
            self.cur += 1
            return c

    def rollback(self):
        '''回滚一个字符'''

        if self.cur > 0:
            self.cur -= 1

def parse(file_path):
    '''解析给定的源文件，返回token列表。'''

    data = open(file_path).read()
    stream = Stream(data)
    curState = states.Empty()
    tokens = []

    c = stream.nextChar()
    while(c):
        nextState = curState.read(c)
        if nextState is not curState:
            token = curState.toToken()
            if token:
                tokens.append(token)
            curState = nextState
        c = stream.nextChar()

    tokens.append(curState.toToken())

    return tokens

import sys
from Word import Word
import Tag
from Token import Token
from Integer import Integer
from Word import Word
from Real import Real
from CharacterString import CharacterString
class Lexer:

    def reserve(self,w):
        self.words[w.getLexeme()] = w

    def __init__(self, filename):
        self.words = {}
        self.peek = ''
        self.input = open(filename, "r")



        self.reserve(Word("program",Tag.PROGRAM))
        self.reserve(Word("constante",Tag.CONSTANT))
        self.reserve(Word("var",Tag.VAR))
        self.reserve(Word("begin",Tag.BEGIN))
        self.reserve(Word("end",Tag.END))
        self.reserve(Word("integer",Tag.INTEGER))
        self.reserve(Word("real",Tag.REAL))
        self.reserve(Word("boolean",Tag.BOOLEAN))
        self.reserve(Word("string",Tag.STRING))
        self.reserve(Word("writeln",Tag.WRITELN))
        self.reserve(Word("readln",Tag.READLN))
        self.reserve(Word("while",Tag.WHILE))
        self.reserve(Word("do",Tag.DO))
        self.reserve(Word("repeat",Tag.REPEAT))
        self.reserve(Word("until",Tag.UNTIL))
        self.reserve(Word("for",Tag.FOR))
        self.reserve(Word("to",Tag.TO))
        self.reserve(Word("downto",Tag.DOWNTO))
        self.reserve(Word("if",Tag.IF))
        self.reserve(Word("then",Tag.THEN))
        self.reserve(Word("else",Tag.ELSE))
        self.reserve(Word("not",Tag.NOT))
        self.reserve(Word("div",Tag.DIV))
        self.reserve(Word("mod",Tag.MOD))
        self.reserve(Word("and",Tag.AND))
        self.reserve(Word("or",Tag.OR))


    def readch(self):
        self.peek = self.input.read(1)

    def readchargs(self,c):
        readch()
        if(self.peek != c):
            return false
        return true

    def peek_char(self):
        pos = self.input.tell()
        peekchar = self.input.read(1)
        self.input.seek(pos)
        return peekchar

    def skipWhiteSpaces(self):
        if not self.peek.isspace():
            return
        while self.peek.isspace():
            self.peek = self.input.read(1)

    def readCharacterString(self):
        cs = "" + self.peek
        self.peek = self.input.read(1)
        while self.peek != '"':
            cs += self.peek
            self.peek = self.input.read(1)
        cs += self.peek
        return CharacterString(cs)

    def readComments(self):
        self.peek = self.input.read(1)
        while not (self.peek == '*' and self.peek_char() == ')'):
            self.peek = self.input.read(1)
        self.peek = self.input.read(1)
        return Token(Tag.COMMENT)

    def scan(self):

        self.peek = self.input.read(1)
        self.skipWhiteSpaces()



        if self.peek == '(':
            if self.peek_char() == '*':
                self.peek = self.input.read(1)
                return self.readComments()
            return Token(Tag.LP)


        if self.peek == ")":
            return Token(Tag.RP)

        if self.peek == ";":
            return Token(Tag.ENDLN)

        if self.peek == ".":
            return Token(Tag.ENDP)

        if self.peek == ",":
            return Token(Tag.COMA)

        if self.peek == "+":
            return Token(Tag.SUM)

        if self.peek == '<':
            if self.peek_char() == '=':
                self.peek = self.input.read(1)
                return Token(Tag.LE)
            elif self.peek_char() == '>':
                self.peek = self.input.read(1)
                return Token(Tag.NEQ)

            self.peek = self.input.read(1)
            return Token(Tag.L)

        if self.peek == '>':
            if self.peek_char() == '=':
                self.peek = self.input.read(1)
                return Token(Tag.GE)
            return Token(Tag.G)

        if self.peek == '=':
            if self.peek_char() == '=':
                self.peek = self.input.read(1)
                return Token(Tag.EQ)

        if self.peek == ':':
            if self.peek_char() == '=':
                self.peek = self.input.read(1)
                return Token(Tag.ASSIGN)
            return Token(Tag.TD)


        if self.peek == '"':
            return self.readCharacterString()

        if self.peek.isdigit():
            v = 0
            v = (10 * v) + int(self.peek)
            while self.peek_char().isdigit():
                self.peek = self.input.read(1)
                v = (10 * v) + int(self.peek)

            if self.peek_char() != '.':
                return Integer(v)
            self.peek = self.input.read(1)
            x = float(v)
            d = 10
            self.peek = self.input.read(1)



            while self.peek_char().isdigit():
                x = x + int(self.peek) / d
                d = d * 10
                self.peek = self.input.read(1)
            return Real(x)

        if self.peek.isalpha():
            name = '' + self.peek.lower()

            while self.peek_char().isalpha() or self.peek_char().isdigit() or self.peek_char() == '_':
                self.peek = self.input.read(1)
                name += self.peek.lower()


            w = self.words.get(name)

            if w is not None:
                return w
            return Word(name,Tag.ID)

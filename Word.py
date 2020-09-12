from Token import Token
import Tag
class Word(Token):
    def __init__(self, lexeme, tag):
        self.lexeme = lexeme
        super().__init__(tag)

    def getLexeme(self):
        return self.lexeme

    

eq = Word("==", Tag.EQ)
ne = Word("<>", Tag.NEQ)
le = Word("<=", Tag.LE)
ge = Word(">=", Tag.GE)
minus = Word("minus", Tag.MINUS)
assing = Word(":=", Tag.ASSIGN)
true = Word("true", Tag.TRUE)
false = Word("false", Tag.FALSE)

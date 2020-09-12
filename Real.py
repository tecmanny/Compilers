from Token import Token
import Tag
class Real(Token):
    def __init__(self,value):
        self.value = value
        super().__init__(Tag.REAL)

    def getValue(self):
        return value

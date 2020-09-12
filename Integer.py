from Token import Token
import Tag
class Integer(Token):
    def __init__(self,value):
        self.value = value
        super().__init__(Tag.INTEGER)

    def getValue():
        return value

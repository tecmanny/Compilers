from Token import Token
import Tag
class CharacterString(Token):
    def __init__(self,value):
        self.value = value
        super().__init__(Tag.STRING)

    def getValue(self):
        return self.value

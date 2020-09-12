import Tag
class Token:
    def __init__(self,tag):
        self.tag = tag

    def getTag(self):
        return tag

    def __str__(self):
        switcher = {
            Tag.PROGRAM:"PROGRAM",
            Tag.CONSTANT:"CONSTANT",
            Tag.COMMENT:"COMMENT",
            Tag.VAR:"VAR",
            Tag.BEGIN:"BEGIN",
            Tag.END:"END",
            Tag.INTEGER:"INTEGER",
            Tag.REAL:"REAL",
            Tag.BOOLEAN:"BOOLEAN",
            Tag.STRING:"STRING",
            Tag.WRITELN:"WRITELN",
            Tag.READLN:"READLN",
            Tag.WHILE:"WHILE",
            Tag.DO:"DO",
            Tag.REPEAT:"REPEAT",
            Tag.UNTIL:"UNTIL",
            Tag.FOR:"FOR",
            Tag.TO:"TO",
            Tag.DOWNTO:"DOWNTO",
            Tag.IF:"IF",
            Tag.THEN:"THEN",
            Tag.ELSE:"ELSE",
            Tag.NOT:"NOT",
            Tag.DIV:"DIV",
            Tag.MOD:"MOD",
            Tag.AND:"AND",
            Tag.OR:"OR",
            Tag.EQ:"==",
            Tag.NEQ:"<>",
            Tag.L:"<",
            Tag.LE:"<=",
            Tag.GE:">=",
            Tag.G:">",
            Tag.MINUS:"-",
            Tag.ASSIGN:":=",
            Tag.TD:":",
            Tag.ID:"ID",
            Tag.EOF:"EOF",
            Tag.LP:"(",
            Tag.ENDLN:";",
            Tag.RP:")",
            Tag.TRUE:"TRUE",
            Tag.FALSE:"FALSE",
            Tag.ENDP:".",
            Tag.COMA:",",
            Tag.SUM:"+"

        }
        return switcher.get(self.tag, '')

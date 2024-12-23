from enum import Enum


class Token(Enum):
    EOF = "EOF"         # End of file token (EOF)
    IDENTIFIER = "IDENTIFIER"   # Variable name (x, y, foo)
    INTEGER = "INTEGER"   # Integer literal (123)
    STRING = "STRING"       # String literal "hello"
    ASSIGN = "ASSIGN"       # Assignment operator =
    SEMICOLON = "SEMICOLON"   # Semicolon ;
    LET = "LET"         # Let keyword

    def __eq__(self, value):
        return super().__eq__(value) or self.value == value

keywords = {
    "let": Token.LET
}
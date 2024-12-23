from scanner import Scanner
from token_type import Token, keywords

class Lexer:

    def __init__(self, input: str):
        self.scanner = Scanner(input)

    def next_token(self):
        while not self.eof():
            self.skip_whitespace()
            if self.eof():
                break
            char = self.scanner.peek()
            if char == '"':
                self.scanner.next()
                return self.parse_string()
            elif char == '=':
                return (Token.ASSIGN, self.scanner.next())
            elif char.isdigit():
                return (Token.INTEGER, self.parse_number())
            elif char == ';':
                return (Token.SEMICOLON, self.scanner.next())
            else:
                identifier = self.parse_identifier()
                if identifier in keywords:
                    return (keywords[identifier], identifier)
                return (Token.IDENTIFIER, identifier)
        
    def skip_whitespace(self):
        while not self.eof():
            char = self.scanner.peek()
            if char == ' ' or char == '\n' or char == '\t':
                self.scanner.next()
            else:
                break

    def parse_number(self):
        s = ''
        while not self.eof():
            char = self.scanner.peek()
            if char.isdigit():
                s += self.scanner.next()
            else:
                return s
        return

    def parse_string(self):
        s = ''
        while not self.eof():
            char = self.scanner.next()
            if char == '"':
                return s
            s += char
        return s
    
    def parse_identifier(self):
        s = ''
        while not self.eof():
            char = self.scanner.next()
            if char == ' ' or char == '\n' or char == '\t':
                return s
            s += char
        return s
    
    def eof(self):
        return self.scanner.eof()
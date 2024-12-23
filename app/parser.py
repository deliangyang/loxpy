from lex import Lexer
from last import *
from token_type import Token


class Parser:

    def __init__(self, input: str):
        self.lexer = Lexer(input)

    def parse(self):
        while not self.lexer.eof():
            token = self.lexer.next_token()
            if token[0] == Token.LET:
                print(self.parse_let_statement())
            elif token[0] == "EOF":
                break

    def parse_let_statement(self):
        (_, identifier) = self.lexer.next_token()
        (tk, _) = self.lexer.next_token()
        if tk != Token.ASSIGN:
            raise Exception("Expected =")
        expression = self.parse_expression()
        return LetStatement(identifier, expression)
    
    def parse_expression(self):
        while not self.lexer.eof():
            (tk, value) = self.lexer.next_token()
            if tk == Token.INTEGER:
                return IntegerLiteral(value)
            elif tk == Token.STRING:
                return StringLiteral(value)
            elif tk == Token.IDENTIFIER:
                return Identifier(value)
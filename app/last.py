
class Expression:
    pass


class IntegerLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class StringLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'"{self.value}"'


class Identifier(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class BinaryExpression(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"


class Statement:
    pass

class LetStatement(Statement):
    def __init__(self, name: StringLiteral, value: Exception):
        self.name = name
        self.value = value

    def __str__(self):
        return f"let {self.name} = {self.value};"
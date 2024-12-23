

class Scanner:
    def __init__(self, input: str):
        self.input = input
        self.l = len(input)
        self.pos = 0

    def peek(self)-> str:
        if self.pos < self.l:
            return self.input[self.pos]
        return ''
    
    def next(self)-> str:
        if self.pos < self.l:
            self.pos += 1
            return self.input[self.pos-1]
        return ''
    
    def eof(self)-> bool:
        return self.pos >= self.l

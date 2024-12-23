import sys
from lex import Lexer
from parser import Parser


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command not in ('tokenize', 'parse'):
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if command == 'tokenize':
        if file_contents:
            lexer = Lexer(file_contents)
            while not lexer.eof():
                print(lexer.next_token())
        else:
            print("EOF  null") # Placeholder, remove this line when implementing the scanner
    elif command == 'parse':
        if file_contents:
            parser = Parser(file_contents)
            parser.parse()
        else:
            print("EOF")


if __name__ == "__main__":
    main()

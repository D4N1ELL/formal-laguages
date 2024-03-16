class Token:
    Kwd = "Kwd"
    Number = "Number"
    Def = "Def"
    Ident = "Ident"


class Lexer:
    def __init__(self):
        pass

    def lex(self, stream):
        if not stream:
            return []

        if stream[0] in [' ', '\n', '\r', '\t']:
            return self.lex(stream[1:])

        if stream.startswith('//'):
            # If line starts with //, find the newline character and return the tokenized stream till there
            newline_index = stream.find('\n')
            if newline_index != -1:
                return self.lex(stream[newline_index + 1:])
            else:
                return []

        if stream.startswith('/*'):
            return self.lex_block_comment(stream[2:])

        if stream[0].isalpha():
            buffer = stream[0]
            return self.lex_ident(buffer, stream[1:])

        if stream[0].isdigit():
            buffer = stream[0]
            return self.lex_number(buffer, stream[1:])

        if stream[0] in ['+', '-', '*', '/', '(', ')']:
            return [(Token.Kwd, stream[0])] + self.lex(stream[1:])

        return [(Token.Kwd, stream[0])] + self.lex(stream[1:])

    def lex_number(self, buffer, stream):
        if not stream:
            return [(Token.Number, float(buffer))]

        if stream[0].isdigit() or stream[0] == '.':
            buffer += stream[0]
            return self.lex_number(buffer, stream[1:])

        return [(Token.Number, float(buffer))] + self.lex(stream)

    def lex_ident(self, buffer, stream):
        if not stream:
            return [(Token.Ident, buffer)]

        if stream[0].isalnum():
            buffer += stream[0]
            return self.lex_ident(buffer, stream[1:])

        if buffer == "def":
            return [(Token.Def,)] + self.lex(stream)
        else:
            return [(Token.Ident, buffer)] + self.lex(stream)

    def lex_block_comment(self, stream):
        if not stream:
            return []

        end_index = stream.find('*/')
        if end_index == -1:
            return []

        return self.lex(stream[end_index + 2:])


def parse(stream):
    lexer = Lexer()
    tokens = lexer.lex(stream)
    return tokens


if __name__ == '__main__':
    file = "test.myLang"
    contents = open(file, "r").read()
    tokens = parse(contents)
    print(tokens)

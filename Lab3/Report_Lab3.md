# Topic: Lexer & Scanner

### Course: Formal Languages & Finite Automata
### Author: Istrati Daniel

----
## Theory

&ensp;&ensp;&ensp; The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages.

&ensp;&ensp;&ensp; The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.

----
## Objectives:

1.  Understand what lexical analysis is.
    
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
    
3. Implement a sample lexer and show how it works.

----
## Code

1. Token Class: This class defines different types of tokens that can be identified in the code.
```commandline
class Token:
    Kwd = "Kwd"
    Number = "Number"
    Def = "Def"
    Extern = "Extern"
    Ident = "Ident"
    String = "String"
```

2. Lexer Class: This class is responsible for converting a stream of characters into tokens.
        The lex method is the main entry point. It analyzes each character in the input stream and generates tokens accordingly.
        It skips whitespace characters, handles comments (both single-line and block comments), identifies keywords and identifiers, and extracts numbers.
        The methods lex_number, lex_ident, and lex_block_comment handle specific token types.


3. Parse Function: This function takes a string input (the code) and initiates the lexer to tokenize it. It returns the list of tokens generated from the input code.
```commandline
def parse(stream):
    lexer = Lexer()
    tokens = lexer.lex(stream)
    return tokens
```

4. Main Block: In the main block, a file named "test.myLang" is opened, its contents are read, and then the parse function is called to tokenize those contents.
        Finally, the tokens are printed.
```commandline
if __name__ == '__main__':
    file = "test.myLang"
    contents = open(file, "r").read()
    tokens = parse(contents)
    print(tokens)
```

----
## Results:

```commandline
('Kwd', '#')
('Ident', 'include')
('Kwd', '<')
('Ident', 'stdio')
('Kwd', '.')
('Ident', 'h')
('Kwd', '>')
('Def',)
('Ident', 'randomFunction')
('Kwd', '(')
('Kwd', ')')
('Kwd', '{')
('Ident', 'int')
('Ident', 'fignea')
('Kwd', '=')
('Number', 1.0)
('Kwd', ';')
('Ident', 'float')
('Ident', 'tojeSamoe')
('Ident', 'if')
('Ident', 'fignea')
('Kwd', '>')
('Ident', 'tojeSamoe')
('Kwd', '{')
('Ident', 'printf')
('Kwd', '(')
('String', 'Ciota ne to')
('Kwd', ')')
('Kwd', ';')
('Kwd', '}')
('Kwd', '}')
('Ident', 'int')
('Ident', 'main')
('Kwd', '(')
('Kwd', ')')
('Kwd', '{')
('Ident', 'printf')
('Kwd', '(')
('String', 'Hello World!')
('Kwd', ')')
('Kwd', ';')
('Ident', 'return')
('Number', 0.0)
('Kwd', ';')
('Kwd', '}')
```

----
## Conclusions

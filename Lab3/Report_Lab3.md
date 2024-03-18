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

2. Lexer Class: This class is responsible for converting a stream of characters into tokens. The lex method is the main 
        entry point. It analyzes each character in the input stream and generates tokens accordingly. 
```commandline
if stream[0].isalpha():
    buffer = stream[0]
    return self.lex_ident(buffer, stream[1:])
```
For example this specific function checks for alphabetical characters. `isalpha()` checks if the first character of the 
stream is alphabetic (a letter). If the first character is alphabetic, it proceeds to the next lines:
`buffer = stream[0]` Assigns the first character of the stream to the variable buffer. Then it returns `lex_ident` identifiers in the input stream.


In the same way work other functions for finding comments `if stream.startswith('//'):` skipping whitespaces `if stream[0] in [' ', '\n', '\r', '\t']:`
finding strings `if stream[0] == '"'` and extracts numbers `if stream[0].isdigit():`. The methods lex_number, lex_ident, and lex_block_comment handle specific token types.


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

During this lab I understood what a lexer is and how it works. It essentially is conversion of a text into 
meaningful lexical tokens belonging to categories defined by a "lexer" class. In case of a natural language, 
those categories include nouns, verbs, adjectives, punctuations etc. In case of a programming language, the categories 
include identifiers, operators, grouping symbols and data types. 

I made it so it reads a whole C like document, and it divides each character into a token. It recognizes strings, numbers, 
individual characters, skips new lines, defined functions, comments and also blocks of comments.

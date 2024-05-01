# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Istrati Daniel

----
## Overview
&ensp;&ensp;&ensp; The process of gathering syntactical meaning or doing a syntactical analysis over some text can also be called parsing. It usually results in a parse tree which can also contain semantic information that could be used in subsequent stages of compilation, for example.

&ensp;&ensp;&ensp; Similarly to a parse tree, in order to represent the structure of an input text one could create an Abstract Syntax Tree (AST). This is a data structure that is organized hierarchically in abstraction layers that represent the constructs or entities that form up the initial text. These can come in handy also in the analysis of programs or some processes involved in compilation.

----
## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

----
## Code

1. Token Class: This class defines different types of tokens that can be identified in the code.
```commandline
class Token:
    Kwd = "Kwd"
    Float = "Float"
    Def = "Def"
    Extern = "Extern"
    Ident = "Ident"
    String = "String"
    LPAREN = "("
    RPAREN = ")"
    Type = "Type"
    Library = "Library"
    Function = "Function"
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
('Library', 'stdio')
('Kwd', '.')
('Ident', 'h')
('Kwd', '>')
('Def',)
('Function', 'randomFunction')
('LPAREN', '(')
('RPAREN', ')')
('Kwd', '{')
('Type', 'int')
('Ident', 'fignea')
('Kwd', '=')
('Float', 1.0)
('Kwd', ';')
('Type', 'float')
('Ident', 'tojeSamoe')
('Function', 'if')
('Ident', 'fignea')
('Kwd', '>')
('Ident', 'tojeSamoe')
('Kwd', '{')
('Ident', 'printf')
('LPAREN', '(')
('String', 'Ciota ne to')
('RPAREN', ')')
('Kwd', ';')
('Kwd', '}')
('Kwd', '}')
('Type', 'int')
('Function', 'main')
('LPAREN', '(')
('RPAREN', ')')
('Kwd', '{')
('Function', 'printf')
('LPAREN', '(')
('String', 'Hello World!')
('RPAREN', ')')
('Kwd', ';')
('Ident', 'return')
('Float', 0.0)
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

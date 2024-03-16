from sys import *


def lexer(contents):
    lines = contents.split("\n")

    for line in lines:
        tokens = []


def parse(file):
    file = "test.myLang"
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return contents


if __name__ == '__main__':
    print(parse(argv[0]))




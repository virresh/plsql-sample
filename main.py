#!/usr/bin/env python
from antlr4 import FileStream, CommonTokenStream
from generated.plsqlLexer import plsqlLexer
from generated.plsqlParser import plsqlParser
from generated.plsqlVisitor import plsqlVisitor

import sys

class Visitor(plsqlVisitor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unique_print_flag = False

    def visitCreate_table(self, ctx):
        # print(ctx.getText())
        self.unique_print_flag = True
        print('\n---- Start Create Table Statement ----')
        k = self.visitChildren(ctx)
        print('\n---- End Create Table Statement ----\n\n')
        self.unique_print_flag = False
        return k

    def visitCreate_type(self, ctx):
        # print(ctx.getText())
        self.unique_print_flag = True
        print('\nxxxx Start Create Type Statement xxxx')
        k = self.visitChildren(ctx)
        print('\nxxxx End Create Type Statement xxxx\n\n')
        self.unique_print_flag = False
        return k

    def visitTerminal(self, node):
        if self.unique_print_flag:
            print(node.getText(), end=" ")

def main(args):
    file = FileStream(args[1])
    lexer = plsqlLexer(file)
    stream = CommonTokenStream(lexer)
    parser = plsqlParser(stream)
    tre = parser.sql_script()
    if parser.getNumberOfSyntaxErrors()!=0:
        print("File contains {} "
              "syntax errors".format(parser.getNumberOfSyntaxErrors()))
        return

    visitor = Visitor()
    visitor.visit(tre)

if __name__ == '__main__':
    """
    Sample usage:
    python main.py ./sample_files/create_tables_samples.sql
    """
    main(sys.argv)
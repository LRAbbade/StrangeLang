import argparse
import os
from lexer import Lexer

parser = argparse.ArgumentParser(description='Compiler for StrangeLang')
parser.add_argument('source', metavar='source_path', help='Path to source file')
args = parser.parse_args()
file_path = args.source

if not os.path.isfile(file_path):
    raise Exception('File does not exists')

def get_source_text():
    with open(file_path, 'r') as source_file:
        return source_file.read()

program = get_source_text()

lexer = Lexer()
token_list = lexer.tokenize(program)

import argparse
import os
from lexer import Lexer
from syntax import Syntax
from pprint import pprint

TEST_PATH = 'Tests/test.sl'

parser = argparse.ArgumentParser(description='Compiler for StrangeLang')
parser.add_argument('-f', help='Path to source file')
parser.add_argument('--test', help='Execute Tests/test.sl file', action="store_true")
args = parser.parse_args()

file_path = TEST_PATH if args.test else args.f

if not os.path.isfile(file_path):
    raise Exception('File does not exists')

def get_source_text():
    with open(file_path, 'r') as source_file:
        return source_file.read()

program = get_source_text()
print(f'source program:\n--------------------\n{program}\n--------------------\n')

print('Starting Lexical Analysis')
lexer = Lexer()
token_list = lexer.tokenize(program)
print('Token list:')
pprint(token_list)

print('Starting Syntax Analyzer')
syntax = Syntax(token_list)
result = syntax.run()

if result:
    print('Syntax analyzer run successfully')

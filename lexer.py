import json
import re

TOKENS_FILE = 'Configs/tokens.json'
number_re = re.compile(r"^\d+\.?\d*$")
var_name_re = re.compile(r"^[_a-zA-Z]+[_a-zA-Z0-9]*$")
string_re = re.compile(r'".*"')

class Lexer:

    def __init__(self):
        self._load_tokens()

    def _load_tokens(self):
        with open(TOKENS_FILE, 'r') as tokens:
            self._tokens = json.load(tokens)

    def _validate_word(self, word):
        def test_tokens(token_type):
            return (True, token_type[:-1], word) if word in self._tokens[token_type] else (False, None, None)

        def test_re(compiled_re, test_type):
            aux = compiled_re.findall(word)
            return (True, test_type, aux[0]) if len(aux) > 0 else (False, None, None)
        
        results = [i for i in [
            test_tokens('keywords'),
            test_tokens('operators'),
            test_tokens('separators'),
            test_re(number_re, 'number'),
            test_re(string_re, 'string'),
            test_re(var_name_re, 'var_name')
        ] if i[0]]
        
        if len(results) > 0:
            return results[0][1], results[0][2]
        
        raise Exception(f'Invalid token: {word}')

    def tokenize(self, source):
        words = [word for word in source.split() if len(word) > 0]
        return [self._validate_word(word) for word in words]

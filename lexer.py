import json
import re

TOKENS_FILE = 'Configs/tokens.json'

class Lexer:

    def __init__(self):
        self._load_tokens()

    def _load_tokens(self):
        with open(TOKENS_FILE, 'r') as tokens:
            self._tokens = json.load(tokens)

    def tokenize(self, source):
        pass

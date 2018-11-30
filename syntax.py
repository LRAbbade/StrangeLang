from node import Node
import json

GRAMMAR_PATH = 'Configs/grammar.json'

class Syntax:

    def __init__(self, token_list):
        self._grammar = self._load_grammar(GRAMMAR_PATH)
        self.token_list = token_list

    def _load_grammar(self, path):
        with open(path, 'r') as file:
            return json.load(file)

    def run(self):
        return self._derivate("S", 0, 0, 0)

    def _derivate(self, nonTerminal, currently_producing, production_position, list_position):
        wait = input()
        print(f'derivate status: {self._get_status(nonTerminal, currently_producing, production_position, list_position)}')

        if list_position >= len(self.token_list):
            print(' * finished running derivate with success')
            return True     # reached the end with no problem
        elif self.token_list[list_position] == ';':   # End of line
            print(' * reached end of a line')
            if self._grammar[nonTerminal][currently_producing][production_position] == ';': # right
                print(' * end of line reached successfully')
                return self._derivate("S", 0, 0, production_position + 1)
            else:                                                                           # wrong
                print(' * line not ended for production, wrong')
                return False

        if currently_producing >= len(self._grammar[nonTerminal]):  # reached the end of this nonTerminal without success
            print(' * reached end of this nonTerminal possibilies, wrong')
            return False
        
        if production_position >= len(self._grammar[nonTerminal][currently_producing]): # reached the end of this possible sentence without success
            print(' * reached the end of this possible production, wrong')
            return False

        current_token = self.token_list[list_position][0]
        possible_production = self._grammar[nonTerminal][currently_producing][production_position]
        is_non_terminal = possible_production in self._grammar

        print(f'\nCurrent token: {current_token}\nPossible production: {possible_production}\n')

        if is_non_terminal:
            print(' * current possible production is non terminal')
            r = self._derivate(possible_production, 0, 0, list_position)
        elif current_token == possible_production:  # matched terminal
            print(' * matched terminal token')
            r = self._derivate(nonTerminal, currently_producing, production_position + 1, list_position + 1)
        elif possible_production == 'eps':          # possible production is empty
            print(' * matched eps')
            # I dont know what to do here
        else:                                       # not matched terminal
            print(' * did not match terminal token')
            r = self._derivate(nonTerminal, currently_producing + 1, 0, list_position - currently_producing)

        if not r:
            raise Exception(f'No match in derivation: \n{self._get_status(nonTerminal, currently_producing, production_position, list_position)}')

        return r

    def _get_status(self, nonTerminal, currently_producing, production_position, list_position):
        return f'NonTerminal: {nonTerminal}\nCurrently_producing: {currently_producing}\nProduction_position: {production_position}\nList_position: {list_position}'

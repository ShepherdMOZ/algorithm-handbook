from typing import List, Dict, Set

class BracketStack():

    def __init__(self):
        self.stack: List[str] = []

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack):
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def is_empty(self):
        if len(self.stack):
            return False
        return True
    
    def push(self, value):
        BRACKET_PAIR: Dict[str,str] = {']':'[','}':'{',')':'('}
        if value in BRACKET_PAIR.values():
            self.stack.append(value)
        elif value in BRACKET_PAIR.keys():
            if len(self.stack) and self.peek() == BRACKET_PAIR.get(value):
                self.pop()
            else:
                return False

def check_balance(sample:str):
    brackets = BracketStack()
    for char in sample:
        if brackets.push(char) is False:
            return False
    if brackets.is_empty():
        return True
    
    return False


if __name__ == "__main__":
    print(check_balance("()()()({})([{}])"))
    print(check_balance("{[}]"))



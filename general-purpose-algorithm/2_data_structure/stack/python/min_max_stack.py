from typing import List, Dict

class MinMaxStack:

    def __init__(self):
        self.stack:List[int] = []
        self.min_max_stack: List[Dict] = []


    def pop(self):
        '''
        Complexity: Time O(1), Space O(1)
        Pop the top of stack
        '''
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, value):
        '''
        Complexity: Time O(1), Space O(1)
        Push a new item to the stack, also caching the min/max value of stack
        '''
        min_max:Dict[str,int]= {'min': value ,'max': value}
        if len(self.min_max_stack):
            last_cache = self.min_max_stack[len(self.min_max_stack) - 1]
            min_max['min'] = min(last_cache['min'], value)
            min_max['max'] = max(last_cache['max'], value)
        self.min_max_stack.append(min_max)
        self.stack.append(value)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def get_min(self):
        if len(self.min_max_stack):
            return self.min_max_stack[len(self.min_max_stack) - 1]['min']
        else:
            return self.stack.peek()

    def get_max(self):
        if len(self.min_max_stack):
            return self.min_max_stack[len(self.min_max_stack) - 1]['max']
        else:
            return self.stack.peek()

    def peek_all(self):
        return self.stack


if __name__ == "__main__":
    new_stack = MinMaxStack()
    new_stack.push(1)
    print(new_stack.get_min())
    print(new_stack.get_max())
    new_stack.push(2)
    new_stack.push(3)
    new_stack.push(4)
    new_stack.push(5)
    print(new_stack.peek_all())
    print(new_stack.peek())
    print(new_stack.get_min())
    print(new_stack.get_max())
    new_stack.pop()
    print(new_stack.peek())
    print(new_stack.get_max())



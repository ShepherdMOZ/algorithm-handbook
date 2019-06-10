def boggleBoard(board, words):
    # Write your code here.
    tree = SufTree()
    for word in words:
        tree.insert(word)
        
    found_strings = []
    find_string(tree, board, found_strings)
    return found_strings
    
    
def find_string(tree, board, found_strings):
    for i in range(len(board)):
        for j in range(len(board[i])):
            letter = board[i][j]
            node = tree.node
            if letter in node:
                check_word(i,j,board,node[letter],tree,letter,found_strings)

def check_word(row,col,board,node,tree,word,found_strings):
    if board[row][col] == '*':
        return
    
    if tree.end_symbol in node and node[tree.end_symbol] == word:
        found_strings.append(word)
    
    current_letter = board[row][col]
    board[row][col] = '*'
    #top-left
    if row-1 > 0 and col-1 > 0 and board[row-1][col-1] in node:
        letter  =  board[row-1][col-1]
        check_word(row-1, col-1, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #top
    if row-1 > 0 and board[row-1][col] in node:
        letter  =  board[row-1][col]
        check_word(row-1, col, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #top-right
    if row-1 > 0 and col+1<len(board[row]) and board[row-1][col+1] in node:
        letter  =  board[row-1][col+1]
        check_word(row-1, col+1, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #left
    if  col-1 > 0 and board[row][col-1] in node:
        letter  =  board[row][col-1]
        check_word(row, col-1, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #right
    if  col+1 < len(board[row]) and board[row][col+1] in node:
        letter  =  board[row][col+1]
        check_word(row, col+1, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #btm-left
    if  row+1 < len(board) and col-1 > 0 and board[row+1][col-1] in node:
        letter  =  board[row+1][col-1]
        check_word(row+1, col-1, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #btm
    if  row+1 < len(board) and board[row+1][col] in node:
        letter  =  board[row+1][col]
        check_word(row+1, col, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
    #btm-right
    if  row+1 < len(board) and col+1 < len(board[row]) and board[row+1][col+1] in node:
        letter  =  board[row+1][col+1]
        check_word(row+1, col+1, board, node[letter], tree ,word+letter, found_strings)
        board[row][col] = current_letter
        
    board[row][col] = current_letter
            
class SufTree:
    def __init__(self):
        self.node = {}
        self.end_symbol = '*'
        
    def insert(self, string):
        current_node = self.node
        for i in range(len(string)):
            letter = string[i]
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node[self.end_symbol] = string


if __name__ == "__main__":
    board = [
        ['a','b','c','d','e'],
        ['f','g','h','i','j'],
        ['k','l','m','n','o'],
        ['p','q','r','s','t'],
        ['u','v','w','x','y'],
    ]
    words = ["agmsy","agmsytojed","agmsytojedinhcbfl","agmsytojedinhcbgl"]
    print(boggleBoard(board,words))

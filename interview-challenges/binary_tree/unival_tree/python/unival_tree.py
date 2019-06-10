
import unittest

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert_left(self, value):
        self.left = Tree(value)
        return self

    def insert_right(self, value):
        self.right = Tree(value)
        return self

def count_unival_tree(tree: Tree):
    counter = 0
    tree, counter = unival_counter(tree, counter)
    return counter

def unival_counter(sub_tree: Tree, counter):
    if sub_tree.left is None and sub_tree.right is None:
        counter += 1
        return (sub_tree, counter)
    else:
        left = None
        right = None

        if sub_tree.left is not None:
            left, count_left = unival_counter(sub_tree.left, counter)
        if sub_tree.right is not None:
            right, count_right = unival_counter(sub_tree.right, counter)

        counter += count_left + count_right

        if left and right:
            if left.value == sub_tree.value and right.value == sub_tree.value:
                counter += 1
        
        return (sub_tree, counter)
        
class TestCase(unittest.TestCase):
    tree_1 = Tree(1).insert_left(1).insert_right(1)
    tree_0 = Tree(0).insert_left(0).insert_right(0)
    
    ## tree_case_1 has 4 unival sub tree
    tree_case_1 = Tree(0, left=tree_1, right=Tree(0))

    ## tree_case_2 has 5 unival sub tree
    tree_case_2 = Tree(0, left=Tree(1), right=tree_case_1)

    ## tree_case_3 has 7 unival sub tree
    tree_case_3 = Tree(0, left=tree_1, right=tree_case_1)

    ## tree_case_4 has 7 unival sub tree
    tree_case_4 = Tree(1, left=tree_1, right=tree_1)
    
    ## tree_case_5 has 6 unival sub tree
    tree_case_5 = Tree(0, left=tree_1, right=tree_1)


    def test_point_1(self):
        self.assertEqual(count_unival_tree(self.tree_case_1), 4)
    
    def test_point_2(self):
        self.assertEqual(count_unival_tree(self.tree_case_2), 5)

    def test_point_3(self):
        self.assertEqual(count_unival_tree(self.tree_case_3), 7)

    def test_point_4(self):
        self.assertEqual(count_unival_tree(self.tree_case_4), 7)
    
    def test_point_5(self):
        self.assertEqual(count_unival_tree(self.tree_case_5), 6)

if __name__=="__main__":
    unittest.main()
import unittest



class SingleLinkedList():

    def __init__(self, value):
        self.value = value
        self.next = None

    def add_nodes(self, array):
        if len(array) > 0:
            last_node = self
            while last_node.next is not None:
                last_node = last_node.next

            for i in range(len(array)):
                new_node = SingleLinkedList(array[i])
                last_node.next = new_node
                last_node = new_node
        return self
    
    def get_nodes_to_array(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

    def remove_kth(self, k):
        '''
        Complexity: Time = O(n); Space = O(1)
        '''
        if k <= 0:
            return False
        interval_length = 1
        interval_start = self
        interval_end = self

        ## Move interval end to the position
        while interval_length <= k:
            interval_end = interval_end.next
            interval_length += 1
        
        ## Reach the start of the linked list
        if interval_end is None:
            interval_start.value = interval_start.next.value
            interval_start.next = interval_start.next.next
            return self

        ## move interval start to the place where item is for removing.
        while interval_end.next is not None:
            interval_start = interval_start.next
            interval_end = interval_end.next
        
        interval_start.next = interval_start.next.next

        return self
        




class TestCases(unittest.TestCase):

    ## Test the correctness of Single List Class
    
    def test_case_1(self):
        case = SingleLinkedList(0).add_nodes([1,2,3,4,5])
        self.assertEqual(case.get_nodes_to_array(),[0,1,2,3,4,5])

    def test_case_2(self):
        case = SingleLinkedList(0).add_nodes([1,2,3])
        self.assertEqual(case.get_nodes_to_array(),[0,1,2,3])
    
    def test_case_3(self):
        case = SingleLinkedList(0).add_nodes([1,2,3]).add_nodes([4,5])
        self.assertEqual(case.get_nodes_to_array(),[0,1,2,3,4,5])

    ## Test Remove Kth function
    def test_case_4(self):
        case = SingleLinkedList(0).add_nodes([1,2,3,4,5,6]).add_nodes([7,8,9])
        self.assertEqual(case.remove_kth(3).get_nodes_to_array(),[0,1,2,3,4,5,6,8,9])
    
    def test_case_5(self):
        case = SingleLinkedList(0).add_nodes([1,2,3]).add_nodes([4,5])
        self.assertEqual(case.remove_kth(6).get_nodes_to_array(),[1,2,3,4,5])


if __name__ == "__main__":
    unittest.main()    
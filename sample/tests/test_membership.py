import unittest

class ContainerMembershipTest(unittest.TestCase):
    def test_list(self):
        self.assertIn(4,[1,2,4,3])
    
    def test_dict(self):
        self.assertIn(3,{1:'a',2:'b',3:'c'})
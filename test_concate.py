import unittest
import concatenate as c

class TestConcate(unittest.TestCase):
    # Function name should be 'test*'
    def test_concate(self):
        self.assertEqual(c.concate(33,44),'33443344')
        self.assertEqual(c.concate(2,'abc'),'2abc2abc')
        self.assertEqual(c.concate(2.89,'c'),'2.89c2.89c')
        
        # (type of error, def, argument_1, argument_2, etc.)
        # self.assertRaises(ValueError, c.concate, 'bb', None)
        
        # Usage of context manager:
        with self.assertRaises(ValueError):
            c.concate(None, 2)
            c.concate(None, None)
            c.concate(2, None)
            c.concate(None, 'bb')

if __name__ == '__main__':
    # When called, it runs all of the methods that start with the word "test" in any class derived from unittest.TestCase
    # One function counts one test
    unittest.main()
        
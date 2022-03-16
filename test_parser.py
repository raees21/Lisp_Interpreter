import unittest
from parser import translate
from tokenizer import tokenize

class MyTestCase(unittest.TestCase):
    """ to test the parsing capabilities"""
    def test_translate(self):
        input_str = "(eq 2 3)"
        result = translate(tokenize(input_str))
        self.assertEqual(result, [ ["EQ", 2, 3] ])

    
if __name__ == '__main__':
    unittest.main()
import unittest
import tokenizer

class MyTestCase(unittest.TestCase):
    def test_tokenize_empty_list(self):
        input_str = "()"
        result = tokenizer.tokenize(input_str)
        self.assertEqual(result, ['(', ')'])

    def test_tokenize_correct(self):
        input_str = "(eq 2 3)"
        result = tokenizer.tokenize(input_str)
        self.assertEqual(result, ['(', 'eq', '2', '3', ')'])
    
    def test_tokenize_incorrect(self):
        input_str = "((eq 2 3 four)"
        try:
            result = tokenizer.tokenize(input_str)
        except:
            result = "Raised an error!"
        self.assertEqual(result, "Raised an error!")

    def testis_valid_syntax(self):
        input_str = "(eq 2 3 four)"
        result = tokenizer.tokenize(input_str)
        self.assertTrue(result, True)
    

if __name__ == '__main__':
    unittest.main()
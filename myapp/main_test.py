from main import return_backwards_string
import unittest
#import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, return_backwards_string(random_string))

   

if __name__ == "__main__":
    unittest.main()
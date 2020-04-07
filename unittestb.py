'''
Using Unittest library:
	- Used to send data to your test program, analyse the returned data and check if they are the expected results.
		
'''

import unittest
import unittesta


class TestCap(unittest.TestCase):
    def test_one(self):
        text = "mark"
        result = unittesta.cap_text(text)
        self.assertEqual(result, "Mark")


if __name__ == "__main__":
    unittest.main()

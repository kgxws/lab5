import unittest
import sys
sys.path.append('src')
import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)

    def test_fail(self):
        self.assertEqual(1, 2)  # Упадет

if __name__ == '__main__':
    unittest.main()
EOF
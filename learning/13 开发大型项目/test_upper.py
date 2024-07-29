import unittest


class TestStringUpper(unittest.TestCase):
    def setUp(self):
        print("Runing:")

    def test_normal(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_fail(self):
        self.assertTrue("foo".upper() == "FOO")

    def tearDown(self):
        print("Donwn!")


if __name__ == "__main__":
    unittest.main()

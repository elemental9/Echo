import echo_lang as e
import unittest


class TestMethods(unittest.TestCase):
    def test_Echo(s):
        e.Echo("Hello World!")
        e.Echo("Free!", 20)

    def test_Echopi(s):
        e.Echopi()


if __name__ == '__main__':
    unittest.main()

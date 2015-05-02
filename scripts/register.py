import sys

__author__ = 'nmader'


import unittest
from lib.testenv import TestEnv
from lib.oculus_app import Oculus_app


class Register(unittest.TestCase):
    def setUp(self):
        self.env = TestEnv()
        self.app = Oculus_app(self.env)

    def tearDown(self):
        if sys.exc_info()[0]:
            self.env.make_screenshot_android()
        self.env.__exit__()

    def test_register(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Register)
    unittest.TextTestRunner(verbosity=2).run(suite)

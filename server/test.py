import unittest
import sys

tests = unittest.TestLoader().discover("tests")
result = unittest.TextTestRunner(verbosity=2).run(tests)
if result.errors or result.failures:
    sys.exit(1)
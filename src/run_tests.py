import unittest
import os

def discover_and_run_tests(start_dir):
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern="test*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    start_dir = os.path.dirname(os.path.abspath(__file__))
    discover_and_run_tests(start_dir)

import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

pytest_args = [
    # 'src',  # Directory containing tests
    '-v',  # Verbose output
    '--maxfail=1',  # Stop after first failure
    # '--disable-warnings'  # Disable warnings
]

exit_code = pytest.main(pytest_args)
sys.exit(exit_code)

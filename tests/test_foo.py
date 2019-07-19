import os
import sys

file_path = os.path.abspath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(file_path)))

from testingpytestframework.foo import bar


def test_bar():
    assert bar(2) == 4
    assert bar(True) == 2
    assert bar("a") == "aa"

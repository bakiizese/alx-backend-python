#!/usr/bin/env python3
from utils import memoize

def memo():
    class TestClass:

        def a_method(self):
            return 42
        
        @memoize
        def a_property(self):
            return self.a_method()

    my = TestClass()
    print(my.a_property())
memo()

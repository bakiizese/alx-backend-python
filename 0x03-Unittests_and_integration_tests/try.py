#!/usr/bin/env python3
from unittest.mock import patch
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import TEST_PAYLOAD

def prints():
    a = TEST_PAYLOAD[0]
    a = a[2]

    #a = a[1]

    print(a)

    
prints()

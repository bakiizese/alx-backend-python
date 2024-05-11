#!/usr/bin/env python3
''' client test '''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    ''' test client '''
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mocked):
        ''' test org '''
        my_ins = GithubOrgClient(org_name)
        my_ins.org()
        mocked.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

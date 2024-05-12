#!/usr/bin/env python3
from unittest.mock import patch
import unittest
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mocked_get):
        my_ins = GithubOrgClient(org_name)
        my_ins.org()
        mocked_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

#!/usr/bin/env python3
''' client test '''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock, Mock, PropertyMock
from parameterized import parameterized
from utils import get_json
#from nessert_labs import mock
#from nessert_labs.mock import propertyMock


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

    @patch('client.get_json', return_value={'repos_url': 'https://api.github.com/orgs/google'})
    def test_public_repos_url(self, mocked_org):
        ''' testing property atttribut '''
        m_ins = GithubOrgClient('google')
        result = m_ins._public_repos_url
        self.assertEqual('https://api.github.com/orgs/google', result)
    

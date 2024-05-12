#!/usr/bin/env python3
''' client test '''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock, Mock, PropertyMock
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

    @patch('client.get_json', return_value={'repos_url': 'https://api.github.com/orgs/google'})
    def test_public_repos_url(self, mocked_org):
        ''' testing property atttribut '''
        m_ins = GithubOrgClient('google')
        result = m_ins._public_repos_url
        self.assertEqual('https://api.github.com/orgs/google', result)

    payload = [
        {'repos_url': 'https://api.github.com/orgs/google', 'name': 'baki'},
        {'repos_url': 'https://api.github.com/orgs/google', 'name': 'dani'},
        {'repos_url': 'https://api.github.com/orgs/google', 'name': 'jack'}]

    @patch('client.get_json', return_value=payload)
    def test_public_repos(self, mocked_get):
        ''' test more patching '''
        with patch('client.GithubOrgClient._public_repos_url') as mocked_org:
            mocked_org.return_value = [{'repos_url': 'https://api.github.com/orgs/google', 'name': 'baki'}]
            my_inst = GithubOrgClient('google')
            r = my_inst.public_repos()
            r2 = my_inst._public_repos_url()
            self.assertEqual(r, ['baki', 'dani', 'jack'])
            mocked_get.assert_called_once()
            mocked_org.assert_called_once()

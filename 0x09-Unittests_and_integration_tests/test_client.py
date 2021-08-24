#!/usr/bin/env python3
""" test client module """

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test client.GithubOrgClient"""

    @parameterized.expand([
        ("google", {}),
        ("abc", {})
        ])
    @patch("client.get_json")
    def test_org(self, url, result, mock):
        """test that GithubOrgClient.org returns the correct value"""
        mock.return_value = {}
        a = GithubOrgClient(url)
        self.assertEqual(a.org, result)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected
        one based on the mocked payload
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as m:
            m.return_value = {"repos_url": "http://m.url"}
            t = GithubOrgClient("xyz")
            a = t._public_repos_url
            self.assertEqual(a, m.return_value.get("repos_url"))


if __name__ == '__main__':
    unittest.main()

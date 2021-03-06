#!/usr/bin/env python
"""Test gswrap helper methods."""

# pylint: disable=missing-docstring
# pylint: disable=protected-access

import unittest

import gswrap


class TestGCSURL(unittest.TestCase):
    def test_expected_structure(self) -> None:
        gs_path = gswrap._GCSURL(
            bucket="bucket", prefix="folder-in-bucket/sub-dir")

        self.assertEqual('bucket', gs_path.bucket)
        self.assertEqual('folder-in-bucket/sub-dir', gs_path.prefix)


class TestGSwrapFunctions(unittest.TestCase):
    def test_contains_wildcard(self) -> None:
        no_wildcard = 'no wildcard here'
        asterisk = '*/somedir'
        questionmark = 'f?lder'
        double_asterisk = 'folder/**/another-folder'

        self.assertFalse(gswrap.contains_wildcard(prefix=no_wildcard))
        self.assertTrue(gswrap.contains_wildcard(prefix=asterisk))
        self.assertTrue(gswrap.contains_wildcard(prefix=questionmark))
        self.assertTrue(gswrap.contains_wildcard(prefix=double_asterisk))

    def test_classify_gcs_url(self) -> None:
        bucket = 'your-bucket'
        prefix = 'your-dir/sub-dir'
        link = 'gs://' + bucket + '/' + prefix
        url = gswrap.resource_type(res_loc=link)

        assert isinstance(url, gswrap._GCSURL)
        self.assertEqual(bucket, url.bucket)
        self.assertEqual(prefix, url.prefix)

    def test_classify_local_url(self) -> None:
        path = '/home/user/'
        url = gswrap.resource_type(res_loc=path)

        self.assertTrue(isinstance(url, str))
        self.assertEqual(path, url)


if __name__ == '__main__':
    unittest.main()

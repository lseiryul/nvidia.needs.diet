import unittest
from unittest import TestCase

from cleaner import clean


class Test(TestCase):

    def setUp(self) -> None:
        # create dummy files for test(copying from resource files)

        # A solution for copying files, found in Stack Overflow.
        # https://stackoverflow.com/a/12514470
        import os, shutil

        def copytree(src, dst, symlinks=False, ignore=None):
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks, ignore)
                else:
                    shutil.copy2(s, d)

        copytree('./res', './')
        # It is confirmed that the file structure is copied properly. @20201014-1115

    def test_clean(self):
        # NOTE:
        # Assume that the given 'path' is designating a directory,
        # and unless referred 'itself' in the explanation of each case,
        # the 'path' is not included in referring 'all directories'.

        # Case: Delete entire directory includes itself.

        # Case: Delete all directories and its belongings in the path, leaving all files.

        # Case: Delete all files only, leaving directories, for all sub-directories under the path.

        self.fail()


if __name__ == '__main__':
    unittest.main()

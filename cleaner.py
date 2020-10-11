import sys
# import platform

# Check os version
# print(sys.platform, platform.architecture())
if 'win' not in sys.platform:
    raise OSError('This script is designed for Windows OS, especially for 64-bit Windows 10.')

# Directories to clean up in simple way; KILL'EM ALL.
TARGET_DIRS = [
    r'C:\ProgramData\NVIDIA Corporation\Downloader'  # Download cache
]
# Directories to clean up but need more attention.
SPECIFIC_TARGET_DIRS = [
    # r''
]


def clean(path, filter=None):
    """Clean up(delete) files under the given path(directory).
    More detailed handling such as filtering, or authorization problems will be appended gradually.

    :param path: str path to clean up.
    :param filter: dict - extensible. Filtering methods will be added.
    :return: tuple - the number of files deleted, the number of directories deleted, total file size cleaned up
    """
    nf = 0
    nd = 0
    tot = 0

    return nf, nd, tot


if __name__ == '__main__':
    pass

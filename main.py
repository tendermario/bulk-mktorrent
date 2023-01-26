#!/usr/bin/env python3

"""

Usage:
    main.py <rootdir>

Options:
    -f --folder=<name>    Folder to make torrents from.

"""

import os
from os import path
from dotenv import load_dotenv
from docopt import docopt
from typing import List


def get_dirs(root: str) -> List[str]:
    """Returns a list of sub-directories from a root directory (non-recursively)."""
    return [path.join(root, i) for i in os.listdir(root) if path.isdir(i)]

def preflight_check():
    myCmd = f'mktorrent'
    if os.system(myCmd) != 0:
        exit("mktorrent needs to be installed")

def make_torrent(path, ANNOUNCE_URL):
    print(f'making a torrent for {path}')
    myCmd = f'mktorrent -l 18 -p -s OPS -a {ANNOUNCE_URL} "{path}"'
    os.system(myCmd)

if __name__ == "__main__":
    load_dotenv()
    arguments = docopt(__doc__)

    rootdir = arguments['<rootdir>']
    ANNOUNCE_URL = os.getenv("ANNOUNCE_URL")

    if not ANNOUNCE_URL:
        raise "Need an announce url. Set this in a .env file."

    dirs = get_dirs(rootdir)
    preflight_check()

    for directory in dirs:
        make_torrent(directory, ANNOUNCE_URL)

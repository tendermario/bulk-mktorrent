#!/usr/bin/env python3

"""

Usage:
    main.py <rootdir>

Options:
    -f --folder=<name>    Folder to make torrents from.

"""

import os
from dotenv import load_dotenv
from docopt import docopt


def getDirs(path):
    dirs = []
    for item in os.listdir(rootdir):
        dir = os.path.join(rootdir, item)
        if os.path.isdir(dir):
            dirs.append(dir)
    return dirs

def makeTorrent(path, ANNOUNCE_URL):
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

    dirs = getDirs(rootdir)

    for dir in dirs:
        makeTorrent(dir, ANNOUNCE_URL)

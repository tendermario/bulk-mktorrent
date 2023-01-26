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
    myCmd = f'mktorrent -h'
    if os.system(myCmd) != 0:
        prompt_install()

def prompt_install():
    print("Error: mktorrent is needed.")
    print("The following will only work if you can ssh clone Github repos. Since you are here, this is pretty likely.")
    if input("Would you like me to try to install  for you? y/n") == 'y':
        install_mktorrent()
    else:
        exit("mktorrent needs to be installed.")


def install_mktorrent():
    os.system("git clone git@github.com:pobrn/mktorrent.git")
    os.system("cd mktorrent; make; sudo make install; cd ..; rm -rf mktorrent")

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

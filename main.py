#!/usr/bin/env python3

# I am using Python 3.11 at the time of writing this script

"""

Usage:
    main.py

Options in .env file:
    FROM=          Folder of folders/files to each turn into torrents.
    TO=            Folder to make .torrent files into. (Use full path)
    ANNOUNCE_URL=  YOUR announce URL.
    TRACKER=       The tracker flag. Orpheus is OPS, Redacted is RED.

"""

import os
from os import path
from dotenv import load_dotenv
from docopt import docopt
from typing import List


def get_dirs(root: str) -> List[str]:
    """Returns a list of sub-directories from a root directory (non-recursively)."""
    return [path.join(root, folder) for folder in os.listdir(root) if path.isdir(root + "/" + folder)]

def preflight_check():
    myCmd = f'mktorrent -h > /dev/null'
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

def make_torrent(TO, TRACKER, ANNOUNCE_URL, PATH):
    print(f'making a torrent for {PATH}')
    myCmd = f'cd "{TO}"; mktorrent -l 18 -p -s {TRACKER} -a {ANNOUNCE_URL} "{PATH}"'
    print(myCmd)
    os.system(myCmd)

if __name__ == "__main__":
    load_dotenv()
    ANNOUNCE_URL = os.getenv("ANNOUNCE_URL")
    TRACKER = os.getenv("TRACKER")
    FROM = os.getenv("FROM")
    TO = os.getenv("TO")

    if not ANNOUNCE_URL:
        raise "Need an announce url. Set this in a .env file."

    """ Only handle directories at this time. Could tweak this to be conditional"""
    dirs = get_dirs(FROM)
    preflight_check()

    print("Running bulk-mktorrent\n\n")

    print(f'There are {len(dirs)} folders we can create torrents from.')

    print(f'Creating a torrent for each of the files/folders in {FROM} to {TO}\n')
    for PATH in dirs:
        make_torrent(TO, TRACKER, ANNOUNCE_URL, PATH)



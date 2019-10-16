"""

Usage:
    main.py [options]

Options:
    -f --folder=<name>    Folder to make torrents from.

"""

import os
from dotenv import load_dotenv
from docopt import docopt

if __name__ == "__main__":
    load_dotenv()
    arguments = docopt(__doc__)

    folder = arguments['--folder']
    ANNOUNCE_URL = os.getenv("ANNOUNCE_URL")

    if not ANNOUNCE_URL:
        raise "Need an announce url. Set this in a .env file."
    if not folder:
        raise "Need a folder"

    myCmd = 'mktorrent -l 18 -p -s OPS -a ANNOUNCE_URL ~/music/torrent_folder -o torrent_filename.torrent'
    #os.system(myCmd)
    os.system('pwd')

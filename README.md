# bulk-mktorrent

"Finally, I can reup all my shit, again!"

## Usage:
    main.py <rootdir>

This will take all folders inside <rootdir> and create a torrent for each one. Does not go deeper than the first level.

I recommend running this from the directory that you want the torrent files
to be in. E.g.:

```
  cd ~/mytorrentfiles
  ~/bulk-mktorrent/main.py ~/mymusicfolder/
```

## Install

I'm going to pretend you have no python experience.

0. **Install mktorrent:** https://github.com/Rudde/mktorrent
1. Check which python you have.
2. Install virtualenv.
3. Clone this repo.
4. Go into this repo.
5. Create a virtualenv for this repo.
6. Enter the virtualenv.
7. Install the requirements.
8. Copy .env.example to .env

```
python --version
python3 --version
pip install virtualenv
git clone git@github.com:tendermario/bulk-mktorrent.git
cd bulk-mktorrent
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

9. **Update `.env` file to have YOUR announce URL.**

## Notes:

- If you get stuck with a ton of .torrent files you want to delete, use the
handy command:

`rm *.torrent`

- `-o` in mktorrent's cli tool does not seem to work to target a directory for the torrents output location, so unfortunately, these torrents will be created in the current directory for now. Maybe we can move all these files after they are created one day.

- Probably doesn't work with things with double quotations in the names right now.

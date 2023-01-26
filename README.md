<h1 align="center">
	<img width="400" src="media/logo.png" alt="bulk-mktorrent">
</h1>

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

0. **Install mktorrent:** https://github.com/pobrn/mktorrent
1. Check which python you have.
2. Install virtualenv.
3. Clone this repo.
4. Go into this repo.
5. Create a virtualenv for this repo.
6. Enter the virtualenv.
7. Install the requirements.
8. Copy .env.example to .env

Steps 1-8:

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

- If you mess up and get stuck with a ton of .torrent files and want to delete them all from the current directory, use the handy command:

`rm *.torrent`

- `-o` in mktorrent's cli tool does not seem to work to target a directory for the torrents output location, so unfortunately, these torrents will be created in the current directory for now. Maybe we can move all these files after they are created one day.

- Probably doesn't work with things with double quotations in the names right now.

- Why only first level? This makes us avoid making a torrent for CD1, CD2, and suits my needs. If you think having multiple levels would be nice, feel free to make a PR.

- Logo made from 30 seconds of tinkering with, and therefore courtesy of, http://recursivedrawing.com

# bulk-mktorrent

"Finally, I can reup all my shit, again!"

Usage:
    `main.py <rootdir>`


I recommend running this from the directory that you want the torrent files
to be in. E.g.:

```
  cd ~/mytorrentfiles
  ~/bulk-mktorrent/main.py ~/mymusicfolder/
```

## Notes:

If you get stuck with a ton of .torrent files you want to delete, use the
handy command:

  rm *.torrent

-o does not seem to work to target a directory for the torrents output
location, so unfortunately, these torrents will be created in the current
directory for now. Maybe we can move all these files after they are created
one day.

Probably doesn't work with things with double quotations in the names right now.

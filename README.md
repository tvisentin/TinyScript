# renameSeriesTitle.py
This script should rename your series to a better form:<br />
`"[No.team].the.handmaids.tales.2017.S01E01.yzx.avi" => "The Handmaids Tales - S01E01.avi"`<br />
`"[NO.TEAM].THE.HANDMAIDS.TALES.E01.avi" => "The Handmaids Tales - E01.avi"`<br />
`"The.Handmaids.Tales.-.01.avi" => "The Handmaids Tales - 01.avi"`

## How it works ?

`git clone https://github.com/tvisentin/renameSeriesTitle.git ~/your/path/renameSeriesTitle`<br />
`$> alias rename='python3 ~/your/path/renameSeriesTitle/renameSeriesTitle.py'`<br />

Go to `renameSeriesTitle.py` and put one or more path to store your files in place of the `pathToMoveX` variable.<br />
If you don't want to change your path, set the `pathToMove` to empty:<br />
`pathToMove = []`<br />
You can also add more ignore words when you set `ignore` variable.<br />

Then, you can go to the folder or stay where you here and type the path.<br />
`$> rename *`<br />
After that, you have to say `y` for valid each files, `Y` for all files or `n`/ `N` to discard changes.<br />
And you can move files changed when you press the number corresponding to the path.<br />
`Where do you want to move your files ?`<br />
`1 -> /First/Path`<br />
`2 -> /Second/Path`<br />
`3 -> etc.`<br />
`Type the number you choose.`<br />
`$> 1`<br />
`Files are moved ! :)`<br />

# renameTitle.py
This script should rename your series to a better form:<br />
`"[No.team].the.handmaids.tales.2017.S01E01.yzx.avi" => "The Handmaids Tales - S01E01.avi"`<br />
`"[NO.TEAM].THE.HANDMAIDS.TALES.E01.avi" => "The Handmaids Tales - E01.avi"`<br />
`"The.Handmaids.Tales.-.01.avi" => "The Handmaids Tales - 01.avi"`

## How it works ?

`git clone https://github.com/tvisentin/renameTitle.git ~/Documents/renameTitle`
`$> alias rename='python3 ~/Documents/renameTitle/renameTitle.py'`<br />
Then, you can go to the folder or stay where you here and type the path.<br />
`$> rename *`<br />
After that, you have to say `y` for valid each files or `n` to discard changes.

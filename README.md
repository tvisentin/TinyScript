# renameTitle.py
This script should rename your series to a better form:<br />
`"[No.team].the.handmaids.tales.S01E01.yzx.avi" => "The Handmaids Tales - S01E01.avi"`<br />
`"[NO.TEAM].THE.HANDMAIDS.TALES.E01.avi" => "The Handmaids Tales - E01.avi"`<br />
`"The.Handmaids.Tales.01.avi" => "The Handmaids Tales - 01.avi"`

## How it works ?

`$> alias rename='python3 renameTitle.py'`<br />
Then, go to the folder you want to change.<br />
`$> rename *`<br />
But be careful, if your files is not formatted with `.`, this can broke your files.

import sys, re, os
import getch

pattern = re.compile("([s|S]\d+)?([e|E])?\d+$")
print ("If you want to change your files:")
print ("y => yes, n => no")
for arg in sys.argv[1:]:
    toRename = arg
    toSave = ""
    if arg.find('[') != -1:
        delete = arg.find(']')
        arg = arg[delete+2:]
    arg = arg.lower().title().split('.')
    for string in arg:
        match = pattern.match(string)
        if match:
            toSave += "- "
            string.upper()
            toSave += string
            toSave += "." + arg[-1].lower()
            print (toSave)
            gets()
            break
        toSave += string
        toSave += ' '
    char = getch.getche()
    if (char == 'y' or char == 'Y'):
        os.rename(toRename, toSave)
    if (char == 'n' or char == 'N'):
        print ("File is not changed")

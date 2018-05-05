import sys, re, os

pattern = re.compile("([s|S]\d+)?([e|E])?\d+$")
yesAll = 'n'
print ("If you want to change your file says yes (y) or no (n): ")
for arg in sys.argv[1:]:
    toRename = arg
    toSave = ""
    if arg[0] == '[':
        delete = arg.find(']')
        arg = arg[delete+2:]
    if arg.find('/'):
        delete = arg.rfind('/')
        arg = arg[delete+1:]
    arg = arg.lower().title().replace('.', ' ').split(' ')
    for string in arg:
        match = pattern.match(string)
        if string.isdigit() and int(string) > 1900 and int(string) < 2100:
            continue
        elif string == "-" or string == "Neatsubs":
            continue # Add more subteam here
        elif match:
            toSave += "- "
            string.upper()
            toSave += string
            toSave += "." + arg[-1].lower()
            print (toSave)
            break
        else:
            toSave += string
            toSave += ' '
    if (yesAll != 'Y'):
        char = input("== ")
    if (char == 'y'):
        os.rename(toRename, toSave)
        print ("File is changed")
    elif (char == 'Y'):
        yesAll = 'Y'
        os.rename(toRename, toSave)
        print ("File is changed")
    else:
        print ("File is not changed")

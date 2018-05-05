import sys, re, os

pattern = re.compile("([s|S]\d+)?([e|E])?\d+$")
print ("If you want to change your file says yes (y) or no (n): ")
for arg in sys.argv[1:]:
    toRename = arg
    toSave = ""
    if arg.find('[') != -1:
        delete = arg.find(']')
        arg = arg[delete+2:]
    arg = arg.lower().title().replace('.', ' ').split(' ')
    for string in arg:
        match = pattern.match(string)
        if string.isdigit() and int(string) > 1900 and int(string) < 2100:
            continue
        elif string == "Neatsubs" or string == "-":
            continue
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
    char = input("== ")
    if (char == 'y' or char == 'Y'):
        os.rename(toRename, toSave)
        print ("File is changed")
    if (char == 'n' or char == 'N'):
        print ("File is not changed")

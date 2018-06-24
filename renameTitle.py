import sys, re, os, shutil
from pathlib import Path

pathToMove = ["/Users/Transmetropolitan/Movies/Thomas/", "/Users/Transmetropolitan/Movies/Lilly/"]
ignore = ["Neatsubs", "Definitelynotme", "Godotaku", "Despair", "Paradise", "Nofun", "Marvels"] # Add more subteam here
extension = ["mp4", "mkv", "avi"]
yesAll = False
noAll = False
new = []
prev = []
pattern = re.compile("([s|S]\d+)?([e|E]|Ep)?\d+$")
for arg in sys.argv[1:]:
    prev.append(arg)
    toSave = ""
    if arg[0] == '[':
        delete = arg.find(']')
        arg = arg[delete+2:]
    elif arg[0] == '(':
        delete = arg.find(')')
        arg = arg[delete+2:]
    if arg.find('/'):
        delete = arg.rfind('/')
        arg = arg[delete+1:]
    ex = arg.rfind(".")
    if arg[ex + 1:] not in extension:
        prev.pop()
        continue
    else:
        arg = list(filter(None, arg.lower().title().replace('.', ' ').replace('_', ' ').replace('-', ' ').split(' ')))
        for string in arg:
            match = pattern.match(string)
            if (string.isdigit() and int(string) > 1900 and int(string) < 2100) or (string in ignore):
                continue
            elif arg[0] == "The" and string == "100" and string == arg[1]: # Special case for The 100
                toSave += string + ' '
            elif match and string != arg[0]:
                string.upper()
                toSave += "- " + string + "." + arg[-1].lower()
                break
            else:
                toSave += string + ' '
        new.append(toSave)

if not new:
    print ("Nothing to change.")
    exit(1)
if len(new) > 1:
    print("----- All files -----")
    for string in new:
        print (string)
    print("----- --------- -----")
print ("If you want to change type [y]/[n]/[Y] (Y/N will change every file): ")
i = 0
while i < len(new):
    print ("Prev: " + (prev[i]))
    print ("New : " + (new[i]))
    if yesAll != True and noAll != True:
        char = input("$> ")
    if char == 'Y':
        yesAll = True
        os.rename(prev[i], new[i])
        print ("Files are changed")
    elif char == 'y':
        os.rename(prev[i], new[i])
        if yesAll != True:
            print ("File is changed")
    elif char == 'N':
        noAll = True
        print ("Files aren't changed")
        exit(1)
    else:
        new.pop()
        prev.pop()
        print ("File isn't changed")
    i += 1

if len(pathToMove) == 0 or len(new) == 0:
    print ("This is the end ! :)")
    exit(1)
print ("Where do you want to move your files ?")
print ("0 -> Don't move")
for idx, folder in enumerate(pathToMove, start=1):
    print (str(idx) + " -> " + folder)
print ("Take the number corresponding to the right folder.")
idx = input("$> ")
if idx.isdigit() and int(idx) <= int(len(pathToMove)) and int(idx) > 0:
    for toMove in new:
        myFile = Path(toMove)
        if myFile.is_file():
            shutil.move(toMove, pathToMove[int(idx) - 1] + toMove)
    if len(new) == 1:
        print ("File is moved ! :)")
    else:
        print ("Files are moved ! :)")
else:
    if len(new) == 1:
        print ("File remain ! :)")
    else:
        print ("Files remain ! :)")
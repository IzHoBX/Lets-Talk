import pickle

CODE_PREFIX = "<td class=\"code\"><a href=\""
NAME_PREFIX = "<td class=\"name\">"
CLOSING_TAG = "</td>"
INVALID_CHAR = "⊛ "

f = open("FullTable.html")

nameToCode = {}
codeToName = {}
foundCode = False
codeTemp = ""
nameTemp = ""

for line in f:
    if not foundCode and CODE_PREFIX in line:
        codeTemp = ""
        for i in range(len(CODE_PREFIX), len(line)):
            if line[i] == "\"":
                break
            else:
                codeTemp += line[i]
        foundCode = True
    elif foundCode and NAME_PREFIX in line:
        nameTemp = ""
        for i in range(line.find(NAME_PREFIX)+len(NAME_PREFIX), len(line)):
            if line[i] == '<':
                break
            else:
                nameTemp += line[i]
        if INVALID_CHAR in nameTemp:
            nameTemp = nameTemp[nameTemp.find(INVALID_CHAR)+len(INVALID_CHAR):]
        nameToCode[nameTemp] = codeTemp
        codeToName[codeTemp] = nameTemp
        foundCode = False

print("Done, found: " + str(len(nameToCode)))
print("Done, found: " + str(len(codeToName)))
pickle.dump([nameToCode, codeToName], open("emojilib", "wb"))
f.close()

f = open("table.csv", "w")
for name, code in nameToCode.items():
    f.write(name+","+code+"\n")
f.close()

from pprint import pprint
from re import search
from json import dumps
PATH = './data/'
FILES = ['a. JAN.md', 'b. FEB.md', 'c. MARCH.md', 'd. APRIL.md', 'e. MAY.md', 'f. JUNE.md',
         'g. JULY.md', 'h. AUGUST.md', 'i. SEPT.md', 'j. OCT.md', 'k. NOV.md', 'l. DEC.md']

# FILES = ['a. JAN.md']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


def getNameAndLink(str):
    name = search(r"\[(.*?)\]", str)[0][1:-1]
    link = search(r"\((.*?)\)", str)[0][1:-1]
    # print(name, link)
    return name, link

def parseLines(line):
    opportunity = {}
    try: 
        items = line.split('|')
        opportunity['name'], opportunity['link'] = getNameAndLink(items[0].strip())
        opportunity['deadline'] = items[1].strip()
        opportunity['type'] = items[2].strip()
    except:
        pprint('Error processing line', line)
        pass
    return opportunity

def readMd(filename):
    print(filename)
    with open(filename, 'r') as f:
            lines = f.readlines()
            return [parseLines(line) for line in lines[4:]]
            # for i, line in enumerate(lines[4:]):
            #     if len(line.strip()) is not 0:
            #         pprint(parseLines(line))

allOpps = []
for i, file in enumerate(FILES):
    allOpps.extend(readMd(PATH+file))

with open("public/opportunities.json", "w") as outfile: 
    outfile.write(dumps(allOpps, indent=4))

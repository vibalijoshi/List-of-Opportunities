#
# Read md files and parse them
#
from pprint import pprint

PATH = './old/'
FILES = ['a. JAN.md', 'b. FEB.md', 'c. MARCH.md', 'd. APRIL.md', 'e. MAY.md', 'f. JUNE.md',
         'g. JULY.md', 'h. AUGUST.md', 'i. SEPT.md', 'j. OCT.md', 'k. NOV.md', 'l. DEC.md']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


def parseLines(line):
    # split by | and create a dictionary

    opportunity = {}
    items = line.split('|')[1:]
    try:
        opportunity['name'] = items[0].strip()
        opportunity['deadline'] = items[1].strip()
        opportunity['type'] = items[2].strip()
        opportunity['link'] = items[3].strip()

        return opportunity
    except:
        print(line)
        return None


def getOpportunities(filename):
    # read file contents in python
    with open(filename, 'r') as f:
        lines = f.readlines()[2:]
        return [parseLines(line) for line in lines]


def parseLink(link):
    # extract link from markdown style links
    try:
        return link.split('](')[1].split(')')[0]
    except:
        return link


def writeFile(opportunities, month, filename):
    with open(filename, 'w') as f:
        f.write('# {}\n\n'.format(month))

        f.write('Opportunity|Deadline|Type\n')
        f.write('----|-----|-----\n')
        for opportunity in opportunities:
            f.write('[{}]({}) | {} | {}\n'.format(
                opportunity['name'],
                parseLink(opportunity['link']),
                opportunity['deadline'],
                opportunity['type']
            ))


for index, file in enumerate(FILES):
    print(index, file)
    opp = getOpportunities(PATH+file)
    writeFile(opp, MONTHS[index], file)

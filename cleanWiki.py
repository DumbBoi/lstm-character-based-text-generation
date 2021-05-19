import os
import string
import re

def filter(x):
    if 'list of' in x:
        return False
    return True

def repl(m):
    return m.group().replace(',', '')

def fixth(m):
    return f'{m.group(0)[0]} {m.group(0)[1:]}'

def nums(m):
    return f'{m.group(0)[0]} {m.group(0)[1:]}'

def puntuationfix(m):
    chrs = m.group()
    if chrs[0].isdigit() and chrs[2].isdigit():
        return (''.join(chrs))
    return ' '.join(chrs)

wikiData = open('./wiki.txt', 'r').read().split('\n')
wikiData = [w for w in wikiData if filter(w.lower())]

wikiData = [' '.join([w for w in W.split(' ')][1:]) for W in wikiData]

wikiSummary = ' . '.join(wikiData)

wikiSummary = re.sub('<.+>', '', wikiSummary)

wikiSummary = wikiSummary + ' '
wikiSummary = wikiSummary#[:500]

wikiSummary = wikiSummary.encode('ascii', 'ignore').decode()
wikiSummary = re.sub('\d,\d', repl, wikiSummary)
wikiSummary = re.sub('@', ' ', wikiSummary)

wikiSummary = re.sub('\dth', fixth, wikiSummary)

wikiSummary = re.sub('((.|\s){1})([\(\)\.,;:\[\]\{\}\'\"\!\?\-\$\%/])((.|\s){1})', puntuationfix, wikiSummary)
wikiSummary = re.sub('((.|\s){1})([\(\)\.,;:\[\]\{\}\'\"\!\?\-\$\%/])((.|\s){1})', puntuationfix, wikiSummary)


wikiSummary = re.sub('\s+', ' ', wikiSummary)
wikiSummary = wikiSummary.lower()

totalSize = len(wikiSummary)

for n, i in enumerate(range(0, totalSize, 20000)):
    with open(f'./wiki data/data_{n}.txt', 'w+') as outputFile:
        outputFile.write(wikiSummary[i: i + 20000])
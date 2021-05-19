import os
import re
import requests
import string
import wikipedia

countries = open('./countries.lst', 'r').read().split('\n')
countries = [c.replace(' ', '_') for c in countries][133:]
wikipedia.set_lang('en')

def repl(m):
    return m.group().replace(',', '')

def fixth(m):
    return f'{m.group(0)[0]} {m.group(0)[1:]}'

def puntuationfix(m):
    chrs = m.group()
    # print(list(chrs))
    if chrs[0].isdigit() and chrs[2].isdigit():
        return (''.join(chrs))

    return ' '.join(chrs)

total = len(countries)
for n, country in enumerate(countries):
    print(f'{n}\{total} {country}\r', end = '')
    
    if not os.path.isdir(f'./data/{country}/'):
        os.mkdir(f'./data/{country}/')

    # wikiSummary = wikipedia.summary(country) + ' '
    wikiSummary = wikipedia.WikipediaPage(country)
    wikiSummary = wikiSummary.summary + ' '

    wikiSummary = wikiSummary.encode('ascii', 'ignore').decode()
    wikiSummary = re.sub('\d,\d', repl, wikiSummary)

    wikiSummary = re.sub('\dth', fixth, wikiSummary)
    wikiSummary = re.sub('((.|\s){1})([\(\)\.,;:\[\]\{\}\'\"\!\?\-\$\%/])((.|\s){1})', puntuationfix, wikiSummary)
    wikiSummary = re.sub('((.|\s){1})([\(\)\.,;:\[\]\{\}\'\"\!\?\-\$\%/])((.|\s){1})', puntuationfix, wikiSummary)

    wikiSummary = re.sub('\s+', ' ', wikiSummary)
    wikiSummary = wikiSummary.lower()

    with open(f'./data/{country}/summary.txt', 'w+') as outputFile:
        outputFile.write(wikiSummary)
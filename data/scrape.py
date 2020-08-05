# obtain data for neural network
# take from basketball reference
from bs4 import BeautifulSoup
from requests import get

# take data between all mvps
urls = [
    'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_per_game.html' for x in range(1956, 2020)
]
for url in urls:
    print(url)
print(len(urls))

test = 'https://www.basketball-reference.com/leagues/NBA_1958_per_game.html'

response = get(test)
soup = BeautifulSoup(response.text, 'html.parser')

header_str = "Player	Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	2P	2PA	2P%\teFG%\tFT	FTA	FT%	ORB	DRB	TRB	" \
          "AST	STL	BLK	TOV	PF	PTS "
headers = [header.strip() for header in header_str.split('\t')]

table = soup.find_all('td')
tables = [''.join(e for e in t.text if e.isalnum()) for t in table]

print(len(tables))
print(len(tables)/len(headers))

l = [{headers[i]: tables[x:x+len(headers)][i] for i in range(0, len(headers))} for x in range(0, len(tables), len(headers))]
for item in l:
    print(item)
print(len(l))
print(len(l[0]))

print('end')

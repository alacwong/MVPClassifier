# script to scrape mvp data
urls = [
    'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_per_game.html' for x in range(1971, 2020)
]

for url in urls:
    print(url)

print(len(urls))
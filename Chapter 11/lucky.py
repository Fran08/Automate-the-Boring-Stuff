#! python3
# lucky.py - Opens several Google search results.

import webbrowser, sys, requests, bs4

print('Googling...')
res = requests.get(f'http://google.com/search?q={" ".join(sys.argv[1:])}')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
link_elems = soup.select('.r a')
num_open = min(5, len(link_elems))

for i in range(num_open):
    webbrowser.open(f"http://google.com{link_elems[i].get('href')}")

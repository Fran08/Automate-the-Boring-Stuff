#! python3
# link_verification.py - Downloads all URL's inside a webpage and flags pages
# with a 404 "Not Found" status code and print them out as broken links.

import requests, bs4

print('What website do you want to verify links for?')
website = input()

res = requests.get(website)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
links = soup.select('a')

for link in links:
    link = link.get('href')

    try: 
        res = requests.get(link)
        
        if res.status_code == 404:
            print(f'404 error for: {link}')

        else:
            print(f'Working link: {link}')

    except:
        continue

print(f'Finished checking.')
    

    

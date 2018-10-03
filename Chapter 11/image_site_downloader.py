#! python3
# image_site_downloader.py - Takes a search input and downloads all image files
# (PNG, JPEG) to a new folder in current directory
# Unfortunately this only downloads the first 60 search results
# If anyone knows the solution to this, please inform!

import requests, os, bs4

print('What do you want to search for?')
search = input()

url = f'https://imgur.com/search?q={search}'
dir_name = f'imgur\\{search}'
os.makedirs(f'{dir_name}', exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
image_elem = soup.select('.post .image-list-link img')

if len(image_elem) == 0:
    print('No images found')

else:
    for i, image in enumerate(image_elem):
        
        image_url = f"https:{image_elem[i].get('src')}"

        print(f'Downloading image {image_url}') 
        res = requests.get(image_url)
        res.raise_for_status()

        image_file = open(os.path.join(dir_name, os.path.basename(image_url)), 'wb')
        print(image_file)
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()

    print('Done')

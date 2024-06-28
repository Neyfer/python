from googleapiclient.discovery import build
import requests
import os

# Replace 'your_api_key' and 'your_cse_id' with your actual API key and Custom Search Engine ID
api_key = 'AIzaSyBYAHKwIVlrDxdGN50rgKsMrK7mCOcwfjI'
cse_id = 'a58e7df8b85c34226'
counter = 1

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, searchType='image', **kwargs).execute()
    return res

items_to_search = ['Python logo', 'JavaScript logo', 'HTML logo']  # Your list of search terms

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

for item in items_to_search:
    results = google_search(item, api_key, cse_id)
    if 'items' in results:
        image_url = results['items'][0]['link']  # Assumes the first image is what you want
        file_extension = image_url.split('.')[-1]
        filename = f"image{counter}.{file_extension}"
        counter += 1
        download_image(image_url, filename)
        print(f"Downloaded {filename}")

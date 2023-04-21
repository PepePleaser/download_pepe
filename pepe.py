import json
import requests
import os
from urllib.parse import urlparse
from googleapiclient.discovery import build

API_KEY = 'YOUR-GOOGLE-SEARCH-API-KEY'
CUSTOM_SEARCH_ENGINE_ID = 'YOUR-GOOGLE-SEARCH-ENGINE-ID'

def get_image_urls(query, api_key, custom_search_engine_id, num_results=200):
    service = build("customsearch", "v1", developerKey=api_key)
    urls = []

    for i in range(0, num_results, 10):
        result = service.cse().list(q=query, cx=custom_search_engine_id, searchType='image', num=10, start=i+1,
                                     imgSize='LARGE', sort='date').execute()
        if 'items' in result:
            urls.extend([item['link'] for item in result['items']])

    return urls

def download_image(url, output_dir):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    filename = os.path.basename(urlparse(url).path)
    output_path = os.path.join(output_dir, filename)

    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def download_images_from_json(json_file, output_dir):
    with open(json_file, 'r') as f:
        image_data = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for url in image_data['urls']:
        try:
            download_image(url, output_dir)
            print(f'Downloaded image: {url}')
        except Exception as e:
            print(f'Error downloading image {url}: {str(e)}')

if __name__ == '__main__':
    query = 'happy pepe frog meme'
    img_urls = get_image_urls(query, API_KEY, CUSTOM_SEARCH_ENGINE_ID)

    json_file = 'pepe.json'
    with open(json_file, 'w') as f:
        json.dump({'urls': img_urls}, f)

    output_dir = 'downloaded_images'
    download_images_from_json(json_file, output_dir)

import requests
from bs4 import BeautifulSoup
import os

def download_urls_from_html(html_code, output_folder):
    soup = BeautifulSoup(html_code, 'html.parser')
    urls = set()

    # Find all anchor tags (links)
    for a_tag in soup.find_all('a', href=True):
        url = a_tag['href']
        urls.add(url)

    # Download content from each URL and save to the output folder
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                filename = os.path.join(output_folder, os.path.basename(url))
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {url}")
            else:
                print(f"Failed to download: {url}")
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

if __name__ == "__main__":
    file_path = "htmlcode.txt"
    output_folder = "downloads"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(file_path, 'r') as file:
        html_code = file.read()

    download_urls_from_html(html_code, output_folder)

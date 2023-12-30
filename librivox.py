import requests
import re
from pathlib import Path



response = requests.get("https://librivox.org/api/feed/audiobooks")
xml = response.text

# cache the file so we dont send too many requests to the XML feed
file_path = Path("librivox-xml-audiobooks-feed.txt")
if file_path.exists():
    print(f"The file path {file_path} exists. Using cached feed.")
else:
    print(f"The file path {file_path} does not exist.")
    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Write the text string to the file
        file.write(xml)

def get_url_zip_files(xml):
    pattern = r'<url_zip_file>(.*?)<\/url_zip_file>'
    matches = re.findall(pattern, xml)
    if matches:
        return matches
    
def get_url_text_source(xml):
    pattern = r'<url_text_source>(.*?)<\/url_text_source>'
    matches = re.findall(pattern, xml)
    if matches:
        return matches    

def get_description(xml):
    pattern = r'<description>(.*?)<\/description>'
    matches = re.findall(pattern, xml)
    if matches:
        return matches

def get_title(xml):
    pattern = r'<title>(.*?)<\/title>'
    matches = re.findall(pattern, xml)
    if matches:
        return matches
    
def get_books(xml):
    pattern = r'<book>(.*?)<\/book>'
    matches = re.findall(pattern, xml)
    if matches:
        return matches
    
def get_ids(xml):
    pattern = r'<id>(.*?)<\/id>'
    matches = re.search(pattern, xml)
    if matches:
        return matches.group(1)    
    

def extract_data(xml):
    books = get_books(xml)
    data = {}
    for book in books:
        id = get_ids(book)
        file = get_url_zip_files(book)
        text = get_url_text_source(book)
        description = get_description(book)
        title = get_title(book)

        data[id] = {}
        data[id]['file'] = file.pop()
        data[id]['text'] = text.pop()
        data[id]['description'] = description.pop()
        data[id]['title'] = title.pop()
    return data


def main():
    data = extract_data(xml)
    # text: https://www.gutenberg.org/cache/epub/744/pg744.txt
    print(data['127'])

if __name__ == "__main__":
    main()
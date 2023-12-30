import requests
from pathlib import Path
import zipfile


zip_file_url = "https://www.archive.org/download/golden_mean_to_5000_digits_0810_librivox/golden_mean_to_5000_digits_0810_librivox_64kb_mp3.zip"

# Specify the local file name for saving the downloaded zip file
local_file_path = "golden_mean_to_5000_digits_0810_librivox_64kb_mp3.zip"

file_path = Path(local_file_path)
if file_path.exists():
    print(f"The file path {file_path} exists. Unzipping...")
    # Specify the directory where you want to extract the contents
    extracted_dir = "extracted_contents"

    # Open the zip file in read mode
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        # Extract all contents to the specified directory
        zip_ref.extractall(extracted_dir)

    print(f"Contents of {file_path} extracted to {extracted_dir}")
else:
    print(f"The file path {file_path} does not exist.")
    # Make a GET request to the URL
    response = requests.get(zip_file_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the file in write mode ('w')
        with open(file_path, 'wb') as file:
            # Write the text string to the file
            file.write(response.content)
        print(f"Zip file downloaded successfully and saved to {local_file_path}")    
    else:
        print(f"Failed to download the zip file. Status code: {response.status_code}")
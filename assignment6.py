import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Step 1: Prompt user for URL
    url = input("Enter the image URL: ").strip()
    
    # Step 2: Create directory
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Step 3: Fetch image
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Raise error for HTTP codes (e.g., 404)

        # Step 4: Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If no filename in URL
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Final file path
        file_path = os.path.join(folder, filename)

        # Step 5: Save image in binary mode
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch image: {e}")

if __name__ == "__main__":
    fetch_image()

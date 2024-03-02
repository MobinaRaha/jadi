import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get("https://divar.ir/s/tehran/electronic-devices")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all occurrences of the term "iphone" in the visible text content
    iphone_occurrences = soup.find(text=lambda text: text and 'iphone' in text.lower())
    
    # Print out the found occurrences
    for occurrence in iphone_occurrences:
        print(occurrence)
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)

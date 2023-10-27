import requests
from bs4 import BeautifulSoup

# URL of the page with the button
url = "https://www.goodreads.com/book/show/44767458-dune"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div element containing the button by class name
button_container = soup.find('div', class_='Button__container--block')

# Extract the button element from the div container
button_element = button_container.find('button')

# Extract the link (data-href attribute) from the button element
if button_element and 'data-href' in button_element.attrs:
    link = button_element['data-href']
    print("Link: ", link)
else:
    print("Button not found or does not have a data-href attribute.")


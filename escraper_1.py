""" Election Scraper """
import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=531758&xvyber=2102"
CSV_FILE = "vysledky_srbsko"

def get_region_number(url : str) -> str:
    """ Extract the number of the region from URL """
    return url[url.index('ps2017nss')+10:url.index('?')]

def save_html_data(url : str, content : str) -> None:
    """ Save the data from the webpage into file for next """
    with open(get_region_number(url)+'_data_html', mode='w', encoding='UTF-8') as f:
        f.write(content)

def read_html_data(url : str) -> str:
    """ Reads saved data """
    with open(get_region_number(url)+'_data_html', mode='r', encoding='UTF-8') as f:
        return f.read()
    
def extract_text(table_header) -> str:
    """ Returns header text even formatted by html tags """
    # pure_text = table_header[table_header.index('>'):-table_header.index('<')]
    pure_text = table_header[5:15]
    return pure_text

# Send a GET request if it is first time
if os.path.isfile(get_region_number(URL)+'_data_html'):
    print("- data file exists")
    html_data = read_html_data(URL)
    print("- data read")
else:
    print("- data file does not exists")
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print("- GET request successful")
            # Save HTML file
            save_html_data(URL, response.text)
            html_data = response.text
            print("- data saved")
        else:
            print("- GET request failed")
    except requests.exceptions.Timeout:
        print("- GET request timed out")

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')
# Look for table
table_tab = soup.find('table', {'id': get_region_number(URL)+'_t1'})
table_rows = [
    table_tab.find_all("tr")
]
# Find all 'th' tags
headers = soup.find_all('th')
# Extract and print the text from each 'th' tag
for header in headers:
    print(header)
    print(extract_text(header))


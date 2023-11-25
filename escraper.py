""" Election Scraper """
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102"
URL_V = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=599417&xvyber=2102"
CSV_FILE = "vysledky_beroun"
EMPTY_HTML = '<html> </html>'
VILLAGE_URL_BASE = 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec='
REGION, VILLAGE = 0, 1
SELECTED_COLUMNS = ['ČÍSLO','OBEC','POČET VOLIČŮ','VYDANÉ OBÁLKY','PLATNÉ HLASY']

def get_region_number(url : str) -> str:
    """ Extract the number of the region from URL """
    return url[url.index('numnuts')+8:]

def save_html_data(content : str, org_code: str) -> None:
    """ Save the data from the webpage into file for next """
    with open('z_'+org_code+'_data.html', mode='w', encoding='UTF-8') as f:
        f.write(content)

def read_html_data(org_code: int) -> str:
    """ Reads saved html data """
    with open('z_'+org_code+'_data.html', mode='r', encoding='UTF-8') as f:
        return f.read()

def get_village_url(election_region_code: str, election_village_code: str) -> str:
    """ Compose the URL with election results for specific village"""
    return f"{VILLAGE_URL_BASE}{election_village_code}&xvyber={election_region_code}"

def get_html_data(url: str, org_entity: str) -> str:
    """ Downloads the requested web page (if not done already) """
    # Send a GET request if it is first time
    if os.path.isfile('z_'+org_entity+'_data.html'):
        # print("- data file exists")
        html_data = read_html_data(org_entity)
    else:
        print("- data file does not exists")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                # print("- GET request successful")
                save_html_data(response.text, org_entity)
                html_data = response.text
            else:
                # print("- GET request failed")
                html_data = EMPTY_HTML
        except requests.exceptions.Timeout:
            # print("- GET request timed out")
            html_data = EMPTY_HTML
    return html_data

def get_villages_list(page_tables) -> []:
    """ Get full list of vilages as dict """
    result_list = []
    # Get data from all tables on page
    for table in (page_tables):
        for rows in table.find_all('tr'):
            rows_data = [td.text for td in rows.find_all('td')]
            if len(rows_data):
                if rows_data[0].isnumeric():
                    result_list.append([rows_data[0], rows_data[1]])
    return result_list

def get_village_results(village_code: str, village_name: str, page_tables):
    """ Function is returning two lists - list of headers and list of results for specific village """
    # Pickup data from tables
    village_general_data = [] # Number of voters, envelopes issued, valid votes - 3, 4, 7
    list_of_parties = []
    votes_received = []
    for counter, table in enumerate(page_tables):
        for row in table.find_all('tr'):
            if row.find('td'):
                row_data = [td.text.replace('\xa0','').replace(',','.') for td in row.find_all('td')]
                if not counter: # First table is including general data
                    village_general_data= [row_data[3], row_data[4], row_data[7]]
                else: # Other tables contains results of parties
                    list_of_parties.append(row_data[1])
                    votes_received.append(row_data[2])
    headers_list = SELECTED_COLUMNS + list_of_parties
    data_list = [village_code, village_name]+village_general_data + votes_received
    return headers_list, data_list

# What region we are looking for?
REGION_NO = get_region_number(URL)
# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(get_html_data(URL, REGION_NO), 'html.parser')
village_list = get_villages_list(soup.find_all('table'))
header_list = []
data_list = []

# Get the election results from all villages in the region
for cnt, village in enumerate(village_list):
    # Compose link to data for specific village
    village_code, village_name = village
    village_url = get_village_url(REGION_NO, village_code)
    # Parse the page and get table(s)
    soup = BeautifulSoup(get_html_data(village_url, village_code), 'html.parser')
    table_tabs = soup.find_all('table')
    # Get list of headers and list of data from the tables
    v_header, v_data = get_village_results(village_code, village_name, table_tabs)
    # Get Header if it is first time
    if not cnt:
        header_list = v_header
    data_list.append(v_data)

# Save to CSV using pandas
df = pd.DataFrame(data_list, columns=header_list)
# Save the DataFrame as a CSV file
df.to_csv('#output.csv', index=False)




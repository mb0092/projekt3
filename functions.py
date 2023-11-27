""" Election Scraper Functions """
import os
import requests
from bs4 import BeautifulSoup

# URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102"
# URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
# URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7105"
# CSV_FILE = "vysledky_voleb.csv"

# Const.
EMPTY_HTML = """<!doctype html>\n<html>\n<body>\n<h3>
Page not found!
</h3>\n</body>\n</html>
"""
URL_VERIFY = "volby.cz/pls/ps2017nss"
EXT_VERIFY = ".csv"
VILLAGE_URL_BASE = 'https://www.volby.cz/pls/ps2017nss/'
SELECTED_COLUMNS = ['ČÍSLO','OBEC','POČET VOLIČŮ','VYDANÉ OBÁLKY','PLATNÉ HLASY']

# Functions
def get_village_url(election_village_link: str) -> str:
    """ Compose the URL with election results for specific village"""
    return f"{VILLAGE_URL_BASE}{election_village_link}"

def get_html_data(url: str) -> str:
    """ Downloads the requested web page """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            html_data = response.text
        else:
            html_data = EMPTY_HTML
    except requests.exceptions.Timeout:
        html_data = EMPTY_HTML
    return html_data

def get_villages_list(v_url: str) -> []:
    """ Get full list of vilages as dict """
    html_soup = BeautifulSoup(get_html_data(v_url), 'html.parser')
    v_tables = html_soup.find_all('table')
    result_list = []
    # Get data from all tables on page
    for table in (v_tables):
        for row in table.find_all('tr'):
            row_data = [td.text for td in row.find_all('td')]
            v_link = row.select('td[class="cislo"] a')
            if row_data:
                if row_data[0].isnumeric():
                    result_list.append([row_data[0], row_data[1], v_link[0].get("href")])
    return result_list

def get_village_results(v_url: str):
    """ Function issys.exit() list of headers and list of results for specific village """
    # Download data and select tables only
    html_soup = BeautifulSoup(get_html_data(v_url), 'html.parser')
    v_tables = html_soup.find_all('table')
    # General data: only number of voters, envelopes issued, valid votes - columns 3, 4, 7
    village_general_data = []
    # List of parties and received votes  - take all
    list_of_parties = []
    votes_received = []
    for counter, table in enumerate(v_tables):
        for row in table.find_all('tr'):
            if row.find('td'): # Ommit header rows
                row_data = [
                    td.text.replace('\xa0','').replace(',','.').replace('-','')
                    for td in row.find_all('td')
                ]
                # First table is including village general data
                if not counter: 
                    village_general_data= [row_data[3], row_data[4], row_data[7]]
                # Other tables contains results of parties
                else: 
                    list_of_parties.append(row_data[1])
                    votes_received.append(row_data[2])
    # Compose final lists
    v_headers_list = SELECTED_COLUMNS + list_of_parties
    v_data_list = village_general_data + votes_received
    return v_headers_list, v_data_list

def check_input_arguments(argv_list: []):
    """ Returns true if all done well, otherwise false """
    if len(argv_list) != 3: # Check if two parameters has been given
        print("- please run this application with arguments : python escraper.py <url> <filename>")
        return False, None, None
    if argv_list[1].lower().find(URL_VERIFY) < 0: # Check if the URL points the correct way
        print("- please specify the URL as \"https://"+ URL_VERIFY + "...\"")
        return False, None, None
    print("- url to scrape:", argv_list[1])
    print("- target csv file:", argv_list[2],"\n")
    return True, argv_list[1], argv_list[2]

def cls_print(text_to_display: str) -> None:
    """ Clear the terminal screen and print the text """
    # For Windows
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(text_to_display)

def check_csv_filename(csv_name: str) -> str:
    """ If the filename does not include .csv extension it will correct it on return """
    correct_name = csv_name
    if csv_name.lower().find(".csv") < 0: # File does not have CSV extension
        if csv_name.lower().find(".") > 0: # But it has some extension
            correct_name = csv_name[0:csv_name.find(".")]+".csv"
        else:
            correct_name = csv_name+".csv"
    return correct_name

if __name__ == "__main__":
    print(check_csv_filename("csv_name"))
    print(check_csv_filename("csv_name.bak"))
    print(check_csv_filename("CSV_NAME.CSV"))

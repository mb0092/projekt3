**ELECTION SCRAPER**

third project for Engeto Python Academy

**APPLICATION DESCRIPTION**

Elections Scraper is downloading data for every municipality in selected district from the website www.volby.cz (link one specific district is here: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101) and then saves data into CSV formatted file

**INSTALLATION OF LIBRARIES**

Used libraries are specified in the requirements.txt file. For installation in your virtual environment use following command:

pip install --upgrade -r requirements.txt

**STARTING THE PROGRAM**

To run the election.py file from command line you need 2 mandatory arguments - link for specific district and name of the file (can be set with or without extension .csv):

python escraper.py <url> <filename.csv>

Link to web page please specify as "https://...." e.g. in quotation marks

**SAMPLE PROGRAM (EXAMPLE)**

Voting results for the Benešov district:

Argument(URL): "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"
Argument(filename): "vysledky_benesov"

**STARTING THE PROGRAM**

Windows
python election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vysledky_benesov
Linux
python3 election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vysledky_benesov

**PROGRESS**

Election Scraper
- url to scrape: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
- target csv file: vysledky_benesov

- Benešov
- Bernartice
- Bílkovice

**FINISH**

Election Scraper
- collected data saved to vysledky_benesov.csv
- scraping finished

**EXPECTED OUTPUT**

ČÍSLO,OBEC,POČET VOLIČŮ,VYDANÉ OBÁLKY,PLATNÉ HLASY,Občanská demokratická strana,Řád národa....
529303,Benešov,13104,8485,8437,1052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,....
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
532380,Blažejovice,96,80,77,6,0,0,5,0,3,11,0,0,3,0,0,5,1,0,0,29,0,0,6,0,0,0,0,8,0
532096,Borovnice,73,54,53,2,0,0,2,0,4,4,1,0,1,0,0,3,0,0,1,29,0,0,5,0,0,0,0,1,0
532924,Bukovany,598,393,393,50,0,0,20,0,53,20,8,0,6,0,0,49,0,1,11,127,0,4,8,0,1,1,4,30,0

**POSSIBLE ERRORS**

1. Missing arguments
    Election Scraper
    - please run this application with arguments : python escraper.py <url> <filename>
    - terminating now...
2. Bad URL specified or enetered without quotation marks
    Election Scraper
    - please specify the URL as "https://volby.cz/pls/ps2017nss..."
    - terminating now...




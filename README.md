# projekt3
Third project for ENGETO Python Academy
Miroslav Babka

ELECTIONS SCRAPER
third project for Engeto Python Academy

APPLICATION DESCRIPTION
Elections Scraper is downloading data for every municipality in selected district from the website www.volby.cz and then saves data for selected municipality ( number of voters, number of issued ballots, number of legal votes and list of candidate parties) into CSV formatted file

INSTALLATION OF LIBRARIES
Used libraries are specified in the requirements.txt file. For installation in your virtual environment use following command:

pip install -r requirements.txt

STARTING THE PROGRAM
To run the election.py file, you need 2 mandatory arguments.

python election.py <"url referring to the desired territory"> <"filename.csv">

SAMPLE PROGRAM (EXAMPLE)
Voting results for the Benešov district:

If you want to take result from Benešov district, in terminal (pycharm) you have to input link of this district and your own name of exported csv file, for example Benesov.csv. Or you can input any district you want and any name of exported file.

Argument(URL): '''https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'''

Argument(filename): "Benesov.csv"

STARTING THE PROGRAM
python election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "Benesov.csv"

DOWNLOADING
Downloading data from: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"

Saving data to: Benesov.csv

Data was saved. Exiting program!

EXPECTED OUTPUT
Code,Location,Registered,Envelopers,Valid,...
529303,Benešov,13104,8485,8437,...
532568,Bernartice,191,148,148,...

POSSIBLE ERRORS
"Program need 2 arguments. URL, CSV file. Exiting program!"
"First argument not correct. Exiting program! "
"Second argument not correct. Exiting program! "

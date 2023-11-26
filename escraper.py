""" Election Scraper """
import sys
import pandas as pd
# Functions from escrap_fncs.py
from escrap_fncs import get_villages_list
from escrap_fncs import get_village_url
from escrap_fncs import check_input_arguments
from escrap_fncs import get_village_results
from escrap_fncs import cls_print, check_csv_filename
# Variables for collected data
village_list=[]
region_header_list = []
region_data_list = []

# Election Scraper
cls_print("Election Scraper")
# Arguments check
if not check_input_arguments(sys.argv):
    print("- terminating now...")
    sys.exit()
else:
    # Get the list of villages for specified region
    village_list = get_villages_list(sys.argv[1])

for village in village_list:
    # Compose link to data for specific village
    village_code, village_name, village_link = village
    village_url = get_village_url(village_link)
    # Print the processed village name and document progress
    print("-", village_name)
    # Get list of headers and list of data from the tables
    region_header_list, village_data = get_village_results(village_url)
    # Update data list with village code and name as first two items
    village_data.insert(0, village_name)
    village_data.insert(0, village_code)
    region_data_list.append(village_data)

# Save to CSV using pandas
csv_file = check_csv_filename(sys.argv[2])
df = pd.DataFrame(region_data_list, columns=region_header_list)
df.to_csv(csv_file, index=False)
# All done
cls_print("Election Scraper")
print("- collected data saved to", csv_file)
print("- scraping finished")

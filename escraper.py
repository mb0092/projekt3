""" Election Scraper """
import sys
import pandas as pd
# Functions from functions.py
from functions import get_villages_list
from functions import get_village_url
from functions import check_input_arguments
from functions import get_village_results
from functions import cls_print, check_csv_filename

# Variables for collected data
village_list=[]
region_header_list = []
region_data_list = []

# Code
cls_print("Election Scraper")
# Arguments check
check_result, target_url, target_file = check_input_arguments(sys.argv)
# Terminate if anything is wrong
if not check_result:
    print("- terminating now...")
    sys.exit()
else:
    # Get the list of villages for specified region
    village_list = get_villages_list(target_url)

for village in village_list:
    village_code, village_name, village_link = village
    # Compose link to data for specific village
    village_url = get_village_url(village_link)
    # Print the processed village name just to document progress
    print("-", village_name)
    # Get list of headers and list of data for single village
    region_header_list, village_data = get_village_results(village_url)
    # Update data list as it needs village code and name as first two items
    village_data.insert(0, village_name)
    village_data.insert(0, village_code)
    # Append village data to results
    region_data_list.append(village_data)

cls_print("Election Scraper")
# Save to CSV using pandas if data collected
if region_data_list and region_header_list:
    target_file = check_csv_filename(target_file)
    df = pd.DataFrame(region_data_list, columns=region_header_list)
    df.to_csv(target_file, index=False)
    print("- collected data saved to", target_file)
else:
    print("- nothing to save")
print("- scraping finished")
# All done
sys.exit()

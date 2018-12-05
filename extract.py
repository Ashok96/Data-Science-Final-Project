"""
Filename: extract.py
Authors: Kymberlee Hill , Swarnim Bhandari
"""
import os
import pandas as pd

api_key = "0D98036D-C6D4-390F-A3E4-C7169A050F15"
raw_data_set_filename = "raw_data_set.csv"

def main():
    does_file_exist = True
    try:
        if not os.path.isfile(raw_data_set_filename):
            print("File [ " + raw_data_set_filename + "] not present. Fetching via http ...")
            source = "http://quickstats.nass.usda.gov/api/api_GET/?key="+ api_key +"&year__GE=1989&year__LE=2018&program=SURVEY&sector=\'ANIMALS & PRODUCTS\'&group=POULTRY&commodity_desc=TURKEYS&category=SLAUGHTERED&data_item__LIKE='F1 - SLAUGHTERED, MEASURED IN HEAD'&format=csv&state_alpha=VA"
            does_file_exist = FALSE
        else:
            print("File [" + raw_data_set_filename + "] exist. Fetching locally ...")
            source = raw_data_set_filename
            data = pd.read_csv(source)
            print("Finished fetching. Data size: [" + str(data.shape[0]) + "x" + str(data.shape[1]) + "]")
            if not does_file_exist:
                data.to_csv(raw_data_set_filename, index=FALSE)

            except Exception as e:
                print("Error" + str(e))

 if __name__ == "__main__":
    main()

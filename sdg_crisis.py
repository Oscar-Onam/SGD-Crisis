import json
import pandas as pd
import requests


def fetch_data_from_unsd(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        data = json.loads(json_data)

        # Extract DataFrame name from the URL
        df_name = url.split('/')[-2] + "_dataframe"

        # Create a DataFrame
        df = pd.DataFrame(data)
        # Rename columns if needed
        # df.rename(columns={'original_column_name': 'new_column_name'}, inplace=True)
        print(f"Data from the API for {df_name}:")
        print(df)
        return df
    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)
        return None

# URLs
urls = [
    "https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/Indicator/List",
    "https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/ArchiveData/GetArchiveTable",
    "https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/DataAvailability/GetIndicatorsAllCountries",
    "https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/DataAvailability/CountriesList"
]

# Fetch data and create DataFrames
data_frames = {url: fetch_data_from_unsd(url) for url in urls}

# Access the DataFrames by their respective names
print("Accessing DataFrames by name:")
print("Available DataFrames:", data_frames.keys())
print("Displaying 'ArchiveDataGetArchiveTable_dataframe':")
print(data_frames['https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/ArchiveData/GetArchiveTable_dataframe'])




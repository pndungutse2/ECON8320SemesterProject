import requests
import pandas as pd
from datetime import datetime

# BLS API Key
API_KEY = "318acea001604c8c8783ca5d415397d0"

# Series IDs (Required and Additional)
SERIES = {
    "Non_farm": "CES0000000001",   # Total non-farm employment
    "Unemployment_rate": "LNS14000000",  # Unemployment rate
    "Participation_rate": "LNS11300000", # Labor force participation rate
    "Civilian_unemployment": "LNS13000000", # Civilian Unemployment
    "Civilian_employment": "LNS12000000" # Unemployment Rate
}

# Function to fetch data from the BLS API
def fetch_bls_data(series_id, start_year, end_year):
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "seriesid": [series_id],
        "startyear": str(start_year),
        "endyear": str(end_year),
        "registrationkey": API_KEY,
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}, {response.text}")

# Process API response into a DataFrame
def process_data(response, series_name):
    data = response["Results"]["series"][0]["data"]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["year"] + df["period"].str[1:], format="%Y%m")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["series"] = series_name
    return df[["date", "value", "series"]]

# Main Function
def main():
    start_year = datetime.now().year - 1
    end_year = datetime.now().year

    all_data = []
    for name, series_id in SERIES.items():
        print(f"Fetching data for {name}...")
        response = fetch_bls_data(series_id, start_year, end_year)
        df = process_data(response, name)
        all_data.append(df)

    # Combine all series into a single DataFrame
    final_df = pd.concat(all_data)
    final_df.to_csv("labor_stats.csv", index=False)
    print("Data saved to labor_stats.csv")

if __name__ == "__main__":
    main()

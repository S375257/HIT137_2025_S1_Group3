import os
import pandas as pd
import numpy as np
from collections import defaultdict
import zipfile

# Define month-to-season mapping
season_months = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

def get_data_folder():
    path = input("Enter the path to the folder containing the CSV files or a .zip file: ").strip()
    if path.endswith('.zip'):
        extract_path = os.path.join(os.path.dirname(path), "extracted_temperature_data")
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        return extract_path
    elif os.path.isdir(path):
        return path
    else:
        raise FileNotFoundError("The specified path is neither a valid folder nor a zip file.")

def load_temperature_data(data_folder):
    station_data = defaultdict(lambda: {
        "monthly_temps": defaultdict(list),
        "all_temps": []
    })
    station_info = {}
    csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
    for file in csv_files:
        df = pd.read_csv(os.path.join(data_folder, file))
        for _, row in df.iterrows():
            station = row["STATION_NAME"]
            if station not in station_info:
                station_info[station] = {
                    "id": row["STN_ID"],
                    "lat": row["LAT"],
                    "lon": row["LON"]
                }
            for month in sum(season_months.values(), []):
                temp = row[month]
                if pd.notnull(temp):
                    station_data[station]["monthly_temps"][month].append(temp)
                    station_data[station]["all_temps"].append(temp)
    return station_data, station_info

def calculate_seasonal_averages(station_data):
    season_averages = {}
    for season, months in season_months.items():
        all_month_temps = []
        for station in station_data.values():
            for month in months:
                all_month_temps.extend(station["monthly_temps"][month])
        season_averages[season] = round(np.mean(all_month_temps), 2)
    return season_averages

def write_average_temperatures_to_file(season_averages, filename):
    with open(filename, "w") as f:
        f.write("Average Seasonal Temperatures Across All Stations and Years:\n")
        for season, avg in season_averages.items():
            f.write(f"{season}: {avg}°C\n")

def analyze_station_extremes(station_data):
    station_ranges = {}
    station_averages = {}

    for station, data in station_data.items():
        temps = data["all_temps"]
        if temps:
            station_ranges[station] = max(temps) - min(temps)
            station_averages[station] = np.mean(temps)

    max_range = max(station_ranges.values())
    max_avg = max(station_averages.values())
    min_avg = min(station_averages.values())

    return {
        "largest_range": {
            "value": round(max_range, 2),
            "stations": [s for s, r in station_ranges.items() if r == max_range]
        },
        "warmest": {
            "value": round(max_avg, 2),
            "stations": [s for s, a in station_averages.items() if a == max_avg]
        },
        "coolest": {
            "value": round(min_avg, 2),
            "stations": [s for s, a in station_averages.items() if a == min_avg]
        }
    }

def write_extremes_to_file(results, station_info):
    def format_station_line(name):
        info = station_info.get(name, {})
        return f"{name} - STATION ID # {info.get('id', 'N/A')} - LAT: {info.get('lat', 'N/A')} LON: {info.get('lon', 'N/A')}"

    with open("largest_temp_range_station.txt", "w") as f:
        f.write("Station(s) with the Largest Temperature Range:\n")
        f.write(f"Range: {results['largest_range']['value']:.2f}°C\n")
        for station in results['largest_range']['stations']:
            f.write(f"{format_station_line(station)}\n")

    with open("warmest_and_coolest_station.txt", "w") as f:
        f.write("Warmest Station(s):\n")
        f.write(f"Average Temp: {results['warmest']['value']:.2f}°C\n")
        for station in results['warmest']['stations']:
            f.write(f"{format_station_line(station)}\n")
        f.write("\nCoolest Station(s):\n")
        f.write(f"Average Temp: {results['coolest']['value']:.2f}°C\n")
        for station in results['coolest']['stations']:
            f.write(f"{format_station_line(station)}\n")

def main():
    data_folder = get_data_folder()
    station_data, station_info = load_temperature_data(data_folder)
    season_averages = calculate_seasonal_averages(station_data)
    write_average_temperatures_to_file(season_averages, "average_temp.txt")
    extremes = analyze_station_extremes(station_data)
    write_extremes_to_file(extremes, station_info)

    output_path = os.path.abspath("average_temp.txt")
    print(f"\nDone! Files saved to: {os.path.dirname(output_path)}")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        input("\nPress Enter to exit...")

import os
import csv

# Folder where the CSVs are stored
data_folder_path = 'temperature_data'

# Variables to track warmest and coolest stations
warmest_station = {'avg_temp': float('-inf')}
coolest_station = {'avg_temp': float('inf')}

# Go through each file in the folder
for filename in os.listdir(data_folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                monthly_temps = []
                for month in [
                    'January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December'
                ]:
                    try:
                        temp = float(row[month])
                        monthly_temps.append(temp)
                    except (ValueError, KeyError):
                        continue  # Skip bad or missing data

                if len(monthly_temps) >= 6:  # Ensure decent amount of data
                    avg_temp = sum(monthly_temps) / len(monthly_temps)

                    if avg_temp > warmest_station['avg_temp']:
                        warmest_station = {
                            'name': row.get('STATION_NAME', 'Unknown'),
                            'id': row.get('STN_NO', 'Unknown'),
                            'lat': row.get('LAT', 'Unknown'),
                            'lon': row.get('LON', 'Unknown'),
                            'file': filename,
                            'avg_temp': round(avg_temp, 2)
                        }

                    if avg_temp < coolest_station['avg_temp']:
                        coolest_station = {
                            'name': row.get('STATION_NAME', 'Unknown'),
                            'id': row.get('STN_NO', 'Unknown'),
                            'lat': row.get('LAT', 'Unknown'),
                            'lon': row.get('LON', 'Unknown'),
                            'file': filename,
                            'avg_temp': round(avg_temp, 2)
                        }

# Output file
output_file = 'warmest_and_coolest_station.txt'

with open(output_file, 'w', encoding='utf-8') as out:
    out.write("Warmest Station:\n")
    for key, value in warmest_station.items():
        out.write(f"{key.capitalize()}: {value}\n")

    out.write("\nCoolest Station:\n")
    for key, value in coolest_station.items():
        out.write(f"{key.capitalize()}: {value}\n")

print(f"✅ Warmest and coolest stations saved to '{output_file}'")

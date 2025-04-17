import os
import csv

# Path to your folder of CSV files
data_folder_path = 'temperature_data'

# Variables to track the station with the largest temperature range
max_range = -1
station_details = {}

# Loop through each CSV file
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
                        continue  # Skip missing or invalid values

                if len(monthly_temps) >= 2:
                    temp_range = max(monthly_temps) - min(monthly_temps)

                    if temp_range > max_range:
                        max_range = temp_range
                        station_details = {
                            'Name': row.get('STATION_NAME', 'Unknown'),
                            'ID': row.get('STN_NO', 'Unknown'),
                            'Latitude': row.get('LAT', 'Unknown'),
                            'Longitude': row.get('LON', 'Unknown'),
                            'Year Range File': filename,
                            'Range': round(temp_range, 2)
                        }

# Write the result to a text file
output_filename = 'station_max_range.txt'

with open(output_filename, 'w', encoding='utf-8') as out:
    out.write("Station with the Largest Temperature Range:\n\n")
    if station_details:
        for key, value in station_details.items():
            out.write(f"{key}: {value}\n")
    else:
        out.write("No station data found.\n")

print(f"✅ Station with largest range written to '{output_filename}'")

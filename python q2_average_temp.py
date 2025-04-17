import os
import csv

# Folder where CSV files are stored
data_folder_path = 'temperature_data'

# Map seasons to month names (exact match with your CSV headers)
season_months = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

# Storage for total and count per season
season_temperature_data = {
    'Summer': [0.0, 0],
    'Autumn': [0.0, 0],
    'Winter': [0.0, 0],
    'Spring': [0.0, 0]
}

# Process all CSV files
for filename in os.listdir(data_folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                for season, months in season_months.items():
                    for month in months:
                        try:
                            temp_value = float(row[month])
                            season_temperature_data[season][0] += temp_value
                            season_temperature_data[season][1] += 1
                        except (ValueError, KeyError):
                            continue  # Skip missing or non-numeric values

# Write results
output_file_name = 'average_temp.txt'

with open(output_file_name, 'w', encoding='utf-8') as f:
    f.write("Average Temperature by Season (°C):\n\n")
    for season, (total_temp, count) in season_temperature_data.items():
        if count > 0:
            avg = total_temp / count
            f.write(f"{season}: {avg:.2f}°C\n")
        else:
            f.write(f"{season}: No data available\n")

print(f"✅ Averages written to '{output_file_name}' successfully.")

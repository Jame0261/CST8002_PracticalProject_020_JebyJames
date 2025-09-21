"""
CST8002 Practical Project 1
Author: Jeby James
Professor: Stanley Pieda
Date: 2025-09-21
Description: Load dataset into record objects and display them
"""

import csv
from record import KelpFishRecord

records = []

try:
    with open(r"C:\Python020\pacific_rim_npr_coastalmarine_kelp_fish_community_2008-2016_data.csv",
              newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)

        for i, row in enumerate(reader):
            if i >= 5:  # load only first 5 records
                break
            record = KelpFishRecord(
                site_identification=row.get('Site identification', ''),
                year=row.get('Year', ''),
                diver_identication=row.get('Diver identification', ''),   
                transect=row.get('Transect', ''),
                average_depth_ft=row.get('Average depth (ft)', ''),
                species_code=row.get('Species code', ''),
                count=row.get('Count', ''),  
                survey_type=row.get('Survey type', '')
            )
            records.append(record)

except FileNotFoundError:
    print("Dataset file not found. Please check the filename.")
    exit(1)

# Loop over records and print them
for record in records:
    print(record)

# Always display your name
print("\nProgram by: Jeby James")

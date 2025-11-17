"""
File I/O functions: load and save KelpFishRecord objects
"""
import csv
import uuid
from model.record import KelpFishRecord  # ensure this import matches your record class

def load_records_from_csv(path, limit=100, encoding='latin-1'):
    """
    Load KelpFishRecord objects from a CSV file.
    :param path: path to CSV file
    :param limit: maximum number of records to read
    :param encoding: file encoding
    :return: list of KelpFishRecord objects
    """
    records = []
    try:
        with open(path, newline='', encoding=encoding) as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                if limit and i >= limit:
                    break
                rec = KelpFishRecord(
                    site_identification=row.get('Site identification', ''),
                    year=row.get('Year', ''),
                    diver_identification=row.get('Diver identification', ''),
                    transect=row.get('Transect', ''),
                    average_depth_ft=row.get('Average depth (ft)', ''),
                    species_code=row.get('Species code', ''),
                    count=row.get('Count', ''),
                    survey_type=row.get('Survey type', '')
                )
                records.append(rec)
    except FileNotFoundError:
        raise
    return records

def save_records_to_csv(records, output_dir='.', prefix='records'):
    """
    Save a list of KelpFishRecord objects to a new CSV file.
    :param records: list of KelpFishRecord objects
    :param output_dir: directory to save the CSV
    :param prefix: filename prefix
    :return: path to saved CSV file
    """
    fname = f"{prefix}_{uuid.uuid4()}.csv"
    path = f"{output_dir}\\{fname}"
    
    # If no records, write header only
    fieldnames = list(records[0].to_dict().keys()) if records else list(KelpFishRecord("", "", "", "", "", "", "", "").to_dict().keys())
    
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow(r.to_dict())
    
    return path

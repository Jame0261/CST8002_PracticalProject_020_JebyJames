def add_record(records, record):
    records.append(record)

def edit_record(records, index, new_record):
    if 0 <= index < len(records):
        records[index] = new_record
        return True
    return False

def delete_record(records, index):
    if 0 <= index < len(records):
        del records[index]
        return True
    return False

def get_record(records, index):
    if 0 <= index < len(records):
        return records[index]
    return None

def sort_records_by_year(records):
    # Keep header intact
    if not records:
        return records
    header, *data_records = records
    try:
        sorted_data = sorted(data_records, key=lambda r: int(r.year))
    except ValueError:
        sorted_data = sorted(data_records, key=lambda r: r.year)
    return [header] + sorted_data

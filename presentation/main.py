import sys
import os

# Ensure project root is added
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from persistence.file_io import load_records_from_csv, save_records_to_csv
from model.record import KelpFishRecord
from business.business_logic import add_record, edit_record, delete_record, get_record, sort_records_by_year

DATA_PATH = r"C:\Users\jebyj\Downloads\project2 (1)\project2\dataset.csv"

def display_records(records):
    for i, r in enumerate(records):
        print(f"{i+1:03d}: {r}")
        if (i+1) % 10 == 0:
            print("Program by Jeby James")

def menu():
    try:
        records = load_records_from_csv(DATA_PATH, limit=100)
    except FileNotFoundError:
        print("Dataset file not found.")
        return

    while True:
        print("\nProgram by Jeby James")
        print("1. Display records")
        print("2. Reload data")
        print("3. Add new record")
        print("4. Edit record")
        print("5. Delete record")
        print("6. Save to CSV")
        print("7. Sort by Year (NEW feature)")
        print("8. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            display_records(records)

        elif choice == "2":
            records = load_records_from_csv(DATA_PATH, limit=100)
            print("Reloaded.")

        elif choice == "3":
            site = input("Site: ")
            year = input("Year: ")
            diver = input("Diver: ")
            transect = input("Transect: ")
            depth = input("Depth: ")
            species = input("Species: ")
            count = input("Count: ")
            survey = input("Survey type: ")

            new_record = KelpFishRecord(site, year, diver, transect, depth, species, count, survey)
            add_record(records, new_record)
            print("Added.")

        elif choice == "4":
            idx = int(input("Index to edit (1-based): ")) - 1
            if get_record(records, idx):
                print("Enter new values or leave blank:")
                site = input("New site: ")
                records[idx].site_identification = site or records[idx].site_identification
                print("Edited.")
            else:
                print("Invalid index.")

        elif choice == "5":
            idx = int(input("Index to delete (1-based): ")) - 1
            if delete_record(records, idx):
                print("Deleted.")
            else:
                print("Invalid index.")

        elif choice == "6":
            path = save_records_to_csv(records)
            print("Saved to:", path)

        elif choice == "7":
            records = sort_records_by_year(records)
            print("Sorted by Year.")

        elif choice == "8":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
7
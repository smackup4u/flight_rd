import csv
import json
from datetime import datetime
from typing import List, Dict

def load_csv_to_dict_list(file_path: str) -> List[Dict]:
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV, where keys 
    are derived from the header row.
    """
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            # DictReader automatically uses the first line as field names (keys)
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the CSV: {e}")
    
    return data

def calculate_duration(time1_str: str, time2_str: str) -> str:
    """
    Calculates the difference between two ISO 8601 timestamps.
    Example Input: "2026-07-24T05:40:47Z"
    Returns a string in 'X hours Y minutes' format.
    """
    try:
        # .replace('Z', '+00:00') ensures compatibility across Python versions
        t1 = datetime.fromisoformat(time1_str.replace('Z', '+00:00'))
        t2 = datetime.fromisoformat(time2_str.replace('Z', '+00:00'))
        
        # Calculate the absolute difference
        diff = abs(t2 - t1)
        
        total_seconds = int(diff.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        
        #return f"{hours} hours {minutes} minutes"
        return total_seconds
    except ValueError as e:
        return f"Error parsing dates: {e}"


def seconds_to_hours(seconds):   #non mutual, just returns a string
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours} hours and {minutes} minutes"

def max_alt(list_altitude: list) -> int | None:
    maximum = 0
    if len(list_altitude) > 0:
        for item in list_altitude:
            item = int(item)
            if item > maximum:
                maximum = item
        return maximum
    else:
        return None

if __name__ == "__main__":
    # --- TEST SECTION ---
    # Test 1: Time Calculation
    t1 = "2026-07-24T05:40:47Z"
    t2 = "2026-07-24T10:15:00Z"
    print(f"Sample Time Diff: {calculate_duration(t1, t2)}")

    # Test 2: CSV Loading (creates a dummy file for demonstration)
    dummy_file = "test_data.csv"
    with open(dummy_file, mode='w', encoding='utf-8') as f:
        f.write("id,event_name,start_time,end_time\n")
        f.write("101,Flight_A,2026-07-24T05:00:00Z,2026-07-24T08:30:00Z\n")

    data = load_csv_to_dict_list(dummy_file)
    print("\nLoaded CSV Data:")
    print(json.dumps(data, indent=2))

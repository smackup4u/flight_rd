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

def seconds_to_minutes(seconds: int) -> str:
    minutes = seconds // 60
    rest = seconds % 60
    return f"{minutes} min and {rest} sec"

# maximum Altitude
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

# Get the flight duration for each FL in seconds
def get_fl_duration(csv_input: list[dict]):
    #lists to store datapoints
    temp_fl31 = []
    temp_fl32 = []
    temp_fl33 = []
    temp_fl34 = []
    temp_fl35 = []
    temp_fl36 = []
    temp_fl37 = []
    temp_fl38 = []
    temp_fl39 = []
    temp_fl40 = []
                    

    #duration for each FL in seconds, data will be returned
    add_fl31 = 0
    add_fl32 = 0
    add_fl33 = 0
    add_fl34 = 0
    add_fl35 = 0
    add_fl36 = 0
    add_fl37 = 0
    add_fl38 = 0
    add_fl39 = 0
    add_fl40 = 0
    
                        
    for alt in csv_input:



        # -------Flightlevel 31
        if 30500 < int(alt.get('Altitude')) < 31500:
            #first_fl31 = alt.get('UTC')
            temp_fl31.append(alt)
        else:
            if len(temp_fl31) > 0:
                duration_tmp = calculate_duration(temp_fl31[0].get('UTC'), temp_fl31[-1].get('UTC'))
                add_fl31 = add_fl31 + duration_tmp
                temp_fl31 = []

        # -------Flightlevel 32
        if 31501 < int(alt.get('Altitude')) < 32500:
                #first_fl31 = alt.get('UTC')
                temp_fl32.append(alt)
        else:
            if len(temp_fl32) > 0:
                duration_tmp = calculate_duration(temp_fl32[0].get('UTC'), temp_fl32[-1].get('UTC'))
                add_fl32 = add_fl32 + duration_tmp
                temp_fl32 = []

        # -------Flightlevel 33
        if 32501 < int(alt.get('Altitude')) < 33500:
                #first_fl31 = alt.get('UTC')
                temp_fl33.append(alt)
        else:
            if len(temp_fl33) > 0:
                duration_tmp = calculate_duration(temp_fl33[0].get('UTC'), temp_fl33[-1].get('UTC'))
                add_fl33 = add_fl33 + duration_tmp
                temp_fl33 = []


        # -------Flightlevel 34
        if 33501 < int(alt.get('Altitude')) < 34500:
                #first_fl31 = alt.get('UTC')
                temp_fl34.append(alt)
        else:
            if len(temp_fl34) > 0:
                duration_tmp = calculate_duration(temp_fl34[0].get('UTC'), temp_fl34[-1].get('UTC'))
                add_fl34 = add_fl34 + duration_tmp
                temp_fl34 = []                        

        # -------Flightlevel 35
        if 34501 < int(alt.get('Altitude')) < 35500:
                #first_fl31 = alt.get('UTC')
                temp_fl35.append(alt)
        else:
            if len(temp_fl35) > 0:
                duration_tmp = calculate_duration(temp_fl35[0].get('UTC'), temp_fl35[-1].get('UTC'))
                add_fl35 = add_fl35 + duration_tmp
                temp_fl35 = []

        # -------Flightlevel 36
        if 35501 < int(alt.get('Altitude')) < 36500:
                #first_fl31 = alt.get('UTC')
                temp_fl36.append(alt)
        else:
            if len(temp_fl36) > 0:
                duration_tmp = calculate_duration(temp_fl36[0].get('UTC'), temp_fl36[-1].get('UTC'))
                add_fl36 = add_fl36 + duration_tmp
                temp_fl36 = []

        # -------Flightlevel 37
        if 36501 < int(alt.get('Altitude')) < 37500:
                #first_fl31 = alt.get('UTC')
                temp_fl37.append(alt)
        else:
            if len(temp_fl37) > 0:
                duration_tmp = calculate_duration(temp_fl37[0].get('UTC'), temp_fl37[-1].get('UTC'))
                add_fl37 = add_fl37 + duration_tmp
                temp_fl37 = []



        # -------Flightlevel 38
        if 37501 < int(alt.get('Altitude')) < 38500:
                #first_fl31 = alt.get('UTC')
                temp_fl38.append(alt)
        else:
            if len(temp_fl38) > 0:
                duration_tmp = calculate_duration(temp_fl38[0].get('UTC'), temp_fl38[-1].get('UTC'))
                add_fl38 = add_fl38 + duration_tmp
                temp_fl38 = []


        # -------Flightlevel 39
        if 38501 < int(alt.get('Altitude')) < 39500:
                #first_fl31 = alt.get('UTC')
                temp_fl39.append(alt)
        else:
            if len(temp_fl39) > 0:
                duration_tmp = calculate_duration(temp_fl39[0].get('UTC'), temp_fl39[-1].get('UTC'))
                add_fl39 = add_fl39 + duration_tmp
                temp_fl39 = []

        # -------Flightlevel 40
        if 39501 < int(alt.get('Altitude')) < 40500:
                #first_fl31 = alt.get('UTC')
                temp_fl40.append(alt)
        else:
            if len(temp_fl40) > 0:
                duration_tmp = calculate_duration(temp_fl40[0].get('UTC'), temp_fl40[-1].get('UTC'))
                add_fl40 = add_fl40 + duration_tmp
                temp_fl40 = []




        #breakpoint()
    #return each value 
    return add_fl31, add_fl32, add_fl33, add_fl34, add_fl35, add_fl36, add_fl37, add_fl38, add_fl39, add_fl40

# Method for taxi time 
def get_taxi_duration(csv_input: list[dict]):
    #lists to store datapoints
    temp_taxi = []
   

    #duration for each FL in seconds, data will be returned
    add_taxi_outbound = 0
    add_taxi_inbound = 0

    #get first timestamp, important for diffirentiate taxi outbound or taxi inbound
    begin = csv_input[0].get('UTC')
    #get last datapoint to still get inbound taxi when speed is over 0 on last datapoint
    last_data = csv_input[-1]
    for alt in csv_input:


        # get taxi datapoint (speed > 0 alt < 1)
        if int(alt.get('Speed')) > 0 and int(alt.get('Altitude')) < 1 and alt != last_data:
            #first_fl31 = alt.get('UTC')
            temp_taxi.append(alt)
        else:
            if len(temp_taxi) > 0:
                time = calculate_duration(begin, temp_taxi[-1].get('UTC'))
                duration_tmp = calculate_duration(temp_taxi[0].get('UTC'), temp_taxi[-1].get('UTC'))
                if time < 2000:
                    add_taxi_outbound = add_taxi_outbound + duration_tmp
                else:
                    add_taxi_inbound = add_taxi_inbound + duration_tmp
                temp_taxi = []


        #breakpoint()
    #return each value 
    return add_taxi_outbound, add_taxi_inbound


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

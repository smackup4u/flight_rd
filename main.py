# CSV scratch

#parentheses wrapping
from csv_agent import (load_csv_to_dict_list, 
                       calculate_duration, 
                       seconds_to_hours, 
                       max_alt, 
                       get_fl_duration, 
                       get_taxi_duration, 
                       seconds_to_minutes)

data_csv = load_csv_to_dict_list('./csv/QR960_40d2a370.csv')
print(len(data_csv))
print('First datapoint')
print(data_csv[0])
print('last datapoint')
print(data_csv[-1])

duration = calculate_duration(data_csv[0].get('UTC'), data_csv[len(data_csv)-1].get('UTC'))
print(f"The duration was: {duration}")
real_depature = ''
real_landing = ''
for item in data_csv:
    if int(item.get('Altitude')) > 0:
        real_depature = item.get('UTC')
        break
for item in reversed(data_csv):
    if int(item.get('Altitude')) > 0:
        real_landing = item.get('UTC')
        break
print(f"real dep: {real_depature}")
real_duration = calculate_duration(real_depature, real_landing)
print(f"The actual flight time was {seconds_to_hours(real_duration)}")
fl31 = 0
fl32 = 0
fl33 = 0
fl34 = 0
fl35 = 0
fl36 = 0

# Count datapoints, not really usable for analizing
for alt in data_csv:
    # FL 31
    
    match int(alt.get('Altitude')):
        case v if 30500 < v < 31500:
            fl31 += 1
        case v if 31500 < v < 32500:
            fl32 += 1
        case v if 32500 < v < 33500:
            fl33 += 1
        
            
print(f"The flight was in FL31: {fl31} FL32: {fl32}")
        
add_fl31 = 0
add_fl32 = 0
add_fl35 = 0
first_fl31 = "" #deprecated
last_fl31 = ""  #deprecated
temp_fl31 = []
temp_fl32 = []
temp_fl35 = []
tmp_alt = []
#breakpoint()
duration_tmp = 0
maximum_altitude = 0


for alt in data_csv:


    tmp_alt.append(alt.get('Altitude'))
    # old code, will keep it for backup
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

    # -------Flightlevel 35
    if 34501 < int(alt.get('Altitude')) < 35500:
                #first_fl31 = alt.get('UTC')
                temp_fl35.append(alt)
    else:
        if len(temp_fl35) > 0:
            duration_tmp = calculate_duration(temp_fl35[0].get('UTC'), temp_fl35[-1].get('UTC'))
            add_fl35 = add_fl35 + duration_tmp
            temp_fl35 = []

    
    #duration_temp = calculate_duration(first_fl31, last_fl31)
    #add_fl31 = add_fl31 + duration_temp

callsign = data_csv[0].get('Callsign')
maximum_altitude = max_alt(tmp_alt)
duration_fl31, duration_fl32, duration_fl33, duration_fl34, duration_fl35, duration_fl36, duration_fl37, duration_fl38, duration_fl39, duration_fl40 = get_fl_duration(data_csv)
print("Duration per FL")
print("-----------------")
print(f"In FL33: {seconds_to_hours(duration_fl33)}")
print(f"In FL35: {seconds_to_hours(duration_fl35)}")
print(f"In FL37: {seconds_to_hours(duration_fl37)}")

print(f"In FL38: {seconds_to_hours(duration_fl38)}")
print(f"In FL39: {seconds_to_hours(duration_fl39)}")
taxi_out, taxi_in = get_taxi_duration(data_csv)
print(f"The flight {callsign} was {seconds_to_minutes(taxi_out)} in taxi outbound (from gate to takeoff)")
print(f"The flight {callsign} was {seconds_to_minutes(taxi_in)} in taxi inbound (from landing to gate)")
print(f"The maximum altitude was {maximum_altitude}")

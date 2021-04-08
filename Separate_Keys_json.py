import json, shelve, sys

# Opening JSON file and loading data
x = open('API_EoB_Data_03162021_MAR29(Formatted_Step1).json')

d = x.read()
data = json.loads(d)

shelfFile = shelve.open('shelf_For_EoB_Key_Separation')
print(f"The init var is currently set to {shelfFile['init']}")
print(f"The write var is currently set to {shelfFile['write']}")


patient_data = data['Patients']

key1, key2, key3, key4, key5, key6, key7, key8, key9 = patient_data[0].keys(), patient_data[4].keys(), \
                                                 patient_data[6].keys(), patient_data[7].keys(), \
                                                 patient_data[8].keys(), patient_data[11].keys(), \
                                                 patient_data[102].keys(), patient_data[150].keys(),  {}

########################################################################################################################
# BE SURE TO SET THE FOLLOWING BOOLEANS TO THE APPROPRIATE VALUE WHEN BEGINNING TO SEPARATE KEYS #######################
init = shelfFile['init']
write = shelfFile['write']
# These vars are now shelved in a file to increase automation
########################################################################################################################
key = 1
c = 0
count = -1
count_s = 0
count_d = 0

if write:
    with open('EoB_Key1.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key1:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key2.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key2:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key3.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key3:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key4.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key4:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key5.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key5:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key6.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key6:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key7.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key7:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

    with open('EoB_Key8.json', 'w') as f:
        for p in patient_data:
            if p.keys() == key8:
                json.dump(p, sort_keys=True, indent=4, fp=f)
                f.write('\n')
        f.close()

else:
    for p in patient_data:
        if init:
            if c < 5000:
                print(c,' ',p.keys())
                c += 1
            if p.keys() in [key1, key2, key3, key4, key5, key6, key7, key8, key9]:
                print('True')
                count_s += 1
            else:
                key += 1
                count_d += 1
                print(f'The new keys have been located in record #{c-1}')
    print(f'There are {count_d} records that have not been assigned a key!')

if count_d == 0 and shelfFile['init'] == True:
    shelfFile['init'] = False
    shelfFile['write'] = True
elif count_d == 0 and shelfFile['write'] == True:
    shelfFile['init'] = True
    shelfFile['write'] = False
print(f"The init var is currently set to {shelfFile['init']}")
print(f"The write var is currently set to {shelfFile['write']}")

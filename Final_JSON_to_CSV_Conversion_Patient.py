# February 1, 2021
# Patient JSON File conversion to CSV
#
# IMPORTANT:
# If you change the source file at the beginning of the program, you must also change
# the name for the two csv files that the program creates. There are 4 lines within the program where this would
# need to be done.
#######################################################################################################################

import json
import pandas as pd
import logging
import pprint
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def extension_Format (row,file,extension_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    extC = len(data[row]['extension'])
    extension_dict['Patient_Race'] = data[row]['extension'][0]['valueCoding']['display']
    extension_dict['rfrnc_year'] = data[row]['extension'][1]['valueDate']

    for e in range(2, extC):
        try:
            extension_dict[f'Dual_{e-1} Code'] = data[row]['extension'][e]['valueCoding']['code']
            extension_dict[f'Dual_{e - 1} Display'] = data[row]['extension'][e]['valueCoding']['display']
        except KeyError:
            extension_dict[f'Dual_{e-1} Code'] = 'Null'
            extension_dict[f'Dual_{e - 1} Display'] = 'Null'


fs = 'Patient_03162021_MAR29Formatted.json'
x = open(fs)
d = x.read()
data = json.loads(d)


c = 0
row = 0

masterdf = pd.DataFrame()
masterdf2 = pd.DataFrame()

address_dict = {}
birthdate_dict = {}
extension_dict = {}
gender_dict = {}
id_dict = {}
identifier_dict = {}
meta_dict = {}
name_dict = {}
resourceType_dict = {}

dict_list = [address_dict, birthdate_dict, extension_dict, gender_dict, id_dict, identifier_dict, meta_dict, name_dict, resourceType_dict]

for x in data:
    c += 1
logging.debug(c)
logging.debug(pprint.pprint(data[45]))
logging.debug(str(data[0]['address'][0]['city']), str(data[0]['address'][0]['line'][0]))


while row < c:
    if row == 0:
        print(row)

        try:
            address_dict['patient_address_city'] = data[row]['address'][0]['city']
        except (KeyError,IndexError):
            address_dict['patient_address_city'] = 'Null'

        try:
            address_dict['patient_address_street'] = data[row]['address'][0]['line'][0]
        except (KeyError,IndexError):
            address_dict['patient_address_street'] = 'Null'

        try:
            address_dict['patient_address_postalCode'] = data[row]['address'][0]['postalCode']
        except (KeyError,IndexError):
            address_dict['patient_address_postalCode'] = 'Null'
        try:
            address_dict['patient_address_state'] = data[row]['address'][0]['state']
        except (KeyError, IndexError):
            address_dict['patient_address_state'] = 'Null'

        birthdate_dict['patient_birthDate'] = data[row]['birthDate']

        extension_Format(row, fs, extension_dict)

        gender_dict['Gender'] = data[row]['gender']

        id_dict['Subject'] = data[row]['id']

        try:
            identifier_dict['Subject_MBI'] = data[row]['identifier'][3]['value']
        except IndexError:
            identifier_dict['Subject_MBI'] = 'Null'

        meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']

        try:
            name_dict['firstName'] = data[row]['name'][0]['given']
            name_dict['firstName'] = name_dict['firstName'][0]
        except KeyError:
            name_dict['firstName'] = 'Null'
        except IndexError:
            name_dict['firstName'] = 'Null'
        name_dict['lastName'] = data[row]['name'][0]['family']

        resourceType_dict['resourceType'] = data[row]['resourceType']

        for i in dict_list:
            df = pd.DataFrame([i])
            masterdf = pd.concat([masterdf,df], axis=1)
        masterdf.to_csv('API_Patient_Data_03082021(5).csv', index=False)
        row += 1

    elif row > 0:
        print(row)
        masterdf2 = pd.DataFrame()

        try:
            address_dict['patient_address_city'] = data[row]['address'][0]['city']
        except (KeyError, IndexError):
            address_dict['patient_address_city'] = 'Null'

        try:
            address_dict['patient_address_street'] = data[row]['address'][0]['line'][0]
        except (KeyError, IndexError):
            address_dict['patient_address_street'] = 'Null'

        try:
            address_dict['patient_address_postalCode'] = data[row]['address'][0]['postalCode']
        except (KeyError, IndexError):
            address_dict['patient_address_postalCode'] = 'Null'
        try:
            address_dict['patient_address_state'] = data[row]['address'][0]['state']
        except (KeyError, IndexError):
            address_dict['patient_address_state'] = 'Null'

        birthdate_dict['patient_birthDate'] = data[row]['birthDate']

        extension_Format(row, fs, extension_dict)

        gender_dict['Gender'] = data[row]['gender']

        id_dict['Subject'] = data[row]['id']

        try:
            identifier_dict['Subject_MBI'] = data[row]['identifier'][3]['value']
        except IndexError:
            identifier_dict['Subject_MBI'] = 'Null'

        meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']

        try:
            name_dict['firstName'] = data[row]['name'][0]['given']
            name_dict['firstName'] = name_dict['firstName'][0]
        except KeyError:
            name_dict['firstName'] = 'Null'
        except IndexError:
            name_dict['firstName'] = 'Null'
        name_dict['lastName'] = data[row]['name'][0]['family']

        resourceType_dict['resourceType'] = data[row]['resourceType']

        for i in dict_list:
            df = pd.DataFrame([i])
            masterdf2 = pd.concat([masterdf2, df], axis=1)
        masterdf2.to_csv('consecutive_rows_Patient(5).csv', mode='a', index=False, header=False)
        row += 1

if row > 1:
    with open('consecutive_rows_Patient(5).csv', 'r') as s:
        source = s.read()
    with open('API_Patient_Data_03082021(5).csv', 'a') as t:
        t.write(source)
    s.close()
    t.close()

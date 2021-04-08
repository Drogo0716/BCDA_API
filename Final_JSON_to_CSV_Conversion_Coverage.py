import json, pprint, sys, threading
import pandas as pd


def extension_Format(row, file, extension_dict):
    if row % 4 == 0:
        try:
            extension_dict['ms_cd'] = data[row]['extension'][0]['valueCoding']['code']  # ms_cd
            extension_dict['ms_display'] = data[row]['extension'][0]['valueCoding']['display']
            extension_dict['orec_cd'] = data[row]['extension'][1]['valueCoding']['code']  # orec_cd
            extension_dict['orec_display'] = data[row]['extension'][1]['valueCoding']['display']  # orec_display
            extension_dict['crec_cd'] = data[row]['extension'][2]['valueCoding']['code']  # crec_cd
            extension_dict['crec_display'] = data[row]['extension'][2]['valueCoding']['display']  # crec_display
            extension_dict['esrd-id'] = data[row]['extension'][3]['valueCoding']['code']  # esrd_id
            extension_dict['a_trm_cd'] = data[row]['extension'][4]['valueCoding']['code']  # a_trm_cd
            extension_dict['a_trm_display'] = data[row]['extension'][4]['valueCoding']['display']  # a_trm_display
            extension_dict['rfrnc_yr'] = data[row]['extension'][5]['valueDate']  # rfrnc_yr
            extension_dict['dual_01_cd'] = data[row]['extension'][6]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_01_display'] = data[row]['extension'][6]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_02_cd'] = data[row]['extension'][7]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_02_display'] = data[row]['extension'][7]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_03_cd'] = data[row]['extension'][8]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_03_display'] = data[row]['extension'][8]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_04_cd'] = data[row]['extension'][9]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_04_display'] = data[row]['extension'][9]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_05_cd'] = data[row]['extension'][10]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_05_display'] = data[row]['extension'][10]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_06_cd'] = data[row]['extension'][11]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_06_display'] = data[row]['extension'][11]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_07_cd'] = data[row]['extension'][12]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_07_display'] = data[row]['extension'][12]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_08_cd'] = data[row]['extension'][13]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_08_display'] = data[row]['extension'][13]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_09_cd'] = data[row]['extension'][14]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_09_display'] = data[row]['extension'][14]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_10_cd'] = data[row]['extension'][15]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_10_display'] = data[row]['extension'][15]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_11_cd'] = data[row]['extension'][16]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_11_display'] = data[row]['extension'][16]['valueCoding']['display']  # dual_01_display
            extension_dict['dual_12_cd'] = data[row]['extension'][17]['valueCoding']['code']  # dual_01_cd
            extension_dict['dual_12_display'] = data[row]['extension'][17]['valueCoding']['display']  # dual_01_display
            extension_dict['BuyIn01_cd'] = data[row]['extension'][18]['valueCoding']['code']  # buyin01 code
            extension_dict['BuyIn01_display'] = data[row]['extension'][18]['valueCoding']['display']  # buyin01 display
            extension_dict['BuyIn02_cd'] = data[row]['extension'][19]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn02_display'] = data[row]['extension'][19]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn03_cd'] = data[row]['extension'][20]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn03_display'] = data[row]['extension'][20]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn04_cd'] = data[row]['extension'][21]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn04_display'] = data[row]['extension'][21]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn05_cd'] = data[row]['extension'][22]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn05_display'] = data[row]['extension'][22]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn06_cd'] = data[row]['extension'][23]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn06_display'] = data[row]['extension'][23]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn07_cd'] = data[row]['extension'][24]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn07_display'] = data[row]['extension'][24]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn08_cd'] = data[row]['extension'][25]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn08_display'] = data[row]['extension'][25]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn09_cd'] = data[row]['extension'][26]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn09_display'] = data[row]['extension'][26]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn10_cd'] = data[row]['extension'][27]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn10_display'] = data[row]['extension'][27]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn11_cd'] = data[row]['extension'][28]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn11_display'] = data[row]['extension'][28]['valueCoding']['display']  # buyin02 display
            extension_dict['BuyIn12_cd'] = data[row]['extension'][29]['valueCoding']['code']  # buyin02 code
            extension_dict['BuyIn12_display'] = data[row]['extension'][29]['valueCoding']['display']  # buyin02 display
        except KeyError:
            extension_dict['ms_cd'] = 'Null'
            extension_dict['ms_display'] = 'Null'
            extension_dict['orec_cd'] = 'Null'
            extension_dict['orec_display'] = 'Null'
            extension_dict['crec_cd'] = 'Null'
            extension_dict['crec_display'] = 'Null'
            extension_dict['esrd-id'] = 'Null'
            extension_dict['a_trm_cd'] = 'Null'
            extension_dict['a_trm_display'] = 'Null'
            extension_dict['rfrnc_yr'] = 'Null'
            extension_dict['dual_01_cd'] = 'Null'
            extension_dict['dual_01_display'] = 'Null'
            extension_dict['dual_02_cd'] = 'Null'
            extension_dict['dual_02_display'] = 'Null'
            extension_dict['dual_03_cd'] = 'Null'
            extension_dict['dual_03_display'] = 'Null'  # dual_01_display
            extension_dict['dual_04_cd'] = 'Null'
            extension_dict['dual_04_display'] = 'Null'
            extension_dict['dual_05_cd'] = 'Null'
            extension_dict['dual_05_display'] = 'Null'
            extension_dict['dual_06_cd'] = 'Null'
            extension_dict['dual_06_display'] = 'Null'
            extension_dict['dual_07_cd'] = 'Null'
            extension_dict['dual_07_display'] = 'Null'
            extension_dict['dual_08_cd'] = 'Null'
            extension_dict['dual_08_display'] = 'Null'
            extension_dict['dual_09_cd'] = 'Null'
            extension_dict['dual_09_display'] = 'Null'
            extension_dict['dual_10_cd'] = 'Null'
            extension_dict['dual_10_display'] = 'Null'
            extension_dict['dual_11_cd'] = 'Null'
            extension_dict['dual_11_display'] = 'Null'
            extension_dict['dual_12_cd'] = 'Null'
            extension_dict['dual_12_display'] = 'Null'
            extension_dict['BuyIn01_cd'] = 'Null'
            extension_dict['BuyIn01_display'] = 'Null'
            extension_dict['BuyIn02_cd'] = 'Null'
            extension_dict['BuyIn02_display'] = 'Null'
            extension_dict['BuyIn03_cd'] = 'Null'
            extension_dict['BuyIn03_display'] = 'Null'
            extension_dict['BuyIn04_cd'] = 'Null'
            extension_dict['BuyIn04_display'] = 'Null'
            extension_dict['BuyIn05_cd'] = 'Null'
            extension_dict['BuyIn05_display'] = 'Null'
            extension_dict['BuyIn06_cd'] = 'Null'
            extension_dict['BuyIn06_display'] = 'Null'
            extension_dict['BuyIn07_cd'] = 'Null'
            extension_dict['BuyIn07_display'] = 'Null'
            extension_dict['BuyIn08_cd'] = 'Null'
            extension_dict['BuyIn08_display'] = 'Null'
            extension_dict['BuyIn09_cd'] = 'Null'
            extension_dict['BuyIn09_display'] = 'Null'
            extension_dict['BuyIn10_cd'] = 'Null'
            extension_dict['BuyIn10_display'] = 'Null'
            extension_dict['BuyIn11_cd'] = 'Null'
            extension_dict['BuyIn11_display'] = 'Null'
            extension_dict['BuyIn12_cd'] = 'Null'
            extension_dict['BuyIn12_display'] = 'Null'

    elif row % 4 == 1:
        try:
            extension_dict['b_trm_cd'] = data[row]['extension'][1]['valueCoding']['code']
        except KeyError:
            extension_dict['b_trm_cd'] = 'Null'
        try:
            extension_dict['b_trm_display'] = data[row]['extension'][1]['valueCoding']['display']
        except KeyError:
            extension_dict['b_trm_display'] = 'Null'

    elif row % 4 == 2:
        for x in range(0,12):
            try:
                extension_dict[f'ptc_cntrct_id_{x+1}'] = data[row]['extension'][x]['valueCoding']['code']
            except KeyError:
                extension_dict[f'ptc_cntrct_id_{x + 1}'] = 'Null'
            except IndexError:
                extension_dict[f'ptc_cntrct_id_{x + 1}'] = 'Null'

        for x in range(0,12):
            try:
                extension_dict[f'hmo_ind_{x+1}'] = data[row]['extension'][12+x]['valueCoding']['code']
                extension_dict[f'hmo_ind_display_{x + 1}'] = data[row]['extension'][12 + x]['valueCoding']['display']
            except KeyError:
                extension_dict[f'hmo_ind_{x+1}'] = 'Null'
                extension_dict[f'hmo_ind_display_{x + 1}'] = 'Null'
            except IndexError:
                extension_dict[f'hmo_ind_{x+1}'] = 'Null'
                extension_dict[f'hmo_ind_display_{x + 1}'] = 'Null'

    elif row % 4 == 3:

        for x in range(1,13):
            try:
                extension_dict[f'ptd_cntrct_cd_{x}'] = data[row]['extension'][x]['valueCoding']['code']
                extension_dict[f'ptd_cntrct_display_{x}'] = data[row]['extension'][x]['valueCoding']['display']
            except KeyError:
                extension_dict[f'ptd_cntrct_cd_{x}'] = 'Null'
                extension_dict[f'ptd_cntrct_display_{x}'] = 'Null'

        try:
            extension_dict['ptdpbpid01'] = data[row]['extension'][13]['valueCoding']['code']
        except KeyError:
            extension_dict['ptdpbpid01'] = 'Null'

        try:
            extension_dict['sgmtid01'] = data[row]['extension'][14]['valueCoding']['code']
        except KeyError:
            extension_dict['sgmtid01'] = 'Null'

        for x in range(15,27):
            try:
                extension_dict[f'cstshr_cd_{x-14}'] = data[row]['extension'][x]['valueCoding']['code']
                extension_dict[f'cstshr_display_{x - 14}'] = data[row]['extension'][x]['valueCoding']['display']
            except KeyError:
                extension_dict[f'cstshr_cd_{x-14}'] = 'Null'
                extension_dict[f'cstshr_display_{x - 14}'] = 'Null'

        for x in range(27,39):
            try:
                extension_dict[f'rdsind_cd_{x-26}'] = data[row]['extension'][x]['valueCoding']['code']
                extension_dict[f'rdsind_display_{x - 26}'] = data[row]['extension'][x]['valueCoding']['display']
            except KeyError:
                extension_dict[f'rdsind_cd_{x-26}'] = 'Null'
                extension_dict[f'rdsind_display_{x - 26}'] = 'Null'


def contract_Format(row, file, contract_dict, bool):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    if not bool:
        try:
            contract_dict['Contract_Id'] = data[row]['contract'][0]['id']
            contract_dict['Contract_Reference'] = data[row]['contract'][1]['reference']
        except KeyError:
            contract_dict['Contract_Id'] = 'Null'
            contract_dict['Contract_Reference'] = 'Null'
    else:
        contract_dict['Contract_Id'] = 'Null'
        contract_dict['Contract_Reference'] = 'Null'


fs = 'Coverage_03162021_March29Formatted.json'
x = open(fs)
d = x.read()
data = json.loads(d)
#pprint.pprint(data[0])
#sys.exit()
c = 0
row = 0
masterdf = pd.DataFrame()
masterdf2 = pd.DataFrame()

for x in data:
    c += 1

# beneficiary, contract, extension, grouping, id, meta, period, resourceType, status, type
# beneficiary, extension, grouping, id, meta, period, resourceType, status, type
fields_list = ['beneficiary', 'contract', 'extension', 'grouping', 'id','meta', 'period', 'resourceType', 'status', 'type']

beneficiary_dict = {}
contract_dict = {}
extension_dict = {}
meta_dict = {}
period_dict = {}
resourceType_dict = {}
status_dict = {}
type_dict = {}

dict_list = [beneficiary_dict, contract_dict, extension_dict, meta_dict, period_dict,
             resourceType_dict, status_dict]


while row < c:
    current_FL = []
    missingField = False

    for y in data[row]:
        current_FL.append(y)

    if current_FL == fields_list:
        missingField = False
    else:
        missingField = True

    if row <= 3:
        print(row)
        if row % 4 == 0:
            beneficiary_dict['Subject'] = data[row]['beneficiary']['reference']
            contract_Format(row, fs, contract_dict, missingField)
            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            period_dict['Coverage_Period_Start_Date'] = data[row]['period']['start']
            resourceType_dict['ResourceType'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']

        extension_Format(row, fs, extension_dict)

        if row % 4 == 3:
            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis=1)
            masterdf.to_csv('API_Coverage_Data_03162021_MAR29.csv', index=False)
        row += 1

    elif row > 3:
        masterdf2 = pd.DataFrame()
        print(row)
        if row % 4 == 0:
            beneficiary_dict['Subject'] = data[row]['beneficiary']['reference']
            contract_Format(row, fs, contract_dict, missingField)
            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            period_dict['Coverage_Period_Start_Date'] = data[row]['period']['start']
            resourceType_dict['ResourceType'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']

        extension_Format(row, fs, extension_dict)

        if row % 4 == 3:
            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis=1)
            masterdf2.to_csv('Consecutive_Rows_Coverage.csv', mode='a', index=False, header=False)
        row += 1

if row > 3:
    with open('Consecutive_Rows_Coverage.csv', 'r') as s:
        source = s.read()
    with open('API_Coverage_Data_03162021_MAR29.csv', 'a') as t:
        t.write(source)

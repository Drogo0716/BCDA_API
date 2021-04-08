from BCDA_API.EoB_Func import careTeam_Format, careTeam_Key5_Format, referral_Format, diag_Format, \
    diag_Key6_Format, extension_Key5_Format, item_Key5_Format, type_Outpatient_Format, type_HHA_Format,\
    item_Key6_Format, type_Key7_Format, careTeam_Inpatient_Format, diag_Inpatient_Format, \
    extension_Inpatient_Format, information_Inpatient_Format, item_Key8_Format, procedure_Key8_Format, type_Key8_Format, \
    lookingForItemFields, extension_Key1_Key2_Format, information_Outpatient_Format, information_HHA_Format, \
    diag_Hospice_Format, extension_Hospice_Format, information_Hospice_Format, facility_Outpatient_Format, \
    facility_HHA_Format, extension_HHA_Format, item_Hospice_Format_Most_Recent_Visit
import json, os
import pandas as pd
#######################################################################################################################
#
# EoB_Keys
#
#######################################################################################################################
fs = 'C:\\Users\\Denver_H\\OneDrive\\Documents\\JSON From API\\March16_March29\\API_EoB_Data_03162021_MAR29(Key5_Formatted_Step2).json'
x = open(fs)
d = x.read()
data = json.loads(d)

c = 0
row = 0
dgns = 0

masterdf = pd.DataFrame()
masterdf2 = pd.DataFrame()

for x in data:
    c += 1

ItemFields = ['line_prmry_alowd_chrg_amt', 'line_dme_prchs_price_amt', 'dmerc_line_mtus_cd', 'dmerc_line_mtus_cnt',
              'dmerc_line_scrn_svgs_amt', 'suplrnum', 'carr_line_rdcd_pmt_phys_astn_c', 'line_nch_pmt_amt',
              'line_pmt_80_100_cd', 'line_bene_pmt_amt', 'line_prvdr_pmt_amt', 'line_bene_ptb_ddctbl_amt',
              'line_bene_prmry_pyr_pd_amt', 'line_coinsrnc_amt', 'line_sbmtd_chrg_amt', 'line_alowd_chrg_amt',
              'line_prcsg_ind_cd',
              'careTeamLinkId', 'line_cms_type_srvc_cd', 'diagnosisLinkId', 'carr_line_mtus_cd', 'carr_line_mtus_cnt',
              'betos_cd', 'line_service_deductible', 'line_place_of_srvc_cd', 'prvdr_state_cd', 'prvdr_zip',
              'dmerc_line_prcng_state_cd', 'dmerc_line_supplr_type_cd', 'carr_line_prcng_lclty_cd', 'hcpcs',
              'servicedPeriod']

fields_list = []
for x in data[0]:
    print(x)
    fields_list.append(x)

if fields_list == ['careTeam','facility','id','identifier','information','insurance','item','meta','organization',
                   'patient', 'payment', 'resourceType', 'status','type'] or fields_list == ['careTeam','facility','id','identifier','information','insurance','item','meta','organization',
                   'patient', 'resourceType', 'status','type']:
    print('This is a Pharmaceutical Claims File.')
    while row < c:
        diagnosis_dict = {}
        careTeam_dict = {}
        facility_dict = {}
        identifier_dict = {}
        information_dict = {}
        insurance_dict = {}
        item_dict = {}
        meta_dict = {}
        organization_dict = {}
        patient_dict = {}
        payment_dict = {}
        resourceType_dict = {}
        status_dict = {}
        type_dict = {}
        dict_list = [diagnosis_dict, careTeam_dict, facility_dict, identifier_dict, information_dict, insurance_dict, item_dict,
                     meta_dict, organization_dict, patient_dict, payment_dict, resourceType_dict, status_dict, type_dict]

        if row == 0:
            print(row)

            careTeam_Format(row, fs, careTeam_dict)
            facility_dict['phrmcy_srvc_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
            facility_dict['phrmcy_srvc_type_display'] = data[row]['facility']['extension'][0]['valueCoding']['display']
            facility_dict['Facility_NPI'] = data[row]['facility']['identifier']['value']
            identifier_dict['pde_id'] = data[row]['identifier'][0]['value']
            identifier_dict['claim_group'] = data[row]['identifier'][1]['value']
            identifier_dict['rx_srvc_rfrnc_num'] = data[row]['identifier'][2]['value']
            information_dict['daw_prod_slctn_cd'] = data[row]['information'][0]['code']['coding'][0]['code']
            information_dict['drug_cvrg_stus_cd'] = data[row]['information'][1]['code']['coding'][0]['code']

            if len(data[row]['information']) == 6:
                information_dict['rx_orgn_cd'] = data[row]['information'][2]['code']['coding'][0]['code']
                information_dict['brnd_gnrc_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
                information_dict['ptnt_rsdnc_cd'] = data[row]['information'][5]['code']['coding'][0]['code']

                if information_dict['rx_orgn_cd'] == 'B' or information_dict['rx_orgn_cd'] == 'G':
                    information_dict['rx_orgn_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
                if information_dict['brnd_gnrc_cd'] == 5 or information_dict['brnd_gnrc_cd'] == 4:
                    information_dict['brnd_gnrc_cd'] = data[row]['information'][4]['code']['coding'][0]['code']

            elif len(data[row]['information']) == 7:
                information_dict['rx_orgn_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
                information_dict['brnd_gnrc_cd'] = data[row]['information'][4]['code']['coding'][0]['code']
                information_dict['ptnt_rsdnc_cd'] = data[row]['information'][5]['code']['coding'][0]['code']

                if information_dict['rx_orgn_cd'] == 'B' or information_dict['rx_orgn_cd'] == 'G':
                    information_dict['rx_orgn_cd'] = data[row]['information'][2]['code']['coding'][0]['code']
                if information_dict['brnd_gnrc_cd'] == '5' or information_dict['brnd_gnrc_cd'] == '05':
                    information_dict['brnd_gnrc_cd'] = data[row]['information'][3]['code']['coding'][0]['code']

            elif len(data[row]['information']) == 8:
                information_dict['rx_orgn_cd'] = data[row]['information'][4]['code']['coding'][0]['code']
                information_dict['brnd_gnrc_cd'] = data[row]['information'][5]['code']['coding'][0]['code']
                information_dict['ptnt_rsdnc_cd'] = data[row]['information'][7]['code']['coding'][0]['code']
                if data[row]['information'][7]['code']['coding'][0]['code'] == 'G' or data[row]['information'][7]['code']['coding'][0]['code'] == 'B' :
                    information_dict['ptnt_rsdnc_cd'] = '01'


            insurance_dict['plan_cntrct_rec_id'] = data[row]['insurance']['coverage']['extension'][0]['valueIdentifier']['value']
            insurance_dict['plan_pbp_rec_num'] = data[row]['insurance']['coverage']['extension'][1]['valueIdentifier']['value']
            insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            item_dict['cvrd_d_plan_pd_amt'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
            item_dict['gdc_blw_oopt_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
            item_dict['gdc_abv_oopt_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            item_dict['ptnt_pay_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            item_dict['othr_troop_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
            item_dict['lics_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
            item_dict['plro_amt'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            item_dict['tot_rx_cst_amt'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            item_dict['rptd_gap_dscnt_num'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            try:
                item_dict['careTeamLinkId'] = data[row]['item'][0]['careTeamLinkId']
            except KeyError:
                try:
                    item_dict['careTeamLinkId'] = data[row]['item'][0][' LinkId']
                except KeyError:
                    item_dict['careTeamLinkId'] = 'Null'
            item_dict['ActCode'] = data[row]['item'][0]['detail'][0]['type']['coding'][0]['code']
            item_dict['fillNum'] = data[row]['item'][0]['quantity']['extension'][0]['valueQuantity']['value']
            item_dict['daysSupply'] = data[row]['item'][0]['quantity']['extension'][1]['valueQuantity']['value']
            item_dict['NDC'] = data[row]['item'][0]['service']['coding'][0]['code']
            item_dict['servicedDate'] = data[row]['item'][0]['servicedDate']
            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            patient_dict['Subject'] = data[row]['patient']['reference']

            try:
                payment_dict['lastPaymentDate'] = data[row]['payment']['date']
            except KeyError:
                payment_dict['lastPaymentDate'] = 'Null'

            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            type_dict['Clm_Type'] = data[row]['type']['coding'][1]['display']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis=1)
            masterdf.to_csv('API_EoB_Data_03162021_MAR29(Key8_Formatted_Step2).csv', index=False)
            row += 1

        elif row > 0:
            print(row)
            masterdf2 = pd.DataFrame()

            careTeam_Format(row, fs, careTeam_dict)
            facility_dict['phrmcy_srvc_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
            facility_dict['phrmcy_srvc_type_display'] = data[row]['facility']['extension'][0]['valueCoding']['display']
            facility_dict['Facility_NPI'] = data[row]['facility']['identifier']['value']
            identifier_dict['pde_id'] = data[row]['identifier'][0]['value']
            identifier_dict['claim_group'] = data[row]['identifier'][1]['value']
            identifier_dict['rx_srvc_rfrnc_num'] = data[row]['identifier'][2]['value']
            information_dict['daw_prod_slctn_cd'] = data[row]['information'][0]['code']['coding'][0]['code']
            information_dict['drug_cvrg_stus_cd'] = data[row]['information'][1]['code']['coding'][0]['code']

            if len(data[row]['information']) == 6:
                information_dict['rx_orgn_cd'] = data[row]['information'][2]['code']['coding'][0]['code']
                information_dict['brnd_gnrc_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
                information_dict['ptnt_rsdnc_cd'] = data[row]['information'][5]['code']['coding'][0]['code']

                if information_dict['rx_orgn_cd'] == 'B' or information_dict['rx_orgn_cd'] == 'G':
                    information_dict['rx_orgn_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
                if information_dict['brnd_gnrc_cd'] == 5 or information_dict['brnd_gnrc_cd'] == 4:
                    information_dict['brnd_gnrc_cd'] = data[row]['information'][4]['code']['coding'][0]['code']

            elif len(data[row]['information']) == 7:
                information_dict['rx_orgn_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
                information_dict['brnd_gnrc_cd'] = data[row]['information'][4]['code']['coding'][0]['code']
                information_dict['ptnt_rsdnc_cd'] = data[row]['information'][5]['code']['coding'][0]['code']

                if information_dict['rx_orgn_cd'] == 'B' or information_dict['rx_orgn_cd'] == 'G':
                    information_dict['rx_orgn_cd'] = data[row]['information'][2]['code']['coding'][0]['code']
                if information_dict['brnd_gnrc_cd'] == '5' or information_dict['brnd_gnrc_cd'] == '05':
                    information_dict['brnd_gnrc_cd'] = data[row]['information'][3]['code']['coding'][0]['code']

            elif len(data[row]['information']) == 8:
                information_dict['rx_orgn_cd'] = data[row]['information'][4]['code']['coding'][0]['code']
                information_dict['brnd_gnrc_cd'] = data[row]['information'][5]['code']['coding'][0]['code']
                information_dict['ptnt_rsdnc_cd'] = data[row]['information'][7]['code']['coding'][0]['code']


            insurance_dict['plan_cntrct_rec_id'] = \
            data[row]['insurance']['coverage']['extension'][0]['valueIdentifier']['value']
            insurance_dict['plan_pbp_rec_num'] = data[row]['insurance']['coverage']['extension'][1]['valueIdentifier']['value']
            insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            item_dict['cvrd_d_plan_pd_amt'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
            item_dict['gdc_blw_oopt_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
            item_dict['gdc_abv_oopt_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            item_dict['ptnt_pay_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            item_dict['othr_troop_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
            item_dict['lics_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
            item_dict['plro_amt'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            item_dict['tot_rx_cst_amt'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            item_dict['rptd_gap_dscnt_num'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            item_dict['careTeamLinkId'] = data[row]['item'][0]['careTeamLinkId']
            item_dict['ActCode'] = data[row]['item'][0]['detail'][0]['type']['coding'][0]['code']
            item_dict['fillNum'] = data[row]['item'][0]['quantity']['extension'][0]['valueQuantity']['value']
            item_dict['daysSupply'] = data[row]['item'][0]['quantity']['extension'][1]['valueQuantity']['value']
            item_dict['NDC'] = data[row]['item'][0]['service']['coding'][0]['code']
            item_dict['servicedDate'] = data[row]['item'][0]['servicedDate']
            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            patient_dict['Subject'] = data[row]['patient']['reference']

            try:
                payment_dict['lastPaymentDate'] = data[row]['payment']['date']
            except KeyError:
                payment_dict['lastPaymentDate'] = 'Null'

            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            type_dict['Clm_Type'] = data[row]['type']['coding'][1]['display']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis=1)
            masterdf2.to_csv('consecutive_rows_key8.csv', mode='a', index=False, header=False)
            row += 1
    if row > 1:
        with open('consecutive_rows_key8.csv', 'r') as s:
            source = s.read()
        with open('API_EoB_Data_03162021_MAR29(Key8_Formatted_Step2).csv', 'a') as t:
            # t.write('\n')
            t.write(source)
        s.close()
        t.close()
    row = 0



elif fields_list == ['billablePeriod', 'careTeam', 'diagnosis', 'extension', 'facility', 'id', 'identifier',
'information', 'insurance', 'item', 'meta', 'organization', 'patient', 'payment', 'provider', 'resourceType', 'status',
'totalCost', 'type']:
    print('This is an Outpatient Claims file.')
    while row < c:
        billablePeriod_dict = {}
        careTeam_dict = {}
        diagnosis_dict = {}
        extension_dict = {}
        facility_dict = {}
        id_dict = {}
        identifier_dict = {}
        information_dict = {}
        insurance_dict = {}
        item_dict = {}
        meta_dict = {}
        organization_dict = {}
        patient_dict = {}
        payment_dict = {}
        provider_dict = {}
        resourceType_dict = {}
        status_dict = {}
        totalCost_dict = {}
        type_dict = {}

        dict_list = [billablePeriod_dict, careTeam_dict, diagnosis_dict, extension_dict, facility_dict,
                     id_dict, identifier_dict, information_dict, insurance_dict, item_dict, meta_dict, organization_dict,
                     patient_dict, payment_dict, provider_dict, resourceType_dict, status_dict, totalCost_dict, type_dict]
        print(row)
        if row == 0:

            diag_Format(row, fs, diagnosis_dict)
            careTeam_Key5_Format(row, fs, careTeam_dict)
            extension_Key5_Format(row, fs, extension_dict)
            facility_Outpatient_Format(row, fs, facility_dict)
            item_Key5_Format(row, fs, item_dict)
            type_Outpatient_Format(row, fs, type_dict)
            information_Outpatient_Format(row, fs, information_dict)

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                id_dict['Outpatient_ID'] = data[row]['id']
            except KeyError:
                id_dict['Outpatient_ID'] = 'Null'

            try:
                identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
                identifier_dict['clm_group'] = data[row]['identifier'][1]['value']
            except KeyError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'
            except IndexError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'


            try:
                insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            except KeyError:
                insurance_dict['Coverage'] = 'Null'

            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            organization_dict['organizationNPI'] = data[row]['organization']['identifier']['value']
            patient_dict['Subject'] = data[row]['patient']['reference']
            payment_dict['Patient_Payment'] = data[row]['payment']['amount']['value']
            provider_dict['Prvdr_Num'] = data[row]['provider']['identifier']['value']
            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            totalCost_dict['Total_Cost'] = data[row]['totalCost']['value']


            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis=1)
            masterdf.to_csv('API_EoB_Data_03162021_MAR29(Key6_Formatted_Step2).csv', index=False)
            row += 1

        elif row > 0:
            masterdf2 = pd.DataFrame()

            diag_Format(row, fs, diagnosis_dict)
            careTeam_Key5_Format(row, fs, careTeam_dict)
            extension_Key5_Format(row, fs, extension_dict)
            facility_Outpatient_Format(row, fs, facility_dict)
            item_Key5_Format(row, fs, item_dict)
            type_Outpatient_Format(row, fs, type_dict)
            information_Outpatient_Format(row, fs, information_dict)

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                id_dict['Outpatient_ID'] = data[row]['id']
            except KeyError:
                id_dict['Outpatient_ID'] = 'Null'

            try:
                identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
                identifier_dict['clm_group'] = data[row]['identifier'][1]['value']
            except KeyError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'
            except IndexError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'

            try:
                insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            except KeyError:
                insurance_dict['Coverage'] = 'Null'

            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            organization_dict['organizationNPI'] = data[row]['organization']['identifier']['value']
            patient_dict['Subject'] = data[row]['patient']['reference']
            payment_dict['Patient_Payment'] = data[row]['payment']['amount']['value']
            provider_dict['Prvdr_Num'] = data[row]['provider']['identifier']['value']
            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            totalCost_dict['Total_Cost'] = data[row]['totalCost']['value']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis=1)
            masterdf2.to_csv('consecutive_rows_key6.csv', mode='a', index=False, header=False)
            row += 1

    if row > 1:
        with open('consecutive_rows_key6.csv', 'r') as s:
            source = s.read()
        with open('API_EoB_Data_03162021_MAR29(Key6_Formatted_Step2).csv', 'a') as t:
            # t.write('\n')
            t.write(source)
        s.close()
        t.close()

    row = 0

elif fields_list == ['benefitBalance', 'billablePeriod', 'careTeam', 'diagnosis', 'extension', 'facility', 'id', 'identifier',
'information', 'insurance', 'item', 'meta', 'organization', 'patient', 'payment', 'provider', 'resourceType', 'status',
'totalCost', 'type']:
    print('This is an HHA Claims file.')
    while row < c:
        benefitBalance_dict = {}
        billablePeriod_dict = {}
        careTeam_dict = {}
        diagnosis_dict = {}
        extension_dict = {}
        facility_dict = {}
        id_dict = {}
        identifier_dict = {}
        information_dict = {}
        insurance_dict = {}
        item_dict = {}
        meta_dict = {}
        organization_dict = {}
        patient_dict = {}
        payment_dict = {}
        provider_dict = {}
        resourceType_dict = {}
        status_dict = {}
        totalCost_dict = {}
        type_dict = {}

        dict_list = [benefitBalance_dict, billablePeriod_dict, careTeam_dict, diagnosis_dict, extension_dict, facility_dict,
                     id_dict, identifier_dict, information_dict, insurance_dict, item_dict, meta_dict, organization_dict,
                     patient_dict, payment_dict, provider_dict, resourceType_dict, status_dict, totalCost_dict, type_dict]
        print(row)
        if row == 0:

            diag_Key6_Format(row, fs, diagnosis_dict)
            careTeam_Key5_Format(row, fs, careTeam_dict)
            item_Key6_Format(row, fs, item_dict)
            type_HHA_Format(row, fs, type_dict)
            information_HHA_Format(row, fs, information_dict)
            facility_HHA_Format(row, fs, facility_dict)
            extension_HHA_Format(row, fs, extension_dict)

            try:
                benefitBalance_dict['Benefit-Category'] = data[row]['benefitBalance'][0]['category']['coding'][0]['display']
            except KeyError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            except IndexError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            try:
                benefitBalance_dict['clm_hha_total_visit_cnt'] = data[row]['benefitBalance'][0]['financial'][0]['usedUnsignedInt']
            except KeyError:
                benefitBalance_dict['clm_hha_total_visit_cnt'] = 'Null'
            except IndexError:
                benefitBalance_dict['clm_hha_total_visit_cnt'] = 'Null'

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                id_dict['HHA_ID'] = data[row]['id']
            except KeyError:
                id_dict['HHA_ID'] = 'Null'

            try:
                identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
                identifier_dict['clm_group'] = data[row]['identifier'][1]['value']
            except KeyError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'
            except IndexError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'

            try:
                insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            except KeyError:
                insurance_dict['Coverage'] = 'Null'

            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            organization_dict['organizationNPI'] = data[row]['organization']['identifier']['value']
            patient_dict['Subject'] = data[row]['patient']['reference']
            payment_dict['Patient_Payment'] = data[row]['payment']['amount']['value']
            provider_dict['Prvdr_Num'] = data[row]['provider']['identifier']['value']
            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            totalCost_dict['Total_Cost'] = data[row]['totalCost']['value']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis=1)
            masterdf.to_csv('API_EoB_Data_03162021_MAR29(Key4_Formatted_Step2).csv', index=False)
            row += 1

        elif row > 0:
            masterdf2 = pd.DataFrame()

            diag_Key6_Format(row, fs, diagnosis_dict)
            careTeam_Key5_Format(row, fs, careTeam_dict)
            item_Key6_Format(row, fs, item_dict)
            type_HHA_Format(row, fs, type_dict)
            information_HHA_Format(row, fs, information_dict)
            facility_HHA_Format(row, fs, facility_dict)
            extension_HHA_Format(row, fs, extension_dict)

            try:
                benefitBalance_dict['Benefit-Category'] = data[row]['benefitBalance'][0]['category']['coding'][0]['display']
            except KeyError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            except IndexError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            try:
                benefitBalance_dict['clm_hha_total_visit_cnt'] = data[row]['benefitBalance'][0]['financial'][0]['usedUnsignedInt']
            except KeyError:
                benefitBalance_dict['clm_hha_total_visit_cnt'] = 'Null'
            except IndexError:
                benefitBalance_dict['clm_hha_total_visit_cnt'] = 'Null'

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                id_dict['HHA_ID'] = data[row]['id']
            except KeyError:
                id_dict['HHA_ID'] = 'Null'

            try:
                identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
                identifier_dict['clm_group'] = data[row]['identifier'][1]['value']
            except KeyError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'
            except IndexError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['clm_group'] = 'Null'

            try:
                insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            except KeyError:
                insurance_dict['Coverage'] = 'Null'

            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            organization_dict['organizationNPI'] = data[row]['organization']['identifier']['value']
            patient_dict['Subject'] = data[row]['patient']['reference']
            payment_dict['Patient_Payment'] = data[row]['payment']['amount']['value']
            provider_dict['Prvdr_Num'] = data[row]['provider']['identifier']['value']
            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            totalCost_dict['Total_Cost'] = data[row]['totalCost']['value']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis=1)
            masterdf2.to_csv('consecutive_rows_key4.csv', mode='a', index=False, header=False)
            row += 1

    if row > 1:
        with open('consecutive_rows_key4.csv', 'r') as s:
            source = s.read()
        with open('API_EoB_Data_03162021_MAR29(Key4_Formatted_Step2).csv', 'a') as t:
            # t.write('\n')
            t.write(source)
        s.close()
        t.close()

    row = 0

elif fields_list == ['benefitBalance', 'billablePeriod', 'careTeam', 'diagnosis', 'extension', 'facility', 'hospitalization', 'id', 'identifier',
'information', 'insurance', 'item', 'meta', 'organization', 'patient', 'payment', 'provider', 'resourceType', 'status',
'totalCost', 'type']:
    print('This is a Hospice Claims file.')
    while row < c:
        benefitBalance_dict = {}
        billablePeriod_dict = {}
        careTeam_dict = {}
        diagnosis_dict = {}
        extension_dict = {}
        facility_dict = {}
        hospitalization_dict = {}
        id_dict = {}
        identifier_dict = {}
        information_dict = {}
        insurance_dict = {}
        item_dict = {}
        meta_dict = {}
        organization_dict = {}
        patient_dict = {}
        payment_dict = {}
        provider_dict = {}
        resourceType_dict = {}
        status_dict = {}
        totalCost_dict = {}
        type_dict = {}

        dict_list = [benefitBalance_dict, billablePeriod_dict, careTeam_dict, diagnosis_dict, extension_dict, facility_dict, hospitalization_dict,
                     id_dict, identifier_dict, information_dict, insurance_dict, item_dict, meta_dict,
                     patient_dict, payment_dict, provider_dict, resourceType_dict, status_dict, totalCost_dict, type_dict]

        if row == 0:
            print(row)
            diag_Hospice_Format(row, fs, diagnosis_dict)
            careTeam_Key5_Format(row, fs, careTeam_dict)
            item_Hospice_Format_Most_Recent_Visit(row, fs, item_dict)
            type_Key7_Format(row, fs, type_dict)
            extension_Hospice_Format(row,fs, extension_dict)
            information_Hospice_Format(row, fs, information_dict)

            try:
                benefitBalance_dict['Benefit-Category'] = data[row]['benefitBalance'][0]['category']['coding'][0]['display']
            except KeyError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            except IndexError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            try:
                benefitBalance_dict['clm_utlztn_day_cnt'] = data[row]['benefitBalance'][0]['financial'][0]['usedUnsignedInt']
            except KeyError:
                benefitBalance_dict['clm_utlztn_day_cnt'] = 'Null'
            except IndexError:
                benefitBalance_dict['clm_utlztn_day_cnt'] = 'Null'

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                facility_dict['Facility_NPI'] = data[0]['facility']['identifier']['value']
                facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
                facility_dict['clm_fac_type_display'] = data[row]['facility']['extension'][0]['valueCoding']['display']
            except KeyError:
                facility_dict['Facility_NPI'] = 'Null'
                facility_dict['clm_fac_type_cd'] = 'Null'
                facility_dict['clm_fac_type_display'] = 'Null'

            try:
                hospitalization_dict['bene_hospc_prd_cnt'] = data[row]['hospitalization']['extension'][0]['valueQuantity']['value']
            except KeyError:
                hospitalization_dict['bene_hospc_prd_cnt'] = 'Null'
            try:
                hospitalization_dict['bene_hospc_prd_serviceStartDate'] = data[row]['hospitalization']['start']
            except KeyError:
                hospitalization_dict['bene_hospc_prd_serviceStartDate'] = 'Null'
            try:
                hospitalization_dict['bene_hospc_prd_serviceEndDate'] = data[row]['hospitalization']['end']
            except KeyError:
                hospitalization_dict['bene_hospc_prd_serviceEndDate'] = 'Null'

            try:
                id_dict['Hospice_ID'] = data[row]['id']
            except KeyError:
                id_dict['Hospice_ID'] = 'Null'

            try:
                identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
                identifier_dict['claim_group'] = data[row]['identifier'][1]['value']
            except KeyError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['claim_group'] = 'Null'

            try:
                insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            except KeyError:
                insurance_dict['Coverage'] = 'Null'

            try:
                meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            except KeyError:
                meta_dict['lastUpdated'] = 'Null'

            try:
                patient_dict['Subject'] = data[row]['patient']['reference']
            except KeyError:
                patient_dict['Subject'] = 'Null'

            try:
                payment_dict['Total_Payment_Amt'] = data[row]['payment']['amount']['value']
            except KeyError:
                payment_dict['Total_Payment_Amt'] = 'Null'

            try:
                totalCost_dict['Total_Cost'] = data[row]['totalCost']['value']
            except KeyError:
                totalCost_dict['Total_Cost'] = 'Null'

            try:
                provider_dict['Prvdr_ID_Num'] = data[row]['provider']['identifier']['value']
            except KeyError:
                provider_dict['Prvdr_ID_Num'] = 'Null'

            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis=1)
            masterdf.to_csv('API_EoB_Data_03162021_MAR29(Key7_Formatted_Step2).csv', index=False)
            row += 1

        elif row > 0:
            print(row)
            masterdf2 = pd.DataFrame()

            diag_Hospice_Format(row, fs, diagnosis_dict)
            careTeam_Key5_Format(row, fs, careTeam_dict)
            item_Hospice_Format_Most_Recent_Visit(row, fs, item_dict)
            type_Key7_Format(row, fs, type_dict)
            extension_Hospice_Format(row, fs, extension_dict)
            information_Hospice_Format(row, fs, information_dict)

            try:
                benefitBalance_dict['Benefit-Category'] = data[row]['benefitBalance'][0]['category']['coding'][0]['display']
            except KeyError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            except IndexError:
                benefitBalance_dict['Benefit-Category'] = 'Null'
            try:
                benefitBalance_dict['clm_utlztn_day_cnt'] = data[row]['benefitBalance'][0]['financial'][0]['usedUnsignedInt']
            except KeyError:
                benefitBalance_dict['clm_utlztn_day_cnt'] = 'Null'
            except IndexError:
                benefitBalance_dict['clm_utlztn_day_cnt'] = 'Null'

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                facility_dict['Facility_NPI'] = data[0]['facility']['identifier']['value']
                facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
                facility_dict['clm_fac_type_display'] = data[row]['facility']['extension'][0]['valueCoding']['display']
            except KeyError:
                facility_dict['Facility_NPI'] = 'Null'
                facility_dict['clm_fac_type_cd'] = 'Null'
                facility_dict['clm_fac_type_display'] = 'Null'

            try:
                hospitalization_dict['bene_hospc_prd_cnt'] = \
                data[row]['hospitalization']['extension'][0]['valueQuantity']['value']
            except KeyError:
                hospitalization_dict['bene_hospc_prd_cnt'] = 'Null'
            try:
                hospitalization_dict['bene_hospc_prd_serviceStartDate'] = data[row]['hospitalization']['start']
            except KeyError:
                hospitalization_dict['bene_hospc_prd_serviceStartDate'] = 'Null'
            try:
                hospitalization_dict['bene_hospc_prd_serviceEndDate'] = data[row]['hospitalization']['end']
            except KeyError:
                hospitalization_dict['bene_hospc_prd_serviceEndDate'] = 'Null'

            try:
                id_dict['Hospice_ID'] = data[row]['id']
            except KeyError:
                id_dict['Hospice_ID'] = 'Null'

            try:
                identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
                identifier_dict['claim_group'] = data[row]['identifier'][1]['value']
            except KeyError:
                identifier_dict['clm_id'] = 'Null'
                identifier_dict['claim_group'] = 'Null'

            try:
                insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            except KeyError:
                insurance_dict['Coverage'] = 'Null'

            try:
                meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            except KeyError:
                meta_dict['lastUpdated'] = 'Null'

            try:
                patient_dict['Subject'] = data[row]['patient']['reference']
            except KeyError:
                patient_dict['Subject'] = 'Null'

            try:
                payment_dict['Total_Payment_Amt'] = data[row]['payment']['amount']['value']
            except KeyError:
                payment_dict['Total_Payment_Amt'] = 'Null'

            try:
                totalCost_dict['Total_Cost'] = data[row]['totalCost']['value']
            except KeyError:
                totalCost_dict['Total_Cost'] = 'Null'

            try:
                provider_dict['Prvdr_ID_Num'] = data[row]['provider']['identifier']['value']
            except KeyError:
                provider_dict['Prvdr_ID_Num'] = 'Null'

            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis=1)
            masterdf2.to_csv('consecutive_rows_key7.csv', mode='a', index=False, header=False)
            row += 1

    if row > 1:
        with open('consecutive_rows_key7.csv', 'r') as s:
            source = s.read()
        with open('API_EoB_Data_03162021_MAR29(Key7_Formatted_Step2).csv', 'a') as t:
            # t.write('\n')
            t.write(source)
        s.close()
        t.close()

    row = 0

elif fields_list == ['benefitBalance', 'billablePeriod', 'careTeam', 'diagnosis', 'extension', 'facility', 'hospitalization', 'id', 'identifier',
'information', 'insurance', 'item', 'meta', 'organization', 'patient', 'payment','procedure', 'provider', 'resourceType', 'status',
'totalCost', 'type']:
    print('This is a Inpatient Claims file.')
    while row < c:
        benefitBalance_dict = {}
        billablePeriod_dict = {}
        careTeam_dict = {}
        diagnosis_dict = {}
        extension_dict = {}
        facility_dict = {}
        hospitalization_dict = {}
        id_dict = {}
        identifier_dict = {}
        information_dict = {}
        insurance_dict = {}
        item_dict = {}
        meta_dict = {}
        organization_dict = {}
        patient_dict = {}
        payment_dict = {}
        provider_dict = {}
        procedure_dict = {}
        resourceType_dict = {}
        status_dict = {}
        totalCost_dict = {}
        type_dict = {}

        dict_list = [benefitBalance_dict, billablePeriod_dict, careTeam_dict, diagnosis_dict, extension_dict,
                     facility_dict, hospitalization_dict, id_dict, identifier_dict, information_dict, insurance_dict, item_dict, meta_dict,
                     organization_dict, patient_dict, payment_dict, procedure_dict, provider_dict, resourceType_dict, status_dict, totalCost_dict,
                     type_dict]

        if row == 0:

            try:
                diagnosis_dict['clm_drg_cd'] = data[row]['diagnosis'][0]['packageCode']['coding'][0]['code']
            except KeyError:
                diagnosis_dict['clm_drg_cd'] = 'Null'

            careTeam_Inpatient_Format(row, fs, careTeam_dict)
            diag_Inpatient_Format(row, fs, diagnosis_dict)
            extension_Inpatient_Format(row, fs, extension_dict)
            information_Inpatient_Format(row, fs, information_dict)
            item_Key8_Format(row, fs, item_dict)
            procedure_Key8_Format(row, fs, procedure_dict)
            type_Key8_Format(row, fs, type_dict)

            try:
                benefitBalance_dict['benefit_category'] = data[row]['benefitBalance'][0]['category']['coding'][0]['display']
                benefitBalance_dict['Bene_Total_Coinsurance_Days'] = data[row]['benefitBalance'][0]['financial'][0]['usedUnsignedInt']
                benefitBalance_dict['Claim_Medicare_Non_Utilization_Days'] = data[row]['benefitBalance'][0]['financial'][1]['usedUnsignedInt']
                benefitBalance_dict['Claim_Medicare_Utilization_Days'] = data[row]['benefitBalance'][0]['financial'][2]['usedUnsignedInt']
            except KeyError:
                benefitBalance_dict['benefit_category'] = 'Null'
                benefitBalance_dict['Bene_Total_Coinsurance_Days'] = 'Null'
                benefitBalance_dict['Claim_Medicare_Non_Utilization_Days'] = 'Null'
                benefitBalance_dict['Claim_Medicare_Utilization_Days'] = 'Null'

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
                facility_dict['clm_fac_type_display'] = data[row]['facility']['extension'][0]['valueCoding']['display']
                facility_dict['Facility_NPI'] = data[row]['facility']['identifier']['value']
            except KeyError:
                facility_dict['clm_fac_type_cd'] = 'Null'
                facility_dict['clm_fac_type_display'] = 'Null'
                facility_dict['Facility_NPI'] = 'Null'

            try:
                hospitalization_dict['Hospitalization_Start'] = data[row]['hospitalization']['start']
                hospitalization_dict['Hospitalization_End'] = data[row]['hospitalization']['end']
            except:
                hospitalization_dict['Hospitalization_Start'] = 'Null'
                hospitalization_dict['Hospitalization_End'] = 'Null'

            id_dict['Inpatient_Id'] = data[row]['id']
            identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
            identifier_dict['clm_group'] = data[row]['identifier'][1]['value']
            insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            organization_dict['Organization_NPI'] = data[row]['organization']['identifier']['value']
            patient_dict['Subject'] = data[row]['patient']['reference']
            payment_dict['Total_Payments'] = data[row]['payment']['amount']['value']
            provider_dict['Provider_Num'] = data[row]['provider']['identifier']['value']
            resourceType_dict['ResourceType'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            totalCost_dict['Total Cost'] = data[row]['totalCost']['value']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis = 1)
            masterdf.to_csv('API_EoB_Data_03162021_MAR29(Key5_Formatted_Step2).csv', index = False)
            row += 1

        elif row > 0:
            masterdf2 = pd.DataFrame()

            try:
                diagnosis_dict['clm_drg_cd'] = data[row]['diagnosis'][0]['packageCode']['coding'][0]['code']
            except KeyError:
                diagnosis_dict['clm_drg_cd'] = 'Null'

            careTeam_Inpatient_Format(row, fs, careTeam_dict)
            diag_Inpatient_Format(row,fs,diagnosis_dict)
            extension_Inpatient_Format(row,fs,extension_dict)
            information_Inpatient_Format(row,fs,information_dict)
            item_Key8_Format(row,fs,item_dict)
            procedure_Key8_Format(row, fs, procedure_dict)
            type_Key8_Format(row, fs, type_dict)

            try:
                benefitBalance_dict['benefit_category'] = data[row]['benefitBalance'][0]['category']['coding'][0]['display']
                benefitBalance_dict['Bene_Total_Coinsurance_Days'] = data[row]['benefitBalance'][0]['financial'][0]['usedUnsignedInt']
                benefitBalance_dict['Claim_Medicare_Non_Utilization_Days'] = data[row]['benefitBalance'][0]['financial'][1]['usedUnsignedInt']
                benefitBalance_dict['Claim_Medicare_Utilization_Days'] = data[row]['benefitBalance'][0]['financial'][2]['usedUnsignedInt']
            except KeyError:
                benefitBalance_dict['benefit_category'] = 'Null'
                benefitBalance_dict['Bene_Total_Coinsurance_Days'] = 'Null'
                benefitBalance_dict['Claim_Medicare_Non_Utilization_Days'] = 'Null'
                benefitBalance_dict['Claim_Medicare_Utilization_Days'] = 'Null'

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
                facility_dict['clm_fac_type_display'] = data[row]['facility']['extension'][0]['valueCoding']['display']
                facility_dict['Facility_NPI'] = data[row]['facility']['identifier']['value']
            except KeyError:
                facility_dict['clm_fac_type_cd'] = 'Null'
                facility_dict['clm_fac_type_display'] = 'Null'
                facility_dict['Facility_NPI'] = 'Null'

            try:
                hospitalization_dict['Hospitalization_Start'] = data[row]['hospitalization']['start']
                hospitalization_dict['Hospitalization_End'] = data[row]['hospitalization']['end']
            except:
                hospitalization_dict['Hospitalization_Start'] = 'Null'
                hospitalization_dict['Hospitalization_End'] = 'Null'

            id_dict['Inpatient_Id'] = data[row]['id']
            identifier_dict['clm_id'] = data[row]['identifier'][0]['value']
            identifier_dict['clm_group'] = data[row]['identifier'][1]['value']
            insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            meta_dict['lastUpdated'] = data[row]['meta']['lastUpdated']
            organization_dict['Organization_NPI'] = data[row]['organization']['identifier']['value']
            patient_dict['Subject'] = data[row]['patient']['reference']
            payment_dict['Total_Payments'] = data[row]['payment']['amount']['value']
            provider_dict['Provider_Num'] = data[row]['provider']['identifier']['value']
            resourceType_dict['ResourceType'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            totalCost_dict['Total Cost'] = data[row]['totalCost']['value']

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis = 1)
            masterdf2.to_csv('consecutive_rows_key5.csv', mode = 'a', index = False, header = False)
            row += 1

    if row > 1:
        with open('consecutive_rows_key5.csv', 'r') as s:
            source = s.read()
        with open('API_EoB_Data_03162021_MAR29(Key5_Formatted_Step2).csv', 'a') as t:
            t.write(source)
        s.close()
        t.close()

    if os.path.exists('.\\consecutive_rows_key5.csv'):
        os.remove('.\\consecutive_rows_key5.csv')
        print('Consecutive row file deleted!')
    else:
        print('No consecutive row file to delete!')

else:
    print('This is a Physician/DME claims file.')
    while row < c:
        n = 0
        ext = -1
        billablePeriod_dict = {}
        careTeam_dict = {}
        contained_dict = {}
        diagnosis_dict = {}
        disposition_dict = {}
        extension_dict = {}
        identifier_dict = {}
        insurance_dict = {}
        item_dict = {}
        meta_dict = {}
        payment_dict = {}
        referral_dict = {}
        resourceType_dict = {}
        status_dict = {}
        type_dict = {}
        split = 4
        dict_list = [billablePeriod_dict, careTeam_dict, contained_dict, diagnosis_dict, disposition_dict,
                     extension_dict, identifier_dict, insurance_dict, item_dict, meta_dict, payment_dict, referral_dict,
                     resourceType_dict, status_dict, type_dict]

        print(row)
        if row == 0:

            diag_Format(row, fs, diagnosis_dict)
            careTeam_Format(row, fs, careTeam_dict)
            extension_Key1_Key2_Format(row, fs, extension_dict)
            referral_Format(row, fs, referral_dict)
            lookingForItemFields(ItemFields, fs, row, item_dict, ItemFields, split)

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                disposition_dict['Disposition'] = data[row]['disposition']
            except KeyError:
                disposition_dict['Disposition'] = 'Null'


            try:
                contained_dict['Subject'] = data[row]['contained'][0]['subject']['reference']
            except KeyError:
                try:
                    contained_dict['Subject'] = data[row]['patient']['reference']
                except KeyError:
                    contained_dict['Subject'] = 'Null'

            identifier_dict['Clm_ID'] = data[row]['identifier'][0]['value']
            identifier_dict['Clm_Group'] = data[row]['identifier'][1]['value']
            insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            type_dict['Clm_Type_Cd'] = data[row]['type']['coding'][0]['code']
            meta_dict['Last_Updated'] = data[row]['meta']['lastUpdated']

            try:
                payment_dict['Payment_Amount'] = data[row]['payment']['amount']['value']
            except KeyError:
                payment_dict['payment_Amount'] = 'Null'

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf = pd.concat([masterdf, df], axis=1)
            masterdf.to_csv('API_EoB_Data_03162021_MAR29(Key2_Formatted_Step2).csv', index=False)
            row += 1

        elif row > 0:
            n = 0
            ext = -1
            masterdf2 = pd.DataFrame()

            diag_Format(row, fs, diagnosis_dict)
            careTeam_Format(row, fs, careTeam_dict)
            extension_Key1_Key2_Format(row, fs, extension_dict)
            referral_Format(row, fs, referral_dict)
            lookingForItemFields(ItemFields, fs, row, item_dict, ItemFields, split)

            try:
                billablePeriod_dict['Start'] = data[row]['billablePeriod']['start']
                billablePeriod_dict['End'] = data[row]['billablePeriod']['end']
            except KeyError:
                billablePeriod_dict['Start'] = 'Null'
                billablePeriod_dict['End'] = 'Null'

            try:
                disposition_dict['Disposition'] = data[row]['disposition']
            except KeyError:
                disposition_dict['Disposition'] = 'Null'

            try:
                contained_dict['Subject'] = data[row]['contained'][0]['subject']['reference']
            except KeyError:
                try:
                    contained_dict['Subject'] = data[row]['patient']['reference']
                except KeyError:
                    contained_dict['Subject'] = 'Null'

            identifier_dict['Clm_ID'] = data[row]['identifier'][0]['value']
            identifier_dict['Clm_Group'] = data[row]['identifier'][1]['value']
            insurance_dict['Coverage'] = data[row]['insurance']['coverage']['reference']
            resourceType_dict['Resource'] = data[row]['resourceType']
            status_dict['Status'] = data[row]['status']
            type_dict['Clm_Type_Cd'] = data[row]['type']['coding'][0]['code']
            meta_dict['Last_Updated'] = data[row]['meta']['lastUpdated']

            try:
                payment_dict['Payment_Amount'] = data[row]['payment']['amount']['value']
            except KeyError:
                payment_dict['Payment_Amount'] = 'Null'

            for i in dict_list:
                df = pd.DataFrame([i])
                masterdf2 = pd.concat([masterdf2, df], axis=1)
            masterdf2.to_csv('consecutive_rows_key2.csv', mode='a', index=False, header=False)
            row += 1

    if row > 1:
        with open('consecutive_rows_key2.csv', 'r') as s:
            source = s.read()
        with open('API_EoB_Data_03162021_MAR29(Key2_Formatted_Step2).csv', 'a') as t:
            # t.write('\n')
            t.write(source)
        s.close()
        t.close()

    row = 0

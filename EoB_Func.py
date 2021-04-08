import json
import datetime as dt
import re, sys
import logging

logging.basicConfig(filename='../item_Hospice_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='diag_Hospice_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
#logging.disable(logging.INFO)
def type_HHA_Format(row, file, type_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        type_dict['nch_clm_type_cd '] = data[row]['type']['coding'][0]['code']
    except (KeyError, IndexError):
        type_dict['nch_clm_type_cd '] = 'Null'

    try:
        type_dict['nch_clm_type_display'] = data[row]['type']['coding'][0]['display']
    except (KeyError, IndexError):
        type_dict['nch_clm_type_display'] = 'Null'

    try:
        type_dict['eob_type'] = data[row]['type']['coding'][1]['code']
    except (KeyError, IndexError):
        type_dict['eob_type'] = 'Null'

    try:
        type_dict['nch_near_line_rec_ident_cd'] = data[row]['type']['coding'][2]['code']
    except (KeyError, IndexError):
        type_dict['nch_near_line_rec_ident_cd'] = 'Null'

    try:
        type_dict['nch_near_line_rec_ident_display'] = data[row]['type']['coding'][2]['display']
    except (KeyError, IndexError):
        type_dict['nch_near_line_rec_ident_display'] = 'Null'

    try:
        type_dict['clm_srvc_clsfctn_type_cd'] = data[row]['type']['coding'][3]['code']
    except (KeyError, IndexError):
        type_dict['clm_srvc_clsfctn_type_cd'] = 'Null'


def type_Outpatient_Format (row, file, type_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        type_dict['nch_clm_type_cd '] = data[row]['type']['coding'][0]['code']
    except (KeyError, IndexError):
        type_dict['nch_clm_type_cd '] = 'Null'

    try:
        type_dict['nch_clm_type_display'] = data[row]['type']['coding'][0]['display']
    except (KeyError, IndexError):
        type_dict['nch_clm_type_display'] = 'Null'

    try:
        type_dict['eob_type'] = data[row]['type']['coding'][1]['code']
    except (KeyError, IndexError):
        type_dict['eob_type'] = 'Null'

    try:
        type_dict['ex-claimtype']= data[row]['type']['coding'][2]['display']
    except (KeyError, IndexError):
        type_dict['ex-claimtype'] = 'Null'

    try:
        type_dict['nch_near_line_rec_ident_cd'] = data[row]['type']['coding'][3]['code']
    except (KeyError, IndexError):
        type_dict['nch_near_line_rec_ident_cd'] = 'Null'

    try:
        type_dict['nch_near_line_rec_ident_display'] = data[row]['type']['coding'][3]['display']
    except (KeyError, IndexError):
        type_dict['nch_near_line_rec_ident_display'] = 'Null'

    try:
        type_dict['clm_srvc_clsfctn_type_cd'] = data[row]['type']['coding'][4]['code']
    except (KeyError, IndexError):
        type_dict['clm_srvc_clsfctn_type_cd'] = 'Null'


def type_Key7_Format (row, file, type_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        type_dict['nch_clm_type_cd'] = data[row]['type']['coding'][0]['code']
    except KeyError:
        type_dict['nch_clm_type_cd'] = 'Null'
    try:
        type_dict['nch_clm_type_display'] = data[row]['type']['coding'][0]['display']
    except KeyError:
        type_dict['nch_clm_type_display'] = 'Null'
    try:
        type_dict['EoB_Type'] = data[row]['type']['coding'][1]['code']
    except KeyError:
        type_dict['EoB_Type'] = 'Null'
    try:
        type_dict['ex-ClaimType'] = data[row]['type']['coding'][2]['display']
    except KeyError:
        type_dict['ex-ClaimType'] = 'Null'
    try:
        type_dict['nch_near_line_rec_ident_cd'] = data[row]['type']['coding'][3]['code']
    except KeyError:
        type_dict['nch_near_line_rec_ident_cd'] = 'Null'
    try:
        type_dict['nch_near_line_rec_ident_display'] = data[row]['type']['coding'][3]['display']
    except KeyError:
        type_dict['nch_near_line_rec_ident_display'] = 'Null'
    try:
        type_dict['clm_srvc_clsfctn_type_cd'] = data[row]['type']['coding'][4]['code']
    except KeyError:
        type_dict['clm_srvc_clsfctn_type_cd'] = 'Null'


def type_Key8_Format (row, file, type_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        type_dict['nch_clm_type_cd'] = data[row]['type']['coding'][0]['code']
    except KeyError:
        type_dict['nch_clm_type_cd'] = 'Null'
    try:
        type_dict['nch_clm_type_display'] = data[row]['type']['coding'][0]['display']
    except KeyError:
        type_dict['nch_clm_type_display'] = 'Null'
    try:
        type_dict['EoB_Type'] = data[row]['type']['coding'][1]['code']
    except KeyError:
        type_dict['EoB_Type'] = 'Null'
    try:
        type_dict['Ex-ClaimType'] = data[row]['type']['coding'][2]['display']
    except KeyError:
        type_dict['Ex-ClaimType'] = 'Null'
    try:
        type_dict['nch_near_line_rec_ident_cd'] = data[row]['type']['coding'][3]['code']
    except KeyError:
        type_dict['nch_near_line_rec_ident_cd'] = 'Null'
    try:
        type_dict['nch_near_line_rec_ident_display'] = data[row]['type']['coding'][3]['display']
    except KeyError:
        type_dict['nch_near_line_rec_ident_display'] = 'Null'
    try:
        type_dict['clm_srvc_clsfctn_type_cd'] = data[row]['type']['coding'][4]['code']
    except KeyError:
        type_dict['clm_srvc_clsfctn_type_cd'] = 'Null'


def item_Key8_Format(row, file, item_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    itemC = 30
    for item in range(0, itemC):
       try:
           item_dict[f'rev_cntr_rate_amt Adj#{item + 1}'] = data[row]['item'][item]['adjudication'][0]['amount']['value']
       except KeyError:
           item_dict[f'rev_cntr_rate_amt Adj#{item + 1}'] = 'Null'
       except IndexError:
           item_dict[f'rev_cntr_rate_amt Adj#{item + 1}'] = 'Null'

       try:
           item_dict[f'rev_cntr_tot_chrg_amt Adj#{item + 1}'] = data[row]['item'][item]['adjudication'][1]['amount']['value']
       except KeyError:
           item_dict[f'rev_cntr_tot_chrg_amt Adj#{item + 1}'] = 'Null'
       except IndexError:
           item_dict[f'rev_cntr_tot_chrg_amt Adj#{item + 1}'] = 'Null'


       try:
           item_dict[f'rev_cntr_ncvrd_chrg_amt Adj#{item + 1}'] = data[row]['item'][item]['adjudication'][2]['amount']['value']
       except KeyError:
           item_dict[f'rev_cntr_ncvrd_chrg_amt Adj#{item + 1}'] = 'Null'
       except IndexError:
           item_dict[f'rev_cntr_ncvrd_chrg_amt Adj#{item + 1}'] = 'Null'


       try:
           item_dict[f'State of Service Adj#{item + 1}'] = data[row]['item'][item]['locationAddress']['state']
       except KeyError:
           item_dict[f'State of Service Adj#{item + 1}'] = 'Null'
       except IndexError:
           item_dict[f'State of Service Adj#{item + 1}'] = 'Null'


       try:
           item_dict[f'rev_cntr_cd Adj#{item + 1}'] = data[row]['item'][item]['revenue']['coding'][0]['code']
       except KeyError:
           item_dict[f'rev_cntr_cd Adj#{item + 1}'] = 'Null'
       except IndexError:
           item_dict[f'rev_cntr_cd Adj#{item + 1}'] = 'Null'


       try:
           item_dict[f'rev_cntr_display Adj#{item + 1}'] = data[row]['item'][item]['revenue']['coding'][0]['display']
       except KeyError:
           item_dict[f'rev_cntr_display Adj#{item + 1}'] = 'Null'
       except IndexError:
           item_dict[f'rev_cntr_display Adj#{item + 1}'] = 'Null'


def item_Hospice_Format (row, file, item_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    i = 0
    j = 1
    logging.debug('Beginning debugging for record %s of the %s file' %(row, file))
    for x in range(0, 10):

        logging.debug(f'Rev_Cntr Encounter #{x}')

        if len(data[row]['item'][0]['adjudication']) == 3:

            logging.debug('The first condition checked evaluates to: ' +
                          str(len(data[row]['item'][0]['adjudication']) == 3))

            item_dict[f'rev_cntr_prvdr_pmt_amt: Visit #{x + 1}'] = 'Null'
            item_dict[f'rev_cntr_bene_pmt_amt: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'rev_cntr_rate_amt: Visit #{x + 1}'] = \
                    data[row]['item'][i]['adjudication'][0]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'rev_cntr_rate_amt: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'rev_cntr_tot_chrg_amt: Visit #{x + 1}'] = \
                    data[row]['item'][i]['adjudication'][1]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'rev_cntr_tot_chrg_amt: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'rev_cntr_ncvrd_chrg_amt: Visit #{x + 1}'] = \
                data[row]['item'][i]['adjudication'][2]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'rev_cntr_ncvrd_chrg_amt: Visit #{x + 1}'] = 'Null'

            item_dict[f'rev_cntr_pmt_amt_amt: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'Prvdr_State: Visit #{x + 1}'] = data[row]['item'][i]['locationAddress']['state']
            except (KeyError, IndexError):
                item_dict[f'Prvdr_State: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'rev_cntr_cd: Visit #{x + 1}'] = data[row]['item'][i]['revenue']['coding'][0]['code']
            except (KeyError, IndexError):
                item_dict[f'rev_cntr_cd: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'rev_cntr_display: Visit #{x + 1}'] = data[row]['item'][i]['revenue']['coding'][0]['display']
            except (KeyError, IndexError):
                item_dict[f'rev_cntr_display: Visit #{x + 1}'] = 'Null'

            try:
                item_dict[f'HCPCS: Visit #{x + 1}'] = data[row]['item'][0]['service']['coding'][0]['code']
            except (KeyError, IndexError):
                item_dict[f'HCPCS: Visit #{x + 1}'] = 'Null'

            item_dict[f'serviced_date: Visit #{x + 1}'] = 'Null'

            i += 1

        else:
            logging.debug(f"'else' block is executing for record {row} ")
            for x in range(0, 10):
                try:
                   item_dict[f'rev_cntr_prvdr_pmt_amt: Visit #{x+1}'] = data[row]['item'][i]['adjudication'][0]['amount']['value']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_prvdr_pmt_amt: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_bene_pmt_amt: Visit #{x+1}'] = data[row]['item'][i]['adjudication'][1]['amount']['value']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_bene_pmt_amt: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_rate_amt: Visit #{x+1}'] = data[row]['item'][i]['adjudication'][2]['amount']['value']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_rate_amt: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_tot_chrg_amt: Visit #{x+1}'] = data[row]['item'][i]['adjudication'][3]['amount']['value']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_tot_chrg_amt: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_ncvrd_chrg_amt: Visit #{x+1}'] = data[row]['item'][i]['adjudication'][4]['amount']['value']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_ncvrd_chrg_amt: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_pmt_amt_amt: Visit #{x+1}'] = data[row]['item'][i]['adjudication'][5]['amount']['value']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_pmt_amt_amt: Visit #{x+1}'] = 'Null'

                i += 2

                try:
                   item_dict[f'Prvdr_State: Visit #{x+1}'] = data[row]['item'][j]['locationAddress']['state']
                except (KeyError, IndexError):
                   item_dict[f'Prvdr_State: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_cd: Visit #{x+1}'] = data[row]['item'][j]['revenue']['coding'][0]['code']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_cd: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'rev_cntr_display: Visit #{x+1}'] = data[row]['item'][j]['revenue']['coding'][0]['display']
                except (KeyError, IndexError):
                   item_dict[f'rev_cntr_display: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'HCPCS: Visit #{x+1}'] = data[row]['item'][j]['service']['coding'][0]['code']
                except (KeyError, IndexError):
                   item_dict[f'HCPCS: Visit #{x+1}'] = 'Null'

                try:
                   item_dict[f'serviced_date: Visit #{x+1}'] = data[row]['item'][j]['servicedDate']
                except (KeyError, IndexError):
                   item_dict[f'serviced_date: Visit #{x+1}'] = 'Null'

                j += 2


def item_Hospice_Format_Most_Recent_Visit (row, file, item_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    i = 0
    j = 1
    logging.debug('Beginning debugging for record %s of the %s file' %(row, file))
    logging.debug(f'Rev_Cntr Encounter #{x}')

    if len(data[row]['item'][0]['adjudication']) == 3:

        logging.debug('The first condition checked evaluates to: ' +
                      str(len(data[row]['item'][0]['adjudication']) == 3))

        item_dict[f'rev_cntr_prvdr_pmt_amt'] = 'Null'
        item_dict[f'rev_cntr_bene_pmt_amt'] = 'Null'

        try:
            item_dict['rev_cntr_rate_amt'] = \
                data[row]['item'][0]['adjudication'][0]['amount']['value']
        except (KeyError, IndexError):
            item_dict['rev_cntr_rate_amt'] = 'Null'

        try:
            item_dict['rev_cntr_tot_chrg_amt'] = \
                data[row]['item'][0]['adjudication'][1]['amount']['value']
        except (KeyError, IndexError):
            item_dict['rev_cntr_tot_chrg_amt'] = 'Null'

        try:
            item_dict['rev_cntr_ncvrd_chrg_amt'] = \
            data[row]['item'][0]['adjudication'][2]['amount']['value']
        except (KeyError, IndexError):
            item_dict['rev_cntr_ncvrd_chrg_amt'] = 'Null'

        item_dict['rev_cntr_pmt_amt_amt'] = 'Null'

        try:
            item_dict['Prvdr_State'] = data[row]['item'][0]['locationAddress']['state']
        except (KeyError, IndexError):
            item_dict['Prvdr_State'] = 'Null'

        try:
            item_dict['rev_cntr_cd'] = data[row]['item'][0]['revenue']['coding'][0]['code']
        except (KeyError, IndexError):
            item_dict['rev_cntr_cd'] = 'Null'

        try:
            item_dict['rev_cntr_display'] = data[row]['item'][0]['revenue']['coding'][0]['display']
        except (KeyError, IndexError):
            item_dict['rev_cntr_display'] = 'Null'

        try:
            item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
        except (KeyError, IndexError):
            item_dict['HCPCS'] = 'Null'

        item_dict['serviced_date'] = 'Null'


    else:
        logging.debug(f"'else' block is executing for record {row} ")
        try:
           item_dict['rev_cntr_prvdr_pmt_amt'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
        except (KeyError, IndexError):
           item_dict['rev_cntr_prvdr_pmt_amt'] = 'Null'

        try:
           item_dict['rev_cntr_bene_pmt_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
        except (KeyError, IndexError):
           item_dict['rev_cntr_bene_pmt_amt'] = 'Null'

        try:
           item_dict['rev_cntr_rate_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
        except (KeyError, IndexError):
           item_dict['rev_cntr_rate_amt'] = 'Null'

        try:
           item_dict['rev_cntr_tot_chrg_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
        except (KeyError, IndexError):
           item_dict['rev_cntr_tot_chrg_amt'] = 'Null'

        try:
           item_dict['rev_cntr_ncvrd_chrg_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
        except (KeyError, IndexError):
           item_dict['rev_cntr_ncvrd_chrg_amt'] = 'Null'

        try:
           item_dict['rev_cntr_pmt_amt_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
        except (KeyError, IndexError):
           item_dict['rev_cntr_pmt_amt_amt'] = 'Null'


        try:
           item_dict['Prvdr_State: Visit'] = data[row]['item'][0]['locationAddress']['state']
        except (KeyError, IndexError):
           item_dict['Prvdr_State: Visit'] = 'Null'

        try:
           item_dict['rev_cntr_cd'] = data[row]['item'][0]['revenue']['coding'][0]['code']
        except (KeyError, IndexError):
           item_dict['rev_cntr_cd'] = 'Null'

        try:
           item_dict['rev_cntr_display'] = data[row]['item'][0]['revenue']['coding'][0]['display']
        except (KeyError, IndexError):
           item_dict['rev_cntr_display'] = 'Null'

        try:
           item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
        except (KeyError, IndexError):
           item_dict['HCPCS'] = 'Null'

        try:
           item_dict['serviced_date'] = data[row]['item'][0]['servicedDate']
        except (KeyError, IndexError):
           item_dict['serviced_date'] = 'Null'


def item_Key6_Format (row, file, item_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        item_dict['Prvdr_State'] = data[row]['item'][0]['locationAddress']['state']
    except KeyError:
        item_dict['Prvdr_State'] = 'Null'
    except IndexError:
        item_dict['Prvdr_State'] = 'Null'

    try:
        item_dict['rev_cntr_rate_amt'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
    except KeyError:
        item_dict['rev_cntr_rate_amt'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_rate_amt'] = 'Null'

    try:
        item_dict['rev_cntr_total_chrg_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
    except KeyError:
        item_dict['rev_cntr_total_chrg_amt'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_total_chrg_amt'] = 'Null'

    try:
        item_dict['rev_cntr_ncvrd_chrg_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
    except KeyError:
        item_dict['rev_cntr_ncvrd_chrg_amt'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_ncvrd_chrg_amt'] = 'Null'

    try:
        item_dict['rev_cntr_pmt_amt_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
    except KeyError:
        item_dict['rev_cntr_pmt_amt_amt'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_pmt_amt_amt'] = 'Null'

    try:
        item_dict['rev_cntr'] = data[row]['item'][0]['revenue']['coding'][0]['code']
    except KeyError:
        item_dict['rev_cntr'] = 'Null'
    except IndexError:
        item_dict['rev_cntr'] = 'Null'

    try:
        item_dict['rev_cntr_display'] = data[row]['item'][0]['revenue']['coding'][0]['display']
    except KeyError:
        item_dict['rev_cntr_display'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_display'] = 'Null'

    try:
        item_dict['rev_cntr_stud_ind_cd'] = data[row]['item'][0]['revenue']['extension'][0]['valueCoding']['code']
    except KeyError:
        item_dict['rev_cntr_stud_ind_cd'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_stud_ind_cd'] = 'Null'

    try:
        item_dict['rev_cntr_stud_ind_display'] = data[row]['item'][0]['revenue']['extension'][0]['valueCoding']['display']
    except KeyError:
        item_dict['rev_cntr_stud_ind_display'] = 'Null'
    except IndexError:
        item_dict['rev_cntr_stud_ind_display'] = 'Null'

    try:
        item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
    except KeyError:
        item_dict['HCPCS'] = 'Null'
    except IndexError:
        item_dict['HCPCS'] = 'Null'

    try:
        item_dict['serviced_Date'] = data[row]['item'][0]['servicedDate']
    except KeyError:
        item_dict['serviced_Date'] = 'Null'
    except IndexError:
        item_dict['serviced_Date'] = 'Null'


def item_Key5_Format (row,file, item_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    try:
        item_dict['rev_cntr_blood_ddctbl_amt'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_blood_ddctbl_amt'] = 'Null'

    try:
        item_dict['rev_cntr_cash_ddctbl_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_cash_ddctbl_amt'] = 'Null'

    try:
        item_dict['rev_cntr_coinsrc_wge_adjstd_c'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_coinsrc_wge_adjstd_c'] = 'Null'

    try:
        item_dict['rev_cntr_rdcd_coinsrc_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_rdcd_coinsrc_amt'] = 'Null'

    try:
        item_dict['rev_cntr_1st_msp_pd_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_1st_msp_pd_amt'] = 'Null'

    try:
        item_dict['rev_cntr_2nd_msp_pd_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_2nd_msp_pd_amt'] = 'Null'

    try:
        item_dict['rev_cntr_prvdr_pmt_amt'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_prvdr_pmt_amt'] = 'Null'

    try:
        item_dict['rev_cntr_bene_pmt_amt'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_bene_pmt_amt'] = 'Null'

    try:
        item_dict['rev_cntr_ptnt_rspnsblty_pmt'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_ptnt_rspnsblty_pmt'] = 'Null'

    try:
        item_dict['rev_cntr_pmt_amt_amt'] = data[row]['item'][0]['adjudication'][9]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_pmt_amt_amt'] = 'Null'

    try:
        item_dict['rev_cntr_rate_amt'] = data[row]['item'][0]['adjudication'][10]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_rate_amt'] = 'Null'

    try:
        item_dict['rev_cntr_tot_chrg_amt'] = data[row]['item'][0]['adjudication'][11]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_tot_chrg_amt'] = 'Null'

    try:
        item_dict['rev_cntr_ncvrd_chrg_amt'] = data[row]['item'][0]['adjudication'][12]['amount']['value']
    except (KeyError, IndexError):
        item_dict['rev_cntr_ncvrd_chrg_amt'] = 'Null'

    try:
        item_dict['prvdr_State'] = data[row]['item'][0]['locationAddress']['state']
    except (KeyError, IndexError):
        item_dict['prvdr_State'] = 'Null'

    try:
        item_dict['rev_cntr'] = data[row]['item'][0]['revenue']['coding'][0]['code']
    except (KeyError, IndexError):
        item_dict['rev_cntr'] = 'Null'

    try:
        item_dict['rev_cntr_stus_ind_cd'] = data[row]['item'][0]['revenue']['extension'][0]['valueCoding']['code']
    except (KeyError, IndexError):
        item_dict['rev_cntr_stus_ind_cd'] = 'Null'

    try:
        item_dict['rev_cntr_stus_ind_display'] = data[row]['item'][0]['revenue']['coding'][0]['display']
    except (KeyError, IndexError):
        item_dict['rev_cntr_stus_ind_display'] = 'Null'

    try:
        item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
    except (KeyError, IndexError):
        item_dict['HCPCS'] = 'Null'


def item_Format (row, file, item_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    if len(data[row]['item']) == 3 or data[row]['item'][0]['adjudication'][0]['category']['coding'][0]['display'] == 'Carrier Line Reduced Payment Physician Assistant Code':
        try:
            item_dict['carr_line_rdcd_pmt_phys_astn_c'] = \
            data[row]['item'][0]['adjudication'][0]['reason']['coding'][0]['code']
            item_dict['line_nch_pmt_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
            item_dict['line_pmt_80_100_cd'] = data[row]['item'][0]['adjudication'][1]['extension'][0]['valueCoding'][
                'code']
            item_dict['line_bene_pmt_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            item_dict['line_prvdr_pmt_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            item_dict['line_bene_ptb_ddctbl_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
            item_dict['line_bene_prmry_pyr_pd_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
            item_dict['line_coinsrnc_amt'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            item_dict['line_sbmtd_chrg_amt'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            item_dict['line_alowd_chrg_amt'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            item_dict['line_prcsg_ind_cd'] = data[row]['item'][0]['adjudication'][9]['reason']['coding'][0]['code']
            item_dict['CareTeamLinkId'] = data[row]['item'][0]['careTeamLinkId']
            item_dict['DiagnosisLinkId'] = data[row]['item'][0]['diagnosisLinkId']
            item_dict['carr_line_mtus_cd'] = data[row]['item'][0]['extension'][0]['valueCoding']['code']
            item_dict['carr_line_mtus_cnt'] = data[row]['item'][0]['extension'][1]['valueQuantity']['value']
            item_dict['betos_cd'] = data[row]['item'][0]['extension'][2]['valueCoding']['code']
            try:
                item_dict['line_service-deductable'] = data[row]['item'][0]['extension'][3]['valueCoding']['display']
            except IndexError:
                item_dict['line_service-deductable'] = 'Null'
            item_dict['line_place_of_srvc_cd'] = data[row]['item'][0]['locationCodeableConcept']['coding'][0]['code']
            item_dict['Prvdr_State'] = data[row]['item'][0]['locationCodeableConcept']['extension'][0]['valueCoding'][
                'code']
            item_dict['Prvdr_Zip'] = data[row]['item'][0]['locationCodeableConcept']['extension'][1]['valueCoding'][
                'code']
            item_dict['Prvdr_City'] = data[row]['item'][0]['locationCodeableConcept']['extension'][2]['valueCoding'][
                'code']
            item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
            item_dict['ServicedPeriod_Start'] = data[row]['item'][0]['servicedPeriod']['start']
            item_dict['ServicedPeriod_End'] = data[row]['item'][0]['servicedPeriod']['end']
            item_dict['line_prmry_alowd_chrg_amt'] = 'Null'
            item_dict['line_dme_prchs_price_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cd'] = 'Null'
            item_dict['suplrnum'] = 'Null'
            item_dict['dmerc_line_scrn_svgs_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cnt'] = 'Null'
        except KeyError:
            print(
                f'The requested attribute for patient {row} has not been found, and will contain ''Null''. Double check the request.')
            item_dict['carr_line_rdcd_pmt_phys_astn_c'] = 'Null'
            item_dict['line_nch_pmt_amt'] = 'Null'
            item_dict['line_pmt_80_100_cd'] = 'Null'
            item_dict['line_bene_pmt_amt'] = 'Null'
            item_dict['line_prvdr_pmt_amt'] = 'Null'
            item_dict['line_bene_ptb_ddctbl_amt'] = 'Null'
            item_dict['line_bene_prmry_pyr_pd_amt'] = 'Null'
            item_dict['line_coinsrnc_amt'] = 'Null'
            item_dict['line_sbmtd_chrg_amt'] = 'Null'
            item_dict['line_alowd_chrg_amt'] = 'Null'
            item_dict['line_prcsg_ind_cd'] = 'Null'
            item_dict['CareTeamLinkId'] = 'Null'
            item_dict['DiagnosisLinkId'] = 'Null'
            item_dict['carr_line_mtus_cd'] = 'Null'
            item_dict['carr_line_mtus_cnt'] = 'Null'
            item_dict['betos_cd'] = 'Null'
            item_dict['line_service-deductable'] = 'Null'
            item_dict['line_place_of_srvc_cd'] = 'Null'
            item_dict['Prvdr_State'] = 'Null'
            item_dict['Prvdr_Zip'] = 'Null'
            item_dict['Prvdr_City'] = 'Null'
            item_dict['HCPCS'] = 'Null'
            item_dict['ServicedPeriod_Start'] = 'Null'
            item_dict['ServicedPeriod_End'] = 'Null'
            item_dict['line_prmry_alowd_chrg_amt'] = 'Null'
            item_dict['line_dme_prchs_price_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cd'] = 'Null'
            item_dict['suplrnum'] = 'Null'
            item_dict['dmerc_line_scrn_svgs_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cnt'] = 'Null'

    elif len(data[row]['item']) == 11 and len(data[row]['item'][0]['adjudication'][1]) == 3:
        try:
            item_dict['carr_line_rdcd_pmt_phys_astn_c'] = data[row]['item'][0]['adjudication'][0]['reason']['coding'][0]['code']
            item_dict['line_nch_pmt_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
            item_dict['line_pmt_80_100_cd'] = data[row]['item'][0]['adjudication'][1]['extension'][0]['valueCoding']['code']
            item_dict['line_bene_pmt_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            item_dict['line_prvdr_pmt_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            item_dict['line_bene_ptb_ddctbl_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
            item_dict['line_bene_prmry_pyr_pd_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
            item_dict['line_coinsrnc_amt'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            item_dict['line_sbmtd_chrg_amt'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            item_dict['line_alowd_chrg_amt'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            item_dict['line_prcsg_ind_cd'] = data[row]['item'][0]['adjudication'][9]['reason']['coding'][0]['code']
            item_dict['CareTeamLinkId'] = data[row]['item'][0]['careTeamLinkId']
            item_dict['DiagnosisLinkId'] = data[row]['item'][0]['diagnosisLinkId']
            item_dict['carr_line_mtus_cd'] = data[row]['item'][0]['extension'][0]['valueCoding']['code']
            item_dict['carr_line_mtus_cnt'] = data[row]['item'][0]['extension'][1]['valueQuantity']['value']
            item_dict['betos_cd'] = data[row]['item'][0]['extension'][2]['valueCoding']['code']
            try:
                item_dict['line_service-deductable'] = data[row]['item'][0]['extension'][3]['valueCoding']['display']
            except IndexError:
                item_dict['line_service-deductable'] = 'Null'
            item_dict['line_place_of_srvc_cd'] = data[row]['item'][0]['locationCodeableConcept']['coding'][0]['code']
            item_dict['Prvdr_State'] = data[row]['item'][0]['locationCodeableConcept']['extension'][0]['valueCoding'][
                'code']
            item_dict['Prvdr_Zip'] = data[row]['item'][0]['locationCodeableConcept']['extension'][1]['valueCoding'][
                'code']
            item_dict['Prvdr_City'] = data[row]['item'][0]['locationCodeableConcept']['extension'][2]['valueCoding'][
                'code']
            item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
            item_dict['ServicedPeriod_Start'] = data[row]['item'][0]['servicedPeriod']['start']
            item_dict['ServicedPeriod_End'] = data[row]['item'][0]['servicedPeriod']['end']
            item_dict['line_prmry_alowd_chrg_amt'] = 'Null'
            item_dict['line_dme_prchs_price_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cd'] = 'Null'
            item_dict['suplrnum'] = 'Null'
            item_dict['dmerc_line_scrn_svgs_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cnt'] = 'Null'
        except KeyError:
            print(
                f'The requested attribute for patient {row} has not been found, and will contain ''Null''. Double check the request.')
            item_dict['carr_line_rdcd_pmt_phys_astn_c'] = 'Null'
            item_dict['line_nch_pmt_amt'] = 'Null'
            item_dict['line_pmt_80_100_cd'] = 'Null'
            item_dict['line_bene_pmt_amt'] = 'Null'
            item_dict['line_prvdr_pmt_amt'] = 'Null'
            item_dict['line_bene_ptb_ddctbl_amt'] = 'Null'
            item_dict['line_bene_prmry_pyr_pd_amt'] = 'Null'
            item_dict['line_coinsrnc_amt'] = 'Null'
            item_dict['line_sbmtd_chrg_amt'] = 'Null'
            item_dict['line_alowd_chrg_amt'] = 'Null'
            item_dict['line_prcsg_ind_cd'] = 'Null'
            item_dict['CareTeamLinkId'] = 'Null'
            item_dict['DiagnosisLinkId'] = 'Null'
            item_dict['carr_line_mtus_cd'] = 'Null'
            item_dict['carr_line_mtus_cnt'] = 'Null'
            item_dict['betos_cd'] = 'Null'
            item_dict['line_service_deductable'] = 'Null'
            item_dict['line_place_of_srvc_cd'] = 'Null'
            item_dict['Prvdr_State'] = 'Null'
            item_dict['Prvdr_Zip'] = 'Null'
            item_dict['Prvdr_City'] = 'Null'
            item_dict['HCPCS'] = 'Null'
            item_dict['ServicedPeriod_Start'] = 'Null'
            item_dict['ServicedPeriod_End'] = 'Null'
            item_dict['line_prmry_alowd_chrg_amt'] = 'Null'
            item_dict['line_dme_prchs_price_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cd'] = 'Null'
            item_dict['suplrnum'] = 'Null'
            item_dict['dmerc_line_scrn_svgs_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cnt'] = 'Null'
    else:
        try:
            item_dict['carr_line_rdcd_pmt_phys_astn_c'] = 'Null'
            item_dict['line_nch_pmt_amt'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            item_dict['line_pmt_80_100_cd'] = data[row]['item'][0]['adjudication'][2]['extension'][0]['valueCoding'][
                'code']
            item_dict['line_bene_pmt_amt'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            item_dict['line_prvdr_pmt_amt'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
            item_dict['line_bene_ptb_ddctbl_amt'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
            item_dict['line_bene_prmry_pyr_pd_amt'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            item_dict['line_coinsrnc_amt'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            item_dict['line_sbmtd_chrg_amt'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            try:
                item_dict['line_alowd_chrg_amt'] = data[row]['item'][0]['adjudication'][9]['amount']['value ']
            except KeyError:
                item_dict['line_alowd_chrg_amt'] = 'Null'
            item_dict['line_prcsg_ind_cd'] = data[row]['item'][0]['adjudication'][10]['reason']['coding'][0]['code']
            item_dict['CareTeamLinkId'] = data[row]['item'][0]['careTeamLinkId']
            item_dict['DiagnosisLinkId'] = data[row]['item'][0]['diagnosisLinkId']
            item_dict['carr_line_mtus_cd'] = 'Null'
            item_dict['carr_line_mtus_cnt'] = 'Null'
            item_dict['betos_cd'] = data[row]['item'][0]['extension'][3]['valueCoding']['code']

            try:
                item_dict['line_service-deductable'] = data[row]['item'][0]['extension'][3]['valueCoding']['display']
            except IndexError:
                item_dict['line_service-deductable'] = 'Null'

            item_dict['line_place_of_srvc_cd'] = data[row]['item'][0]['locationCodeableConcept']['coding'][0]['code']
            item_dict['Prvdr_State'] = data[row]['item'][0]['locationCodeableConcept']['extension'][0]['valueCoding'][
                'code']
            item_dict['Prvdr_Zip'] = data[row]['item'][0]['locationCodeableConcept']['extension'][1]['valueCoding'][
                'code']
            item_dict['Prvdr_City'] = data[row]['item'][0]['locationCodeableConcept']['extension'][2]['valueCoding'][
                'code']
            item_dict['HCPCS'] = data[row]['item'][0]['service']['coding'][0]['code']
            item_dict['ServicedPeriod_Start'] = data[row]['item'][0]['servicedPeriod']['start']
            item_dict['ServicedPeriod_End'] = data[row]['item'][0]['servicedPeriod']['end']
            item_dict['line_prmry_alowd_chrg_amt'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
            item_dict['line_dme_prchs_price_amt'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
            item_dict['dmerc_line_mtus_cd'] = data[row]['item'][0]['extension'][2]['valueQuantity']['code']
            item_dict['suplrnum'] = data[row]['item'][0]['extension'][0]['valueIdentifier']['value']
            item_dict['dmerc_line_scrn_svgs_amt'] = data[row]['item'][0]['extension'][1]['valueQuantity']['value']
            item_dict['dmerc_line_mtus_cnt'] = data[row]['item'][0]['extension'][2]['valueQuantity']['value']
        except KeyError:
            print(
                f'The requested attribute for patient {row} has not been found, and will contain ''Null''. Double check the request.')
            item_dict['carr_line_rdcd_pmt_phys_astn_c'] = 'Null'
            item_dict['line_nch_pmt_amt'] = 'Null'
            item_dict['line_pmt_80_100_cd'] = 'Null'
            item_dict['line_bene_pmt_amt'] = 'Null'
            item_dict['line_prvdr_pmt_amt'] = 'Null'
            item_dict['line_bene_ptb_ddctbl_amt'] = 'Null'
            item_dict['line_bene_prmry_pyr_pd_amt'] = 'Null'
            item_dict['line_coinsrnc_amt'] = 'Null'
            item_dict['line_sbmtd_chrg_amt'] = 'Null'
            item_dict['line_alowd_chrg_amt'] = 'Null'
            item_dict['line_prcsg_ind_cd'] = 'Null'
            item_dict['CareTeamLinkId'] = 'Null'
            item_dict['DiagnosisLinkId'] = 'Null'
            item_dict['carr_line_mtus_cd'] = 'Null'
            item_dict['carr_line_mtus_cnt'] = 'Null'
            item_dict['betos_cd'] = 'Null'
            item_dict['line_service_deductable'] = 'Null'
            item_dict['line_place_of_srvc_cd'] = 'Null'
            item_dict['Prvdr_State'] = 'Null'
            item_dict['Prvdr_Zip'] = 'Null'
            item_dict['Prvdr_City'] = 'Null'
            item_dict['HCPCS'] = 'Null'
            item_dict['ServicedPeriod_Start'] = 'Null'
            item_dict['ServicedPeriod_End'] = 'Null'
            item_dict['line_prmry_alowd_chrg_amt'] = 'Null'
            item_dict['line_dme_prchs_price_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cd'] = 'Null'
            item_dict['suplrnum'] = 'Null'
            item_dict['dmerc_line_scrn_svgs_amt'] = 'Null'
            item_dict['dmerc_line_mtus_cnt'] = 'Null'


def careTeam_Inpatient_Format (row, file, careTeam_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        careTeam_dict["Assissting_Provider_NPI"] = data[row]['careTeam'][0]['provider']['identifier']['value']
        careTeam_dict["Primary_Provider_NPI"] = data[row]['careTeam'][1]['provider']['identifier']['value']

    except KeyError:
        careTeam_dict["Assissting_Provider_NPI"] = 'Null'
        careTeam_dict["Primary_Provider_NPI"] = 'Null'


def careTeam_Key5_Format (row, file, careTeam_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    npi_cnt = len(data[row]['careTeam'])

    if npi_cnt == 1:
        try:
            careTeam_dict['Primary Provider NPI'] = data[row]['careTeam'][0]['provider']['identifier']['value']
        except KeyError:
            careTeam_dict['Primary Provider NPI'] = 'Null'
        careTeam_dict['Assisting Provider NPI'] = 'Null'
        careTeam_dict['Other Provider NPI'] = 'Null'

    elif npi_cnt == 2:
        try:
            careTeam_dict['Primary Provider NPI'] = data[row]['careTeam'][1]['provider']['identifier']['value']
            careTeam_dict['Assisting Provider NPI'] = data[row]['careTeam'][0]['provider']['identifier']['value']
        except (KeyError,IndexError):
            careTeam_dict['Primary Provider NPI'] = 'Null'
            careTeam_dict['Assisting Provider NPI'] = 'Null'
        careTeam_dict['Other Provider NPI'] = 'Null'

    else:
        try:
            careTeam_dict['Primary Provider NPI'] = data[row]['careTeam'][2]['provider']['identifier']['value']
            careTeam_dict['Assisting Provider NPI'] = data[row]['careTeam'][0]['provider']['identifier']['value']
            careTeam_dict['Other Provider NPI'] = data[row]['careTeam'][1]['provider']['identifier']['value']
        except (KeyError,IndexError):
            careTeam_dict['Primary Provider NPI'] = 'Null'
            careTeam_dict['Assisting Provider NPI'] = 'Null'
            careTeam_dict['Other Provider NPI'] = 'Null'


def careTeam_Format (row, file, careTeam_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        careTeam_dict["carr_line_prvdr_type"] = data[row]['careTeam'][0]['extension'][0]['valueCoding']['code']
    except KeyError:
        print(f'Care Team attribute for patient {row} has not been found. Check for Index or Key Errors')
        careTeam_dict["carr_line_prvdr_type"] = 'Null'

    try:
        careTeam_dict['Prtcptng_Ind_Cd'] = data[row]['careTeam'][0]['extension'][3]['valueCoding']['code']
    except (KeyError, IndexError):
        try:
            careTeam_dict['Prtcptng_Ind_Cd'] = data[row]['careTeam'][0]['extension'][1]['valueCoding']['code']
        except (KeyError, IndexError):
            careTeam_dict['Prtcptng_Ind_Cd'] = 'Null'
            print(f'Care Team attribute for patient {row} has not been found. Check for Index or Key Errors')

    try:
        careTeam_dict['PCP_NPI'] = data[row]['careTeam'][0]['provider']['identifier']['value']
    except (KeyError, IndexError):
        careTeam_dict['PCP_NPI'] = 'Null'

    try:
        careTeam_dict["Prvdr_Spclty"] = data[row]['careTeam'][0]['qualification']['coding'][0]['display']
    except KeyError:
        try:
            careTeam_dict["Prvdr_Spclty"] = data[row]['careTeam'][0]['qualification']['coding'][0]['code']
        except KeyError:
            careTeam_dict["Prvdr_Spclty"] = 'Null'

    try:
        careTeam_dict["Responsible"] = data[row]['careTeam'][0]['responsible']
    except (KeyError, IndexError):
        print(f'Care Team attribute for patient {row} has not been found. Check for Index or Key Errors')
        careTeam_dict['Responsible'] = 'Null'

    try:
        careTeam_dict['Role'] = data[row]['careTeam'][0]['role']['coding'][0]['display']
    except (KeyError, IndexError):
        print(f'Care Team attribute for patient {row} has not been found. Check for Index or Key Errors')
        careTeam_dict['Role'] = 'Null'

    try:
        careTeam_dict['Sequence'] = data[row]['careTeam'][0]['sequence']
    except (KeyError, IndexError):
        print(f'Care Team attribute for patient {row} has not been found. Check for Index or Key Errors')
        careTeam_dict['Sequence'] = 'Null'


def referral_Format (row, file, referral_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        referral_dict['Referral_Cd'] = data[row]['referral']['reference']
    except KeyError:
        print(f'Key Error for Referral attribute for patient {row}')
        referral_dict['Referral_Cd'] = 'Null'


def diag_Format (row, file, diagnosis_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    try:
        diaC = len(data[row]['diagnosis'])
        for dgns in range(0, diaC):
            if dgns == 0:
                diagnosis_dict['DGNS_CD_Principal'] = \
                    data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0][
                        'code']
            elif 1 <= dgns < 20:
                diagnosis_dict[f'DGNS_CD_{dgns}'] = data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0][
                    'code']
            else:
                print('Only taking the past 20 diagnoses')
        if diaC < 20:
            delta = 20 - diaC
            for dgns in range(0, delta):
                elem = diaC + dgns
                diagnosis_dict[f'DGNS_CD_{elem}'] = 'Null'

    except KeyError:
        print(f'No diagnosis for patient {row}')
        diagnosis_dict['DGNS_CD_Principal'] = 'Null'
        for dgns in range(1, 20):
            diagnosis_dict[f'DNGS_CD_{dgns+1}'] = 'Null'


def diag_Hospice_Format (row, file, diagnosis_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    noVar = False

    try:
        diagnosis_dict['clm_drg_cd'] = data[row]['diagnosis'][0]['packageCode']['coding'][0]['code']
    except(KeyError,IndexError):
        diagnosis_dict['clm_drg_cd'] = 'Null'
        noVar = True

    if not noVar:
        try:
            diaC = len(data[row]['diagnosis'])
            for dgns in range(1, diaC):
                if dgns == 1:
                    diagnosis_dict['DGNS_CD_Admitting'] = \
                        data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0]['code']
                elif dgns == 2:
                    diagnosis_dict['DGNS_CD_Principal'] = \
                        data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0]['code']
                elif 3 <= dgns < 20:
                    diagnosis_dict[f'DGNS_CD_{dgns}'] = \
                        data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0]['code']
                else:
                    print('Only taking the past 20 diagnoses')
            if diaC < 20:
                delta = 20 - diaC
                for dgns in range(0, delta):
                    elem = diaC + dgns
                    diagnosis_dict[f'DGNS_CD_{elem}'] = 'Null'

        except (KeyError,IndexError):
            print(f'No diagnosis for patient {row}')
            diagnosis_dict['DGNS_CD_Principal'] = 'Null'
            for dgns in range(1, 20):
                diagnosis_dict[f'DNGS_CD_{dgns+1}'] = 'Null'
    else:
        try:
            diaC = len(data[row]['diagnosis'])
            for dgns in range(0, diaC):
                if dgns == 0:
                    diagnosis_dict['DGNS_CD_Admitting'] = \
                        data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0]['code']

                    logging.info(diagnosis_dict['DGNS_CD_Admitting'])

                elif dgns == 1:
                    diagnosis_dict['DGNS_CD_Principal'] = \
                        data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0]['code']

                    logging.info(diagnosis_dict['DGNS_CD_Principal'])

                elif 2 <= dgns < 19:
                    diagnosis_dict[f'DGNS_CD_{dgns}'] = \
                        data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0]['code']

                    logging.info(diagnosis_dict[f'DGNS_CD_{dgns}'])

            if diaC < 20:
                delta = 20 - diaC
                for dgns in range(1, delta):
                    elem = diaC + dgns
                    diagnosis_dict[f'DGNS_CD_{elem}'] = 'Null'
                    logging.info(f'{diaC}, {elem}')

        except (KeyError, IndexError):
            print(f'No diagnosis for patient {row}')
            diagnosis_dict['DGNS_CD_Admitting'] = 'Null'
            diagnosis_dict['DGNS_CD_Principal'] = 'Null'
            for dgns in range(1, 19):
                diagnosis_dict[f'DNGS_CD_{dgns + 1}'] = 'Null'


def diag_Key6_Format (row, file, diagnosis_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    try:
        diaC = len(data[row]['diagnosis'])
        for dgns in range(0, diaC):
            if dgns == 0:
                diagnosis_dict['DGNS_CD_Principal'] = \
                    data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0][
                        'code']
            elif 1 <= dgns < 25:
                diagnosis_dict[f'DGNS_CD_{dgns}'] = data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0][
                    'code']
            else:
                print('Only taking the past 25 diagnoses')
        if diaC < 25:
            delta = 25 - diaC
            for dgns in range(0, delta):
                elem = diaC + dgns
                diagnosis_dict[f'DGNS_CD_{elem}'] = 'Null'

    except KeyError:
        print(f'No diagnosis for patient {row}')
        diagnosis_dict['DGNS_CD_Principal'] = 'Null'
        for dgns in range(1, 20):
            diagnosis_dict[f'DNGS_CD_{dgns+1}'] = 'Null'


def diag_Inpatient_Format (row, file, diagnosis_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    try:
        diaC = len(data[row]['diagnosis'])
        for dgns in range(1, diaC):
            if dgns == 1:
                diagnosis_dict['DGNS_CD_Principal'] = \
                    data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0][
                        'code']
            elif 2 <= dgns < 31:
                diagnosis_dict[f'DGNS_CD_{dgns-1}'] = data[row]['diagnosis'][dgns]['diagnosisCodeableConcept']['coding'][0][
                    'code']
            else:
                print('Only taking the past 30 diagnoses')
        if diaC < 31:
            delta = 31 - diaC
            for dgns in range(0, delta):
                elem = diaC + dgns
                diagnosis_dict[f'DGNS_CD_{elem-1}'] = 'Null'

    except KeyError:
        print(f'No diagnosis for patient {row}')
        diagnosis_dict['DGNS_CD_Principal'] = 'Null'
        for dgns in range(1, 30):
            diagnosis_dict[f'DNGS_CD_{dgns+1}'] = 'Null'


def extension_Key1_Key2_Format (row, file, extension_dict,):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    ext = -1
    n = 0

    for x in data[row]['extension']:
        ext += 1

    while n <= ext:
        if n == 0:
            try:
                extension_dict['PrPayAmt'] = data[row]['extension'][n]['valueMoney']['value']
            except(KeyError, IndexError):
                extension_dict['PrPayAmt'] = 'Null'
            n += 1

        elif n == 1:
            try:
                extension_dict['Carr_Num'] = data[row]['extension'][n]['valueIdentifier']['value']
            except(KeyError, IndexError):
                extension_dict['Carr_Num'] = 'Null'
            n += 1

        elif n == 2:
            try:
                extension_dict['Carr_Clm_Cntl_Num'] = data[row]['extension'][n]['valueIdentifier']['value']
            except(KeyError, IndexError):
                extension_dict['Carr_Clm_Cntl_Num'] = 'Null'
            n += 1

        elif n == 3:
            try:
                extension_dict['Carr_Clm_Pmt_DNL_cd'] = data[row]['extension'][n]['valueCoding']['code']
            except(KeyError,IndexError):
                extension_dict['Carr_Clm_Pmt_DNL_cd'] = 'Null'
            n += 1
        elif n == 4:
            try:
                extension_dict['Assignment_Code'] = data[row]['extension'][n]['valueCoding']['code']
            except(KeyError, IndexError):
                extension_dict['Assignment_Code'] = 'Null'
            n += 1
        elif n == 5:
            try:
                extension_dict['Clm_Clncl_Tril_Num'] = data[row]['extension'][n]['valueIdentifier']['value']
            except (KeyError, IndexError):
                extension_dict['Clm_Clncl_Tril_Num'] = 'Null'
            n += 1
        elif n == 6:
            try:
                extension_dict['Carr_Clm_Cash_Ddctbl_Apld_Amt'] = data[row]['extension'][n]['valueMoney']['value']
            except (KeyError, IndexError):
                extension_dict['Carr_Clm_Cash_Ddctbl_Apld_Amt'] = 'Null'
            n += 1
        elif n == 7:
            try:
                extension_dict['Nch_Clm_Prvdr_Pmt_Amt'] = data[row]['extension'][n]['valueMoney']['value']
            except (KeyError, IndexError):
                extension_dict['Nch_Clm_Prvdr_Pmt_Amt'] = 'Null'
            n += 1
        elif n == 8:
            try:
                extension_dict['Nch_Clm_Bene_Pmt_Amt'] = data[row]['extension'][n]['valueMoney']['value']
            except (KeyError, IndexError):
                extension_dict['Nch_Clm_Bene_Pmt_Amt'] = 'Null'
            n += 1
        elif n == 9:
            try:
                extension_dict['Nch_Carr_Clm_Sbmtd_Chrg_Amt'] = data[row]['extension'][n]['valueMoney']['value']
            except (KeyError, IndexError):
                extension_dict['Nch_Carr_Clm_Sbmtd_Chrg_Amt'] = 'Null'
            n += 1
        elif n == 10:
            try:
                extension_dict['Nch_Carr_Clm_Alowd_Amt'] = data[row]['extension'][n]['valueMoney']['value']
            except (KeyError, IndexError):
                extension_dict['Nch_Carr_Clm_Alowd_Amt'] = 'Null'
            n += 1
        else:
            print(f'n = {n}')
            break


def extension_Hospice_Format(row, file, extension_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    j = 0


    if len(data[row]['extension']) == 20:
        try:
            extension_dict['clm_pass_thru_per_diem_amt'] = data[row]['extension'][0]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pass_thru_per_diem_amt'] = 'Null'
        try:
            extension_dict['nch_profnl_cmpnt_chrg_amt'] = data[row]['extension'][1]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_profnl_cmpnt_chrg_amt'] = 'Null'
        try:
            extension_dict['clm_tot_pps_cptl_amt'] = data[row]['extension'][2]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_tot_pps_cptl_amt'] = 'Null'
        try:
            extension_dict['clm_uncompd_care_pmt_amt'] = data[row]['extension'][3]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_uncompd_care_pmt_amt'] = 'Null'
        try:
            extension_dict['nch_bene_ip_ddctbl_amt'] = data[row]['extension'][4]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_ip_ddctbl_amt'] = 'Null'
        try:
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = data[row]['extension'][5]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = 'Null'
        try:
            extension_dict['nch_ip_ncvrd_chrg_amt'] = data[row]['extension'][6]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_ncvrd_chrg_amt'] = 'Null'
        try:
            extension_dict['nch_ip_tot_ddctn_amt'] = data[row]['extension'][7]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_tot_ddctn_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = data[row]['extension'][8]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_excptn_amt'] = data[row]['extension'][9]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_excptn_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_fsp_amt'] = data[row]['extension'][10]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_fsp_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_ime_amt'] = data[row]['extension'][11]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_ime_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_outlier_amt'] = data[row]['extension'][12]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_outlier_amt'] = 'Null'
        try:
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = data[row]['extension'][13]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = 'Null'
        try:
            extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = data[row]['extension'][14]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = 'Null'
        try:
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = data[row]['extension'][15]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = 'Null'
        try:
            extension_dict['clm_mdcr_non_pmt_rsn_cd'] = data[row]['extension'][16]['valueCoding']['code']
        except (KeyError, IndexError):
            extension_dict['clm_mdcr_non_pmt_rsn_cd'] = 'Null'
        try:
            extension_dict['clm_mdcr_non_pmt_rsn_display'] = data[row]['extension'][16]['valueCoding']['display']
        except (KeyError, IndexError):
            extension_dict['clm_mdcr_non_pmt_rsn_display'] = 'Null'
        try:
            extension_dict['prpayamt'] = data[row]['extension'][17]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['prpayamt'] = 'Null'
        try:
            extension_dict['fi_num'] = data[row]['extension'][18]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_num'] = 'Null'
        try:
            extension_dict['fi_doc_clm_cntl_num'] = data[row]['extension'][19]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_doc_clm_cntl_num'] = 'Null'
        try:
            extension_dict['fi_orig_clm_cntl_num'] = data[row]['extension'][20]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_orig_clm_cntl_num'] = 'Null'

    elif len(data[row]['extension']) == 14:
        extension_dict['clm_pass_thru_per_diem_amt'] = 'Null'
        extension_dict['nch_profnl_cmpnt_chrg_amt'] = 'Null'
        extension_dict['clm_tot_pps_cptl_amt'] = 'Null'
        extension_dict['clm_uncompd_care_pmt_amt'] = 'Null'

        try:
            extension_dict['nch_bene_ip_ddctbl_amt'] = data[row]['extension'][0]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_ip_ddctbl_amt'] = 'Null'

        try:
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = data[row]['extension'][1]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = 'Null'

        try:
            extension_dict['nch_ip_ncvrd_chrg_amt'] = data[row]['extension'][2]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_ncvrd_chrg_amt'] = 'Null'

        try:
            extension_dict['nch_ip_tot_ddctn_amt'] = data[row]['extension'][3]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_tot_ddctn_amt'] = 'Null'

        try:
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = data[row]['extension'][4]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = 'Null'

        try:
            extension_dict['clm_pps_cptl_excptn_amt'] = data[row]['extension'][5]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_excptn_amt'] = 'Null'

        try:
            extension_dict['clm_pps_cptl_fsp_amt'] = data[row]['extension'][6]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_fsp_amt'] = 'Null'

        try:
            extension_dict['clm_pps_cptl_ime_amt'] = data[row]['extension'][7]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_ime_amt'] = 'Null'

        try:
            extension_dict['clm_pps_cptl_outlier_amt'] = data[row]['extension'][8]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_outlier_amt'] = 'Null'

        try:
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = data[row]['extension'][9]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = 'Null'

        extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = 'Null'

        try:
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = data[row]['extension'][10]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = 'Null'

        extension_dict['clm_mdcr_non_pmt_rsn_cd'] = 'Null'
        extension_dict['clm_mdcr_non_pmt_rsn_display'] = 'Null'

        try:
            extension_dict['prpayamt'] = data[row]['extension'][11]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['prpayamt'] = 'Null'

        try:
            extension_dict['fi_num'] = data[row]['extension'][12]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_num'] = 'Null'
        try:
            extension_dict['fi_doc_clm_cntl_num'] = data[row]['extension'][13]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_doc_clm_cntl_num'] = 'Null'
        extension_dict['fi_orig_clm_cntl_num'] = 'Null'

    else:
        extension_dict['clm_pass_thru_per_diem_amt'] = 'Null'
        extension_dict['nch_profnl_cmpnt_chrg_amt'] = 'Null'
        extension_dict['clm_tot_pps_cptl_amt'] = 'Null'
        extension_dict['clm_uncompd_care_pmt_amt'] = 'Null'
        extension_dict['nch_bene_ip_ddctbl_amt'] = 'Null'
        extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = 'Null'
        extension_dict['nch_ip_ncvrd_chrg_amt'] = 'Null'
        extension_dict['nch_ip_tot_ddctn_amt'] = 'Null'
        extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = 'Null'
        extension_dict['clm_pps_cptl_excptn_amt'] = 'Null'
        extension_dict['clm_pps_cptl_fsp_amt'] = 'Null'
        extension_dict['clm_pps_cptl_ime_amt'] = 'Null'
        extension_dict['clm_pps_cptl_outlier_amt'] = 'Null'
        extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = 'Null'
        extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = 'Null'
        extension_dict['nch_bene_blood_ddctbl_lblty_am'] = 'Null'
        extension_dict['clm_mdcr_non_pmt_rsn_cd'] = 'Null'
        extension_dict['clm_mdcr_non_pmt_rsn_display'] = 'Null'

        try:
            extension_dict['prpayamt'] = data[row]['extension'][0]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['prpayamt'] = 'Null'

        try:
            extension_dict['fi_num'] = data[row]['extension'][1]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_num'] = 'Null'
        try:
            extension_dict['fi_doc_clm_cntl_num'] = data[row]['extension'][2]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['fi_doc_clm_cntl_num'] = 'Null'

        extension_dict['fi_orig_clm_cntl_num'] = 'Null'


def extension_Key5_Format (row, file, extension_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    try:
        extension_dict['nch_profnl_cmpnt_chrg_amt'] = data[row]['extension'][0]['valueMoney']['value']
    except KeyError:
        extension_dict['nch_profnl_cmpnt_chrg_amt'] = 'Null'
    try:
        extension_dict['nch_bene_ptb_ddctbl_amt'] = data[row]['extension'][1]['valueMoney']['value']
    except KeyError:
        extension_dict['nch_bene_ptb_ddctbl_amt'] = 'Null'
    try:
        extension_dict['nch_bene_ptb_coinsrnc_amt'] = data[row]['extension'][2]['valueMoney']['value']
    except KeyError:
        extension_dict['nch_bene_ptb_coinsrnc_amt'] = 'Null'
    try:
        extension_dict['clm_op_prvdr_pmt_amt'] = data[row]['extension'][3]['valueMoney']['value']
    except KeyError:
        extension_dict['clm_op_prvdr_pmt_amt'] = 'Null'
    try:
        extension_dict['clm_op_bene_pmt_amt'] = data[row]['extension'][4]['valueMoney']['value']
    except KeyError:
        extension_dict['clm_op_bene_pmt_amt'] = 'Null'
    try:
        extension_dict['nch_bene_blood_ddctbl_lblty_am'] = data[row]['extension'][5]['valueMoney']['value']
    except KeyError:
        extension_dict['nch_bene_blood_ddctbl_lblty_am'] = 'Null'
    try:
        extension_dict['prpayment'] = data[row]['extension'][6]['valueMoney']['value']
    except KeyError:
        extension_dict['prpayment'] = 'Null'
    try:
        extension_dict['fi_num'] = data[row]['extension'][7]['valueIdentifier']['value']
    except KeyError:
        extension_dict['fi_num'] = 'Null'


def extension_Inpatient_Format (row, file, extension_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    if len(data[row]['extension']) == 20:

        extension_dict['ime_op_clm_val_amt'] = 'Null'

        try:
            extension_dict['dsh_op_clm_val_amt'] = data[row]['extension'][0]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['dsh_op_clm_val_amt'] = 'Null'
        try:
            extension_dict['clm_pass_thru_per_diem_amt'] = data[row]['extension'][1]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pass_thru_per_diem_amt'] = 'Null'
        try:
            extension_dict['nch_profnl_cmpnt_chrg_amt'] = data[row]['extension'][2]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_profnl_cmpnt_chrg_amt'] = 'Null'
        try:
            extension_dict['clm_tot_pps_cptl_amt'] = data[row]['extension'][3]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_tot_pps_cptl_amt'] = 'Null'

        try:
            extension_dict['Claim Uncompensated Care Payment Amount'] = data[row]['extension'][4]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['Claim Uncompensated Care Payment Amount'] = 'Null'

        try:
            extension_dict['nch_bene_ip_ddctbl_amt'] = data[row]['extension'][5]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_ip_ddctbl_amt'] = 'Null'
        try:
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = data[row]['extension'][6]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = 'Null'
        try:
            extension_dict['nch_ip_ncvrd_chrg_amt'] = data[row]['extension'][7]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_ncvrd_chrg_amt'] = 'Null'
        try:
            extension_dict['nch_ip_tot_ddctn_amt'] = data[row]['extension'][8]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_tot_ddctn_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = data[row]['extension'][9]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_excptn_amt'] = data[row]['extension'][10]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_excptn_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_fsp_amt'] = data[row]['extension'][11]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_fsp_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_ime_amt'] = data[row]['extension'][12]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_ime_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_outlier_amt'] = data[row]['extension'][13]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_outlier_amt'] = 'Null'
        try:
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = data[row]['extension'][14]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = 'Null'
        try:
            extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = data[row]['extension'][15]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = 'Null'
        try:
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = data[row]['extension'][16]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = 'Null'
        try:
            extension_dict['NCH Primary Payer (if not Medicare) Claim Paid Amount'] = data[row]['extension'][17]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['NCH Primary Payer (if not Medicare) Claim Paid Amount'] = 'Null'
        try:
            extension_dict['Fiscal Intermediary or MAC Number'] = data[row]['extension'][18]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['Fiscal Intermediary or MAC Number'] = 'Null'
        try:
            extension_dict['Fiscal Intermediary Claim CNTL Number'] = data[row]['extension'][19]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['Fiscal Intermediary Claim CNTL Number'] = 'Null'

    elif len(data[row]['extension']) == 22:
        try:
            extension_dict['ime_op_clm_val_amt'] = data[row]['extension'][0]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['ime_op_clm_val_amt'] = 'Null'
        try:
            extension_dict['dsh_op_clm_val_amt'] = data[row]['extension'][1]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['dsh_op_clm_val_amt'] = 'Null'
        try:
            extension_dict['clm_pass_thru_per_diem_amt'] = data[row]['extension'][2]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pass_thru_per_diem_amt'] = 'Null'
        try:
            extension_dict['nch_profnl_cmpnt_chrg_amt'] = data[row]['extension'][3]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_profnl_cmpnt_chrg_amt'] = 'Null'
        try:
            extension_dict['clm_tot_pps_cptl_amt'] = data[row]['extension'][4]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_tot_pps_cptl_amt'] = 'Null'

        try:
            extension_dict['Claim Uncompensated Care Payment Amount'] = data[row]['extension'][6]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['Claim Uncompensated Care Payment Amount'] = 'Null'

        try:
            extension_dict['nch_bene_ip_ddctbl_amt'] = data[row]['extension'][7]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_ip_ddctbl_amt'] = 'Null'
        try:
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = data[row]['extension'][8]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_pta_coinsrnc_lblty_amt'] = 'Null'
        try:
            extension_dict['nch_ip_ncvrd_chrg_amt'] = data[row]['extension'][9]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_ncvrd_chrg_amt'] = 'Null'
        try:
            extension_dict['nch_ip_tot_ddctn_amt'] = data[row]['extension'][10]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_ip_tot_ddctn_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = data[row]['extension'][11]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_dsprprtnt_shr_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_excptn_amt'] = data[row]['extension'][12]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_excptn_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_fsp_amt'] = data[row]['extension'][13]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_fsp_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_ime_amt'] = data[row]['extension'][14]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_ime_amt'] = 'Null'
        try:
            extension_dict['clm_pps_cptl_outlier_amt'] = data[row]['extension'][15]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_cptl_outlier_amt'] = 'Null'
        try:
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = data[row]['extension'][16]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['clm_pps_old_cptl_hld_hrmls_amt'] = 'Null'
        try:
            extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = data[row]['extension'][17]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_drg_outlier_aprvd_pmt_amt'] = 'Null'
        try:
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = data[row]['extension'][18]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['nch_bene_blood_ddctbl_lblty_am'] = 'Null'
        try:
            extension_dict['NCH Primary Payer (if not Medicare) Claim Paid Amount'] = \
                data[row]['extension'][19]['valueMoney']['value']
        except (KeyError, IndexError):
            extension_dict['NCH Primary Payer (if not Medicare) Claim Paid Amount'] = 'Null'
        try:
            extension_dict['Fiscal Intermediary or MAC Number'] = data[row]['extension'][20]['valueIdentifier']['value']
        except (KeyError, IndexError):
            extension_dict['Fiscal Intermediary or MAC Number'] = 'Null'
        try:
            extension_dict['Fiscal Intermediary Claim CNTL Number'] = data[row]['extension'][21]['valueIdentifier'][
                'value']
        except (KeyError, IndexError):
            extension_dict['Fiscal Intermediary Claim CNTL Number'] = 'Null'

    else:
        print('Length of Extension Dictionary Record larger/smaller than expected!\nInspect the JSON File!')
        sys.exit()


def extension_HHA_Format (row, file, extension_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    if data[row]['extension'][0]['url'] == 'https://bluebutton.cms.gov/resources/variables/prpayamt':
        # If condition is true, pr_payment is the first attribute in 'extension' key
        try:
            extension_dict['pr_payment'] = data[row]['extension'][0]['valueMoney']['value']
        except(KeyError, IndexError):
            extension_dict['pr_payment'] = 'Null'

        try:
            extension_dict['fi_num'] = data[row]['extension'][1]['valueIdentifier']['value']
        except(KeyError, IndexError):
            extension_dict['fi_num'] = 'Null'
    else:
        try:
            extension_dict['pr_payment'] = data[row]['extension'][1]['valueMoney']['value']
        except(KeyError, IndexError):
            extension_dict['pr_payment'] = 'Null'

        try:
            extension_dict['fi_num'] = data[row]['extension'][2]['valueIdentifier']['value']
        except(KeyError, IndexError):
            extension_dict['fi_num'] = 'Null'


def facility_Outpatient_Format (row, file, facility_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    keyList = []
    for key in data[row]['facility'].keys():
        keyList.append(key)
    #print(keyList)
    if keyList == ['display', 'extension', 'identifier']:
        try:
            facility_dict['Facility_Name'] = data[row]['facility']['display']
            facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
            facility_dict['Facility_Type'] = data[row]['facility']['extension'][0]['valueCoding']['display']
            facility_dict['Facility_NPI'] = data[row]['facility']['identifier']['value']
        except (KeyError, IndexError):
            facility_dict['Facility_Name'] = 'Null'
            facility_dict['clm_fac_type_cd'] = 'Null'
            facility_dict['Facility_Type'] = 'Null'
            facility_dict['Facility_NPI'] = 'Null'
    else:
        try:
            facility_dict['Facility_Name'] = 'Null'
            facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
            facility_dict['Facility_Type'] = data[row]['facility']['extension'][0]['valueCoding']['display']
            facility_dict['Facility_NPI'] = data[row]['facility']['identifier']['value']
        except (KeyError, IndexError):
            facility_dict['Facility_Name'] = 'Null'
            facility_dict['clm_fac_type_cd'] = 'Null'
            facility_dict['Facility_Type'] = 'Null'
            facility_dict['Facility_NPI'] = 'Null'


def facility_HHA_Format (row, file, facility_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    if len(data[row]['facility']) == 3:
        try:
            facility_dict['Facility_Name'] = data[row]['facility']['display']
        except (KeyError, IndexError):
            facility_dict['Facility_Name'] = 'Null'
        try:
            facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
        except (KeyError, IndexError):
            facility_dict['clm_fac_type_cd'] = 'Null'
        try:
            facility_dict['Facility_Type'] = data[row]['facility']['extension'][0]['valueCoding']['display']
        except (KeyError, IndexError):
            facility_dict['Facility_Type'] = 'Null'
    else:
        facility_dict['Facility_name'] = 'Null'
        try:
            facility_dict['clm_fac_type_cd'] = data[row]['facility']['extension'][0]['valueCoding']['code']
        except (KeyError, IndexError):
            facility_dict['clm_fac_type_cd'] = 'Null'
        try:
            facility_dict['Facility_Type'] = data[row]['facility']['extension'][0]['valueCoding']['display']
        except (KeyError, IndexError):
            facility_dict['Facility_Type'] = 'Null'


def information_Inpatient_Format (row, file, information_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        information_dict['NCH_Weekly_Processing_Date'] = data[row]['information'][0]['timingDate']
    except (KeyError, IndexError):
        information_dict['NCH_Weekly_Processing_Date'] = 'Null'

    try:
        information_dict['NCH_Patient_Status_Indicator_Code'] = data[row]['information'][1]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['NCH_Patient_Status_Indicator_Code'] = 'Null'

    try:
        information_dict['NCH_Patient_Status_Indicator_Display'] = data[row]['information'][1]['code']['coding'][0]\
            ['display']
    except (KeyError, IndexError):
        information_dict['NCH_Patient_Status_Indicator_Display'] = 'Null'

    try:
        information_dict['Claim_Inpatient_Admission_Type_Code'] = data[row]['information'][2]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['Claim_Inpatient_Admission_Type_Code'] = 'Null'

    try:
        information_dict['Claim_Inpatient_Admission_Type_Display'] = data[row]['information'][2]['code']['coding'][0]['display']
    except (KeyError, IndexError):
        information_dict['Claim_Inpatient_Admission_Type_Display'] = 'Null'

    try:
        information_dict['Claim_Source_Inpatient_Admission_Code'] = data[row]['information'][3]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['Claim_Source_Inpatient_Admission_Code'] = 'Null'

    try:
        information_dict['NCH_Blood_Pints_Furnished_Quantity'] = data[row]['information'][4]['valueQuantity']['value']
    except (KeyError, IndexError):
        information_dict['NCH_Blood_Pints_Furnished_Quantity'] = 'Null'

    try:
        information_dict['Claim_Frequency_Code'] = data[row]['information'][5]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['Claim_Frequency_Code'] = 'Null'

    try:
        information_dict['Patient_Discharge_Status_Code'] = data[row]['information'][6]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['Patient_Discharge_Status_Code'] = 'Null'

    try:
        information_dict['Patient_Discharge_Status_Display'] = data[row]['information'][6]['code']['coding'][0]['display']
    except (KeyError, IndexError):
        information_dict['Patient_Discharge_Status_Display'] = 'Null'

    try:
        information_dict['NCH_Primary_Payer_Code'] = data[row]['information'][7]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['NCH_Primary_Payer_Code'] = 'Null'

    try:
        information_dict['NCH_Primary_Payer_Display'] = data[row]['information'][7]['code']['coding'][0]['display']
    except (KeyError, IndexError):
        information_dict['NCH_Primary_Payer_Display'] = 'Null'


def information_Hospice_Format (row, file, information_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)
    oddBall = False

    try:
        information_dict['nch_wkly_proc_dt'] = data[row]['information'][0]['timingDate']  # nch_wkly_proc_dt
    except (KeyError, IndexError):
        information_dict['nch_wkly_proc_dt'] = 'Null'

    try:
        information_dict['nch_ptnt_stus_ind_cd'] = data[row]['information'][1]['code']['coding'][0]['code']  # nch_ptnt_stus_ind_cd
        if information_dict['nch_ptnt_stus_ind_cd'] not in {'A','B', 'C'}:
            information_dict['nch_ptnt_stus_ind_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
            oddBall = True
    except (KeyError, IndexError):
        information_dict['nch_ptnt_stus_ind_cd'] = 'Null'


    try:
        if oddBall:
            information_dict['nch_ptnt_stus_ind_display'] = data[row]['information'][3]['code']['coding'][0]['display']
        else:
            information_dict['nch_ptnt_stus_ind_display'] = data[row]['information'][1]['code']['coding'][0]['display']  # nch_ptnt_stus_ind_display
    except (KeyError, IndexError):
        information_dict['nch_ptnt_stus_ind_display'] = 'Null'

    try:
        if oddBall:
            information_dict['clm_ip_admsn_type_cd'] = data[row]['information'][1]['code']['coding'][0]['code']
        else:
            information_dict['clm_ip_admsn_type_cd'] = data[row]['information'][2]['code']['coding'][0]['code']  # clm_ip_admsn_type_cd
    except (KeyError, IndexError):
        information_dict['clm_ip_admsn_type_cd'] = 'Null'

    try:
        if oddBall:
            information_dict['clm_ip_admsn_type_display'] = data[row]['information'][1]['code']['coding'][0]['display']
        else:
            information_dict['clm_ip_admsn_type_display'] = data[row]['information'][2]['code']['coding'][0]['display']  # clm_ip_admsn_type_display
    except (KeyError, IndexError):
        information_dict['clm_ip_admsn_type_display'] = 'Null'

    try:
        if oddBall:
            information_dict['clm_src_ip_admsn_cd'] = data[row]['information'][2]['code']['coding'][0]['code'] # clm_src_ip_admsn_cd
        else:
            information_dict['clm_src_ip_admsn_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['clm_src_ip_admsn_cd'] = 'Null'

    try:
        information_dict['nch_blood_pnts_frnshd_qty'] = data[row]['information'][4]['valueQuantity']['value']  # nch_blood_pnts_frnshd_qty
    except (KeyError, IndexError):
        information_dict['nch_blood_pnts_frnshd_qty'] = 'Null'

    try:
        if oddBall:
            information_dict['clm_freq_cd'] = data[row]['information'][6]['code']['coding'][0]['code']  # clm_freq_cd
        else:
            information_dict['clm_freq_cd'] = data[row]['information'][5]['code']['coding'][0]['code']
    except (KeyError, IndexError):
        information_dict['clm_freq_cd'] = 'Null'

    try:
        if oddBall:
            information_dict['clm_freq_display'] = data[row]['information'][6]['code']['coding'][0]['display']  # clm_freq_display
        else:
            information_dict['clm_freq_display'] = data[row]['information'][5]['code']['coding'][0]['display']
    except (KeyError, IndexError):
        information_dict['clm_freq_display'] = 'Null'

    try:
        if oddBall:
            information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][7]['code']['coding'][0]['code']
        else:
            information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][6]['code']['coding'][0]['code']  # ptnt_dschrg_stus_cd
    except (KeyError, IndexError):
        information_dict['ptnt_dschrg_stus_cd'] = 'Null'

    try:
        if oddBall:
            information_dict['ptnt_dschrg_stus_display'] = data[row]['information'][7]['code']['coding'][0]['display']
            oddBall = False
        else:
            information_dict['ptnt_dschrg_stus_display'] = data[row]['information'][6]['code']['coding'][0]['display']  # ptnt_dschrg_stus_display
    except (KeyError, IndexError):
        information_dict['ptnt_dschrg_stus_display'] = 'Null'


def procedure_Key8_Format (row, file, procedure_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    for p in range(0,5):
        try:
            procedure_dict[f'Date of Procedure {p + 1}'] = data[row]['procedure'][p]['date']
        except KeyError:
            procedure_dict[f'Date of Procedure {p + 1}'] = 'Null'
        except IndexError:
            procedure_dict[f'Date of Procedure {p + 1}'] = 'Null'
        try:
            procedure_dict[f'Procedure Code {p + 1}'] = data[row]['procedure'][p]['procedureCodeableConcept']['coding'][0]['code']
        except KeyError:
            procedure_dict[f'Procedure Code {p + 1}'] = 'Null'
        except IndexError:
            procedure_dict[f'Procedure Code {p + 1}'] = 'Null'
        try:
            procedure_dict[f'Procedure Display {p + 1}'] = data[row]['procedure'][p]['procedureCodeableConcept']['coding'][0]['display']
        except KeyError:
            procedure_dict[f'Procedure Display {p + 1}'] = 'Null'
        except IndexError:
            procedure_dict[f'Procedure Display {p + 1}'] = 'Null'


def recordItemMatch (word, row, item_dict, fs, item_fields, split):
    x = open(fs)
    d = x.read()
    data = json.loads(d)

    if word == item_fields[0]:  # line_prmry_alowd_chrg_amt
        print(f'{item_fields[0]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][0]['amount']['value']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[1]:  # line_dme_prchs_price_amt
        print(f'{item_fields[1]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[2]:  # dmerc_line_mtus_cd
        print(f'{item_fields[2]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['extension'][2]['valueQuantity']['code']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[3]:  # dmerc_line_mtus_cnt
        print(f'{item_fields[3]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['extension'][2]['valueQuantity']['value']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[4]:  # dmerc_line_scrn_svgs_amt
        print(f'{item_fields[4]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['extension'][1]['valueQuantity']['value']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[5]:  # suplrnum
        print(f'{item_fields[5]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['extension'][0]['valueIdentifier']['value']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[6]:  # carr_line_rdcd_pmt_phys_astn_c
        print(f'{item_fields[6]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][0]['reason']['coding'][0]['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
                # return item_dict[f'{word}']
        else:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[7]:  # line_nch_pmt_amt
        print(f'{item_fields[7]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][1]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[8]:  # line_pmt_80_100_cd
        print(f'{item_fields[8]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][1]['extension'][0]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
                return item_dict[f'{word}']
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][2]['extension'][0]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
                return item_dict[f'{word}']

    elif word == item_fields[9]:  # line_bene_pmt_amt
        print(f'{item_fields[9]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][2]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            except KeyError:
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[10]:  # line_prvdr_pmt_amt
        print(f'{item_fields[10]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][3]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][4]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[11]:  # line_bene_ptb_ddctbl_amt
        print(f'{item_fields[11]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[12]:  # line_bene_prmry_pyr_pd_amt
        print(f'{item_fields[12]} : ', dt.datetime.now())
        if split == 4:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][5]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[13]:  # line_coinsrnc_amt
        print(f'{item_fields[13]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][6]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            except KeyError:
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[14]:  # line_sbmtd_chrg_amt
        print(f'{item_fields[14]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][7]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[15]:  # line_alowd_chrg_amt
        print(f'{item_fields[15]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][8]['amount']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][9]['amount']['value']
            except KeyError:
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[16]:  # line_prcsg_ind_cd
        print(f'{item_fields[16]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][9]['reason']['coding'][0]['display']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['adjudication'][10]['reason']['coding'][0]['display']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
                return item_dict[f'{word}']

    elif word == item_fields[17]:  # careTeamLinkId
        print(f'{item_fields[17]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['careTeamLinkId']
        except (KeyError, IndexError):
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[18]:  # line_cms_type_srvc_cd
        print(f'{item_fields[18]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['category']['coding'][0]['code']
        except (KeyError, IndexError):
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[19]:  # diagnosisLinkId
        print(f'{item_fields[19]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['diagnosisLinkId']
        except (KeyError, IndexError):
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[20]:  # carr_line_mtus_cd
        print(f'{item_fields[20]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['extension'][0]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[21]:  # carr_line_mtus_cnt
        print(f'{item_fields[21]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['extension'][1]['valueQuantity']['value']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[22]:  # betos_cd
        print(f'{item_fields[22]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['extension'][2]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['extension'][3]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[23]:  # line_service_deductable
        print(f'{item_fields[23]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['extension'][3]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
                return item_dict[f'{word}']
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['extension'][4]['valueCoding']['code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
                return item_dict[f'{word}']

    elif word == item_fields[24]:  # line_place-of_service_cd
        print(f'{item_fields[24]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['locationCodeableConcept']['coding'][0]['code']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[25]:  # prvdr_state_cd
        print(f'{item_fields[25]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['locationCodeableConcept']['extension'][0]['valueCoding'][
                'code']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[26]:  # prvdr_zip
        print(f'{item_fields[26]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[0]['item'][0]['locationCodeableConcept']['extension'][1]['valueCoding']['code']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[27]:  # dmerc_line_prcng_state_cd
        print(f'{item_fields[27]} : ', dt.datetime.now())
        if split == 1:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['locationCodeableConcept']['extension'][1]['valueCoding'][
                    'code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[28]:  # dmerc_line_supplr_type_cd
        print(f'{item_fields[28]} : ', dt.datetime.now())
        if split == 1:
            item_dict[f'{word}'] = 'Null'
        else:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['locationCodeableConcept']['extension'][2]['valueCoding'][
                    'code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'

    elif word == item_fields[29]:  # carr_line_prcng_lclty_cd
        print(f'{item_fields[29]} : ', dt.datetime.now())
        if split in {1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23}:
            try:
                item_dict[f'{word}'] = data[row]['item'][0]['locationCodeableConcept']['extension'][2]['valueCoding'][
                    'code']
            except (KeyError, IndexError):
                item_dict[f'{word}'] = 'Null'
        else:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[30]:  # hcpcs
        print(f'{item_fields[30]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}'] = data[row]['item'][0]['service']['coding'][0]['code']
        except KeyError:
            item_dict[f'{word}'] = 'Null'

    elif word == item_fields[31]:  # servicedPeriod
        print(f'{item_fields[31]} : ', dt.datetime.now())
        try:
            item_dict[f'{word}_Start'] = data[row]['item'][0]['servicedPeriod']['start']
            item_dict[f'{word}_End'] = data[row]['item'][0]['servicedPeriod']['end']
        except KeyError:
            item_dict[f'{word}_Start'] = 'Null'
            item_dict[f'{word}_End'] = 'Null'


def lookingForItemFields (words, fs, row, item_dict, item_fields, split):
    x = open(fs)
    d = x.read()
    records = json.loads(d)
    for word in words:
        match = re.findall(word, str(records[row]['item']))
        if match:
            recordItemMatch(word, row, item_dict, fs, item_fields, split)
        else:
            item_dict[f'{word}'] = 'Null'


def information_Outpatient_Format (row, file, information_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    try:
        information_dict['nch_wkly_proc_dt'] = data[row]['information'][0]['timingDate']
        information_dict['clm_freq_cd'] = data[row]['information'][1]['code']['coding'][0]['code']
        information_dict['clm_freq_display'] = data[row]['information'][1]['code']['coding'][0]['display']
        information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][2]['code']['coding'][0]['code']
        information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][2]['code']['coding'][0]['display']
    except (KeyError, IndexError):
        try:
            information_dict['nch_wkly_proc_dt'] = 'Null'
            information_dict['clm_freq_cd'] = data[row]['information'][0]['code']['coding'][0]['code']
            information_dict['clm_freq_display'] = data[row]['information'][0]['code']['coding'][0]['display']
            information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][1]['code']['coding'][0]['code']
            information_dict['ptnt_dschrg_stus_display'] = data[row]['information'][1]['code']['coding'][0]['display']
        except (KeyError, IndexError):
            information_dict['nch_wkly_proc_dt'] = 'Null'
            information_dict['clm_freq_cd'] = 'Null'
            information_dict['clm_freq_display'] = 'Null'
            information_dict['ptnt_dschrg_stus_cd'] = 'Null'
            information_dict['ptnt_dschrg_stus_display'] = 'Null'


def information_HHA_Format (row, file, information_dict):
    x = open(file)
    d = x.read()
    data = json.loads(d)

    feb24_21_File = False

    if len(data[row]['information']) == 4:
        feb24_21_File = True

    if feb24_21_File:
        try:
            information_dict['nch_wkly_proc_dt'] = data[row]['information'][0]['timingDate']
        except(KeyError, IndexError):
            information_dict['nch_wkly_proc_dt'] = 'Null'
        try:
            information_dict['clm_frq_cd'] = data[row]['information'][1]['code']['coding'][0]['code']
        except(KeyError, IndexError):
            information_dict['clm_freq_cd'] = 'Null'
        try:
            information_dict['clm_freq_display'] = data[row]['information'][1]['code']['coding'][0]['display']
        except(KeyError, IndexError):
            information_dict['clm_freq_display'] = 'Null'
        try:
            information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][2]['code']['coding'][0]['code']
        except(KeyError, IndexError):
            information_dict['ptnt_dschrg_stus_cd'] = 'Null'
        try:
            information_dict['ptnt_dschrg_stus_dispaly'] = data[row]['information'][2]['code']['coding'][0]['display']
        except(KeyError, IndexError):
            information_dict['ptnt_dschrg_stus_display'] = 'Null'
        try:
            information_dict['clm_hha_frfl_cd'] = data[row]['information'][3]['code']['coding'][0]['code']
        except(KeyError, IndexError):
            information_dict['clm_hha_frfl_cd'] = 'Null'
        try:
            information_dict['clm_hha_frfl_display'] = data[row]['information'][3]['code']['coding'][0]['display']
        except(KeyError, IndexError):
            information_dict['clm_hha_frfl_display'] = 'Null'

    else:
        try:
            information_dict['nch_wkly_proc_dt'] = 'Null'
            information_dict['clm_freq_cd'] = data[row]['information'][0]['code']['coding'][0]['code']
            information_dict['clm_freq_display'] = data[row]['information'][0]['code']['coding'][0]['display']
            information_dict['ptnt_dschrg_stus_cd'] = data[row]['information'][1]['code']['coding'][0]['code']
            information_dict['ptnt_dschrg_stus_display'] = data[row]['information'][1]['code']['coding'][0]['display']
            information_dict['clm_hha_frfl_cd'] = 'Null'
            information_dict['clm_hha_frfl_display'] = 'Null'
        except (KeyError, IndexError):
            information_dict['nch_wkly_proc_dt'] = 'Null'
            information_dict['clm_freq_cd'] = 'Null'
            information_dict['clm_freq_display'] = 'Null'
            information_dict['ptnt_dschrg_stus_cd'] = 'Null'
            information_dict['ptnt_dschrg_stus_display'] = 'Null'
            information_dict['clm_hha_frfl_cd'] = 'Null'
            information_dict['clm_hha_frfl_display'] = 'Null'

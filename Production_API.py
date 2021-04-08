# Denver Hancock
# January 4th, 2020
# This program implements the production BCDA API and utilizes the Phynet Client Key
########################################################################################################################
import requests
import logging
import ndjson
from time import sleep
import datetime as dt

logging.basicConfig(filename='../Prod_API_DEBUG_log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
########################################################################################################################
# MAKE SURE THE APPROPRIATE INDEX IS USED FOR THE DESIRED FILE
# ft[0] = 'Patient'
# ft[1] = 'Coverage'
# ft[2] = 'ExplanationOfBenefit'
filetype = ['Patient', 'Coverage', 'ExplanationOfBenefit']
ft = filetype[0]


response = requests.get("https://api.bcda.cms.gov/api/v1/metadata", headers={'accept': 'application/json'})

try:
    response.raise_for_status()
except Exception as exec:
    print('There was an error: %s' % exec)

logging.debug(f'JSON Outpout: {response.json}, Response Headers: {response.headers}')
version = response.json()['software']['version']
#print(f'Recieved Status Code: {response.status_code}')
#print(f'The API is currently on version: {version}')

# as of 2/24/2021, BCDA API is on version r94

# A POST request is required to send credentials
response_i = requests.post("https://api.bcda.cms.gov/auth/token", auth=('15c1e612-9f89-4cf1-8dbf-1b729e01c1ce',
                                                                    '290ee2352b796be67b23177ff0340f460b3864cb258484148161fddc2a7bb34bc70284e9f1c9cdb0'))
try:
    response.raise_for_status()
except Exception as exec:
    print('There was an error: %s' % exec)

logging.debug(f'JSON Response to POST: {response_i.json()}')
token = response_i.json()['access_token']
authToken = 'Bearer ' + token


# This GET should return a success message
response_ii = requests.get('https://api.bcda.cms.gov/auth/welcome', headers={'Authorization': authToken})

try:
    response.raise_for_status()
except Exception as exec:
    print('There was an error: %s' % exec)

logging.debug(f'JSON Response to GET: {response_ii.json()}')

# Now that authentication is set up, let's run a job!
response_iii = requests.get('https://api.bcda.cms.gov/api/v1/Patient/$export?_type=' + ft +
                            '&_since=2021-03-16T08:00:00.000-05:00', headers={'Authorization': authToken,
                                            'accept': 'application/fhir+json', 'Prefer': 'respond-async'})

print(f'Received Status Code: {response_iii.status_code} after sending GET request for jobID')
logging.debug(f'Response headers from GET request for current job: {response_iii.headers}')
jobID = response_iii.headers.get('Content-Location')
jobID = jobID[-5:]
print(jobID) 

# THE FOLLOWING TIMER IS SET UP TO RENEW THE ACCESS TOKEN AS NEEDED TO AVOID DISCONNECTION
Status_Code = 202
start = dt.datetime.now()
timer = start + dt.timedelta(minutes=14)

while Status_Code == 202:
    sleep(100)
    r = requests.get('https://api.bcda.cms.gov/api/v1/jobs' + jobID, headers={'Authorization': authToken, 'accept': 'application/fhir+json',
                                                                              'Accept-Encoding': 'gzip'})
    Status_Code = r.status_code
    print(Status_Code)
    r_h = r.headers
    percent = r_h.get('X-Progress')
    print(percent)
    start = dt.datetime.now()
    logging.debug(f'A new token will be requested at {timer}. The current time is {start}')
    if start > timer:
        new_token = requests.post("https://api.bcda.cms.gov/auth/token", auth=('15c1e612-9f89-4cf1-8dbf-1b729e01c1ce',
                                                                                '290ee2352b796be67b23177ff0340f460b3864cb258484148161fddc2a7bb34bc70284e9f1c9cdb0'))
        print(f'Received Status Code: {new_token.status_code}')
        print(new_token.json())
        token = new_token.json()['access_token']
        authToken = 'Bearer ' + token
        print('Here is the new Access Token: {}'.format(authToken))
        timer = start + dt.timedelta(minutes=14)


if Status_Code != 200:
    print('Error:\n Job did not finish. Try double-checking the JobID.')

response_iv = r.json()
print(f'The resulting .JSON file is: {response_iv}')

filenames = response_iv['output']
filename_ = filenames[0]
filename__ = filenames[1]
filename___ = filenames[2]
filename____ = filenames[3]
filename_____ = filenames[4]
print(f'{filename_}\n{filename__}\n{filename___}\n{filename____}\n{filename_____}')

filename_Patient_1 = filename_['url']
filename_Patient_2 = filename__['url']
filename_Patient_3 = filename___['url']
filename_Patient_4 = filename____['url']
filename_Patient_5 = filename_____['url']
print(f'{filename_Patient_1}\n{filename_Patient_2}\n{filename_Patient_3}\n{filename_Patient_4}\n{filename_Patient_5}')


response_v = requests.get(filename_Patient_1, headers={"Authorization": authToken, "accept": "application/fhir+json",
                                                       "Accept-Encoding": "gzip"})
print(f'Received Status Code for {ft} Request: {response_v.status_code}')
r_v_h = response_v.headers
print(r_v_h)

response_vi = requests.get(filename_Patient_2, headers={"Authorization": authToken, "accept": "application/fhir+json",
                                                       "Accept-Encoding": "gzip"})
print(f'Received Status Code for {ft} Request: {response_vi.status_code}')
r_vi_h = response_vi.headers
print(r_vi_h)

response_vii = requests.get(filename_Patient_3, headers={"Authorization": authToken, "accept": "application/fhir+json",
                                                       "Accept-Encoding": "gzip"})
print(f'Received Status Code for {ft} Request: {response_vii.status_code}')
r_viii_h = response_vii.headers
print(r_viii_h)

response_viii = requests.get(filename_Patient_4, headers={"Authorization": authToken, "accept": "application/fhir+json",
                                                       "Accept-Encoding": "gzip"})
print(f'Received Status Code for {ft} Request: {response_viii.status_code}')
r_viii_h = response_viii.headers
print(r_viii_h)

response_ix = requests.get(filename_Patient_5, headers={"Authorization": authToken, "accept": "application/fhir+json",
                                                       "Accept-Encoding": "gzip"})
print(f'Received Status Code for {ft} Request: {response_ix.status_code}')
r_ix_h = response_ix.headers
print(r_ix_h)


with open(f'API_{ft}_Data_03162021_MAR29(1).json', 'w', encoding="utf-8") as f:
    ndjson.dump(response_v.json(cls=ndjson.Decoder), sort_keys=True, indent=4, fp=f)
    f.close()

with open(f'API_{ft}_Data_03162021_MAR29(2).json', 'w', encoding="utf-8") as f:
    ndjson.dump(response_vi.json(cls=ndjson.Decoder), sort_keys=True, indent=4, fp=f)
    f.close()

with open(f'API_{ft}_Data_03162021_MAR29(3).json', 'w', encoding="utf-8") as f:
    ndjson.dump(response_vii.json(cls=ndjson.Decoder), sort_keys=True, indent=4, fp=f)
    f.close()

with open(f'API_{ft}_Data_03162021_MAR29(4).json', 'w', encoding="utf-8") as f:
    ndjson.dump(response_viii.json(cls=ndjson.Decoder), sort_keys=True, indent=4, fp=f)
    f.close()

with open(f'API_{ft}_Data_03162021_MAR29(5).json', 'w', encoding="utf-8") as f:
    ndjson.dump(response_ix.json(cls=ndjson.Decoder), sort_keys=True, indent=4, fp=f)
    f.close()

import pandas as pd
from fuzzywuzzy import process

#data
df_stats = pd.read_csv(r'INPUT/data/covid_19_india.csv')

def check(x):
    states = 'Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jammu and Kashmir, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal, Andaman and Nicobar Islands, Delhi, Chandigarh, Dadra and Nagar Haveli and Daman and Diu, Lakshadweep, Ladakh, Jammu and Kashmir, Puducherry'
    states = states.split(", ")
    #print(len(states))
    if x in states:
        x = x
    if x not in states and (x != 'Cases being reassigned to states' and x != 'Unassigned'):
        match = process.extractOne(x, states)
        #print(f'{x} matches {match}.')
        if match[1]>=85:
            x = match[0]      
    return x
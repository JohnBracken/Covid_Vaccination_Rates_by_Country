# Script to find vaccination percentages by country.

import csv
import json
import operator

vax_records = []

with open('country_vaccinations.csv',newline = '') as vaxfile:
    csvreader = csv.DictReader(vaxfile)
    for row in csvreader:
        vax_records.append(row)

for j in range(len(vax_records)):
    try:
        vax_records[j]['total_vaccinations'] = float(vax_records[j]['total_vaccinations'])
    except:
        vax_records[j]['total_vaccinations'] = None
    try:
        vax_records[j]['people_vaccinated'] = float(vax_records[j]['people_vaccinated'])
    except:
        vax_records[j]['people_vaccinated'] = None
    try:
        vax_records[j]['people_fully_vaccinated'] = float(vax_records[j]['people_fully_vaccinated'])
    except:
        vax_records[j]['people_fully_vaccinated'] = None
    try:
        vax_records[j]['daily_vaccinations_raw'] = float(vax_records[j]['daily_vaccinations_raw'])
    except:
        vax_records[j]['daily_vaccinations_raw'] = None
    try:
        vax_records[j]['daily_vaccinations'] = float(vax_records[j]['daily_vaccinations'])
    except:
        vax_records[j]['daily_vaccinations'] = None
    try:
        vax_records[j]['total_vaccinations_per_hundred'] = float(vax_records[j]['total_vaccinations_per_hundred'])
    except:
        vax_records[j]['total_vaccinations_per_hundred'] = None
    try:
        vax_records[j]['people_vaccinated_per_hundred'] = float(vax_records[j]['people_vaccinated_per_hundred'])
    except:
        vax_records[j]['people_vaccinated_per_hundred'] = None
    try:
        vax_records[j]['people_fully_vaccinated_per_hundred'] = float(vax_records[j]['people_fully_vaccinated_per_hundred'])
    except:
        vax_records[j]['people_fully_vaccinated_per_hundred'] = None
    try:
        vax_records[j]['daily_vaccinations_per_million'] = float(vax_records[j]['daily_vaccinations_per_million'])
    except:
        vax_records[j]['daily_vaccinations_per_million'] = None

country_list = list()
for vax in vax_records:
    country_list.append(vax['country'])


country_list = list(set(country_list))
max_vax_list = []

for m in country_list:
    country_index = country_list.index(m)
    country = country_list[country_index]
    vax_by_country = [country_rec for country_rec in vax_records if country_rec['country'] == country]
    vax_per_hundred = [x['people_fully_vaccinated_per_hundred'] for x in vax_by_country if x['people_fully_vaccinated_per_hundred'] != None]
    if len(vax_per_hundred) > 0:
        max_vax = max(vax_per_hundred)
        max_vax_obj = dict.fromkeys({'country','max_vaxxed_people_per_hundred'})
        max_vax_obj['country'] = country
        max_vax_obj['max_vaxxed_people_per_hundred'] = max_vax
        max_vax_list.append(max_vax_obj)

max_vax_list = sorted(max_vax_list, key=operator.itemgetter('max_vaxxed_people_per_hundred'), reverse=True)

with open('max_vaccination_rates_by_country.json', 'w') as gout:
    json.dump(max_vax_list, gout, indent=4)

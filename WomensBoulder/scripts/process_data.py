import json
import csv
import os
import uuid

# define path
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
raw_data_path = os.path.join(data_dir, 'raw_data.json')

with open(raw_data_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# new copy
data = raw_data[:]

def json_to_csv(output_file):

    headers = list(data[0].keys())

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file has been created successfully.")

def add_ids():
    num_entries = len(data)
    for i, entry in enumerate(data, start=0):
        entry['id'] = num_entries - i

def find_cities():
    unique_cities = set()

    for competition in data:
        city = competition.get("city")
        if city:
            unique_cities.add(city)

    return list(unique_cities)

def find_countries_athlete():
    unique_country_athletes = set()

    for competition in data:
        results = competition.get("results")
        if results:
            for result in results:
                country_athlete = result.get("Country_Athlete")
                if country_athlete:
                    unique_country_athletes.add(country_athlete)

    return list(unique_country_athletes)

def clean_entries():
    for entry in data:
        if 'city' in entry and entry['city'] == 'WIEN':
            entry['city'] = 'VIENNA'
        if 'city' in entry and entry['city'] == 'LA REUNION':
            entry['city'] = 'REUNION'
        if 'results' in entry:
            for result in entry['results']:
                if 'Country' in result:
                    result['Country_Athlete'] = result.pop('Country')

def add_country(city_country):
    for entry in data:
        city = entry.get("city")
        if city in city_country:
            country = city_country[city]
            entry["country"] = country

def country_ath_full_name(country_names):
    for entry in data:
        if 'results' in entry:
            for result in entry['results']:
                if 'Country_Athlete' in result:
                    country_code = result['Country_Athlete']
                    if country_code in country_names:
                        result['Country_Athlete'] = country_names[country_code]




# add country
print(find_cities())
city_country_mapping = {
                        'SALT LAKE CITY': 'UNITED STATES',
                        "TAI'AN": 'CHINA',
                        'KAZO': 'JAPAN',
                        'MEIRINGEN': 'SWITZERLAND',
                        'WUJIANG': 'CHINA',
                        'CANMORE': 'CANADA',
                        'PARIS': 'FRANCE',
                        'AVILES': 'SPAIN',
                        'INNSBRUCK': 'AUSTRIA',
                        'LAVAL': 'FRANCE',
                        'MILANO': 'ITALY',
                        'BARCELONA': 'SPAIN',
                        'WIEN': 'AUSTRIA',
                        'HALL': 'AUSTRIA',
                        'BRIXEN': 'ITALY',
                        'SOFIA': 'BULGARIA',
                        'CHONGQING': 'CHINA',
                        'QINGHAI': 'CHINA',
                        'FIERA DI PRIMIERO': 'ITALY',
                        'GREIFENSEE': 'SWITZERLAND',
                        'MONTAUBAN': 'FRANCE',
                        'GRINDELWALD': 'SWITZERLAND',
                        'MUNICH': 'GERMANY',
                        'BRNO': 'CZECH REPUBLIC',
                        'BERN': 'SWITZERLAND',
                        'ERLANGEN': 'GERMANY',
                        'LOG-DRAGOMER': 'SLOVENIA',
                        'ARCO': 'ITALY',
                        'LA REUNION': 'FRANCE',
                        'NAVI MUMBAI': 'INDIA',
                        'NANJING': 'CHINA',
                        'HACHIOJI': 'JAPAN',
                        'VIENNA': 'AUSTRIA',
                        'VAIL': 'UNITED STATES',
                        'KITZBÜHEL': 'AUSTRIA',
                        'HACHIOJI, TOKYO': 'JAPAN',
                        'PRAGUE': 'CZECH REPUBLIC',
                        'BAKU': 'AZERBAIJAN',
                        'MOSCOW': 'RUSSIA',
                        'TORONTO': 'CANADA',
                        'SEOUL': 'SOUTH KOREA',
                        'EINDHOVEN': 'NETHERLANDS',
                        'SHEFFIELD': 'ENGLAND',
                        'HAIYANG': 'CHINA',
                        'REUNION': 'FRANCE',
                        'MILLAU': 'FRANCE'}
add_country(city_country_mapping)

# clean data
clean_entries()

# add ids
add_ids()

# add full country name
print(find_countries_athlete())
country_at_mapping = {
    'NOR': 'NORWAY',
    'CHI': 'CHILE',
    'POL': 'POLAND',
    'NEP': 'NEPAL',
    'ISR': 'ISRAEL',
    'HKG': 'HONG KONG',
    'BRA': 'BRAZIL',
    'VEN': 'VENEZUELA',
    'UZB': 'UZBEKISTAN',
    'POR': 'PORTUGAL',
    'AUT': 'AUSTRIA',
    'GER': 'GERMANY',
    'ECU': 'ECUADOR',
    'SVK': 'SLOVAKIA',
    'INA': 'INDONESIA',
    'LTU': 'LITHUANIA',
    'SUI': 'SWITZERLAND',
    'USA': 'UNITED STATES',
    'MEX': 'MEXICO',
    'IND': 'INDIA',
    'PER': 'PERU',
    'NED': 'NETHERLANDS',
    'ESA': 'EL SALVADOR',
    'CRO': 'CROATIA',
    'BLR': 'BELARUS',
    'SRB': 'SERBIA',
    'COL': 'COLOMBIA',
    'GUA': 'GUATEMALA',
    'AZE': 'AZERBAIJAN',
    'TPE': 'TAIWAN',
    'ARG': 'ARGENTINA',
    'HUN': 'HUNGARY',
    'ROU': 'ROMANIA',
    'SWE': 'SWEDEN',
    'IRI': 'IRAN',
    'LAT': 'LATVIA',
    'CFR': 'CENTRAL AFRICAN REPUBLIC',
    'MRI': 'MAURITIUS',
    'DEN': 'DENMARK',
    'GEO': 'GEORGIA',
    'GRE': 'GREECE',
    'THA': 'THAILAND',
    'GBR': 'UNITED KINGDOM',
    'JPN': 'JAPAN',
    'ITA': 'ITALY',
    'SGP': 'SINGAPORE',
    'UKR': 'UKRAINE',
    'PHI': 'PHILIPPINES',
    'MKD': 'NORTH MACEDONIA',
    'HON': 'HONDURAS',
    'KOR': 'SOUTH KOREA',
    'BEL': 'BELGIUM',
    'ISL': 'ICELAND',
    'TUR': 'TURKEY',
    'KAZ': 'KAZAKHSTAN',
    'PUR': 'PUERTO RICO',
    'CHN': 'CHINA',
    'FIN': 'FINLAND',
    'CAM': 'CAMBODIA',
    'ESP': 'SPAIN',
    'NZL': 'NEW ZEALAND',
    'CZE': 'CZECH REPUBLIC',
    'RUS': 'RUSSIA',
    'CAN': 'CANADA',
    'SLO': 'SLOVENIA',
    'FRA': 'FRANCE',
    'BUL': 'BULGARIA',
    'EST': 'ESTONIA',
    'RSA': 'SOUTH AFRICA',
    'AUS': 'AUSTRALIA'
}
country_ath_full_name(country_at_mapping)


# save data
json_data_path = os.path.join(data_dir, 'data.json')
csv_file_path = os.path.join(data_dir, 'data.csv')

with open(json_data_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

json_to_csv(csv_file_path)

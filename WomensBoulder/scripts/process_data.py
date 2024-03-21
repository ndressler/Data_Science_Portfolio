import json
import os

# define path
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
raw_data_path = os.path.join(data_dir, 'raw_data.json')

with open(raw_data_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# new copy
data = raw_data[:]

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

def replace_scores():
    for competition in data:
        for result in competition["results"]:
            # Qualification
            if "Qualification" in result and result["Qualification"] is not None:
                if '0T ' in result["Qualification"]:
                    result["Qualification"] = result["Qualification"].replace('0T ', '0T0 ')
                if ' 0B' in result["Qualification"]:
                    result["Qualification"] = result["Qualification"].replace(' 0B', ' 0B0')

            # Semi-final
            if "Semi-Final" in result and result["Semi-Final"] is not None:
                if '0T ' in result["Semi-Final"]:
                    result["Semi-Final"] = result["Semi-Final"].replace('0T ', '0T0 ')
                if ' 0B' in result["Semi-Final"]:
                    result["Semi-Final"] = result["Semi-Final"].replace(' 0B', ' 0B0')

            # Final
            if "Final" in result and result["Final"] is not None:
                if '0T ' in result["Final"]:
                    result["Final"] = result["Final"].replace('0T ', '0T0 ')
                if ' 0B' in result["Final"]:
                    result["Final"] = result["Final"].replace(' 0B', ' 0B0')

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

def parse_result_2018up(result):
    parsed_result = {}

    qualification = result.get("Qualification")
    if qualification is not None and qualification != "DNS":
        q_parts = qualification.split(' ')
        parsed_result["q_top"] = int(q_parts[0][0])
        parsed_result["q_zone"] = int(q_parts[0][-2])
        parsed_result["q_top_att"] = int(q_parts[1])
        parsed_result["q_zone_att"] = int(q_parts[2])

    semi_final = result.get("Semi-final")
    if semi_final is not None and semi_final != "DNS":
        sf_parts = semi_final.split(' ')
        parsed_result["sf_top"] = int(sf_parts[0][0])
        parsed_result["sf_zone"] = int(sf_parts[0][-2])
        parsed_result["sf_top_att"] = int(sf_parts[1])
        parsed_result["sf_zone_att"] = int(sf_parts[2])

    final = result.get("Final")
    if final is not None and final != "DNS":
        f_parts = final.split(' ')
        parsed_result["f_top"] = int(f_parts[0][0])
        parsed_result["f_zone"] = int(f_parts[0][-2])
        parsed_result["f_top_att"] = int(f_parts[1])
        parsed_result["f_zone_att"] = int(f_parts[2])

    return parsed_result

def parse_result_2017down(result):
    parsed_result = {}

    qualification = result.get("Qualification")
    if qualification is not None and qualification != "DNS":
        q_parts = qualification.split(' ')
        parsed_result["q_top"] = int(q_parts[0].split('T')[0])
        parsed_result["q_zone"] = int(q_parts[0].split('T')[1])
        parsed_result["q_top_att"] = int(q_parts[1].split('B')[0])
        parsed_result["q_zone_att"] = int(q_parts[1].split('B')[1])
    else:
        parsed_result["f_top"] = None
        parsed_result["f_zone"] = None
        parsed_result["f_top_att"] = None
        parsed_result["f_zone_att"] = None

    semi_final = result.get("Semi-Final")
    if semi_final is not None and semi_final != "DNS":
        sf_parts = semi_final.split(' ')
        parsed_result["sf_top"] = int(sf_parts[0].split('T')[0])
        parsed_result["sf_zone"] = int(sf_parts[0].split('T')[1])
        parsed_result["sf_top_att"] = int(sf_parts[1].split('B')[0])
        parsed_result["sf_zone_att"] = int(sf_parts[1].split('B')[1])

    final = result.get("Final")
    if final is not None and final != "DNS":
        f_parts = final.split(' ')
        parsed_result["f_top"] = int(f_parts[0].split('T')[0])
        parsed_result["f_zone"] = int(f_parts[0].split('T')[1])
        parsed_result["f_top_att"] = int(f_parts[1].split('B')[0])
        parsed_result["f_zone_att"] = int(f_parts[1].split('B')[1])

    return parsed_result



# add country
#print(find_cities())
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

# clean scores
replace_scores()

# add ids
add_ids()

# add full country name
#print(find_countries_athlete())
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

# separate points
for competition in data:
    if competition["year"] > 2017:
        for result in competition["results"]:
            result.update(parse_result_2018up(result))
    if competition["year"] <= 2017:
        for result in competition["results"]:
            result.update(parse_result_2017down(result))


# save data
json_data_path = os.path.join(data_dir, 'data.json')
csv_file_path = os.path.join(data_dir, 'data.csv')

with open(json_data_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

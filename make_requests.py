import requests
import json
# import urllib3
# https://www.ncdc.noaa.gov/cdo-web/api/v2/data
# ?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31
URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
token = 'JvEHhyqQqVpFAqcmAHjcuhjNfFNjyvKV'
total_records = 1386
offset = 1
req_limit = 1000
offset_count = 0


# response = requests.get(URL, headers={'Token': 'JvEHhyqQqVpFAqcmAHjcuhjNfFNjyvKV'})
# temp_data = json.dumps(response)

while offset < total_records:
    # offsetURL = URL + f"?offset=" + str(offset) + "&" + f"limit=" + str(req_limit)
    offsetURL = URL + f"?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&offset=" + str(offset) + f"&limit=" + str(req_limit)
    response = requests.get(offsetURL, headers={'Token': token})
    temp_data = response.json()
    output_filename = f"locations_{offset_count}.json"
    output_file = open(output_filename, 'w')
    output_file.write(json.dumps(temp_data))
    offset += 1000
    offset_count += 1

# print(response.json())


# def get_record_count(url):
#     pass
#
#
# def set_offset_increment(rec_count, limit):
#     pass
#
#
# def get_response(url):
#     pass
#
#
# def write_to_json(data):
#     pass

# if __name__ == "__main__":

# will need a way to parse request limit or also pass it in
# pass a url argument
# retrieve count of entries
# set total records
# loop through requests, updating offset

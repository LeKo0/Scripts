import requests
import sys

def main():

    try:

        # Get every parameter after the command
        query = sys.argv[1:]

    except IndexError as e:

        print("Missing argument \n Correct usage : python search.py <query>")

    else:

        # Google API token
        TOKEN = "-----"
        # Coordinate of central search point
        LONG, LAT = 45.545042,-73.676466
        # Radius of search area (max 50000)
        RADIUS = 50000
        # Language of results
        LANGUAGE = 'fr'
        # Base url for Google Place Search API
        SEARCH_BASE = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={token}&location={long},{lat}&radius={radius}&keyword={query}"
        # Base url for Google Place Details API
        DETAILS_BASE = "https://maps.googleapis.com/maps/api/place/details/json?key={token}&placeid={placeid}&language={language}"

        data = dict(name='', street_number='', route='', district='',
                    town='', province='', country='', postal_code='',
                    phone_number='', website='')

        search_url = SEARCH_BASE.format(token=TOKEN, long=LONG, lat=LAT,
                                        radius=RADIUS, query=query )
        search_response = requests.get(search_url)
        search_json = search_response.json()

        # If there is any results
        if(search_json['results'] != []):

            placeid = search_json['results'][0]['place_id']

            details_url = DETAILS_BASE.format(token=TOKEN, placeid=placeid,
                                                language=LANGUAGE)
            details_response = requests.get(details_url)
            details_json = details_response.json()

            address_components = details_json['result']['address_components']

            data['name'] = search_json['results'][0]['name']

            for component in address_components:

                if('street_number' in component['types']):
                    data['street_number'] = component['long_name']

                elif('route' in component['types']):
                    data['route'] = component['long_name']

                elif('sublocality_level_1' in component['types']):
                    data['district'] = component['long_name']

                elif('locality' in component['types']):
                    data['town'] = component['long_name']

                elif('administrative_area_level_1' in component['types']):
                    data['province'] = component['long_name']

                elif('country' in component['types']):
                    data['country'] = component['long_name']

                elif('postal_code' in component['types']):
                    data['postal_code'] = component['long_name']

            if('phone_number' in details_json['result']):
                data['phone_number'] = details_json['result']['formatted_phone_number']
            if('website' in details_json['result']):
                data['website'] = details_json['result']['website']

            print_dict(data)

        else:

            print("Note a place \n")

def print_dict(data):

    for entry in data:
        print("{} :".format(entry), end="")
        if(data[entry] is not None):
            print( " {}".format(data[entry]))
        else:
            print("Unavailable")

if __name__ == '__main__':
    main()

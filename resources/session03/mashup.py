import requests
from bs4 import BeautifulSoup
import pprint
import json


def fetch_search_results(**kwargs):
    base = 'http://raleigh.craigslist.org/search/apa'
    valid_kws = ('query', 'minAsk', 'maxAsk', 'bedrooms')
    use_kwargs = dict(
        [(key, val) for key, val in kwargs.items() if key in valid_kws])
    if not use_kwargs:
        raise ValueError("No valid keywords")

    resp = requests.get(base, params=use_kwargs, timeout=3)
    resp.raise_for_status()
    return resp.content, resp.apparent_encoding


def read_results(filename):
    fh = open(filename, 'r')
    body = fh.read()
    fh.close()
    return body


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed


def extract_listings(doc):
    location_attrs = {'data-latitude': True,
                      'data-longitude': True}
    for row in doc.find_all('p', class_='row',
                            attrs=location_attrs):
        location = dict(
            [(key, row.attrs.get(key)) for key in location_attrs])
        link = row.find('span', class_='pl').find('a')
        price_span = row.find('span', class_='price')
        listing = {
            'location': location,
            'href': link.attrs['href'],
            'description': link.string.strip(),
            'price': price_span.string.strip(),
            'size': price_span.next_sibling.strip(' \n-/')
        }
        yield listing


def add_address(listing):
    api_url = 'http://maps.googleapis.com/maps/api/geocode/json'
    loc = listing['location']
    parameters = {
        'sensor': 'false',
        'latlng': "%s,%s" % (loc['data-latitude'],
                             loc['data-longitude'])
    }
    resp = requests.get(api_url, params=parameters)
    data = json.loads(resp.text)
    if data['status'] == 'OK':
        best = data['results'][0]
        listing['address'] = best['formatted_address']
    else:
        listing['address'] = 'unavailable'
    return listing


def add_walkscore(listing):
    api_url = 'http://api.walkscore.com/score'
    apikey = 'YOURAPIKEYGOESHERE'
    loc = listing['location']
    if listing['address'] == 'unavailable':
        return listing
    parameters = {
        'lat': loc['data-latitude'], 'lon': loc['data-longitude'],
        'address': listing['address'], 'wsapikey': apikey,
        'format': 'json'
    }
    resp = requests.get(api_url, params=parameters)
    data = json.loads(resp.text)
    if data['status'] == 1:
        listing['ws_description'] = data['description']
        listing['ws_score'] = data['walkscore']
        listing['ws_link'] = data['ws_link']
    return listing


if __name__ == '__main__':
    params = {'minAsk': 500, 'maxAsk': 1000, 'bedrooms': 2}
    html, encoding = fetch_search_results(**params)
    doc = parse_source(html, encoding)
    for listing in extract_listings(doc):
        listing = add_address(listing)
        listing = add_walkscore(listing)
        pprint.pprint(listing)

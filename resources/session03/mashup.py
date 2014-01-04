from bs4 import BeautifulSoup
import json
import pprint
import requests


def fetch_search_results(
    query=None, minAsk=None, maxAsk=None, bedrooms=None
):
    incoming = locals().copy()
    base = 'http://seattle.craigslist.org/search/apa'
    search_params = dict(
        [(key, val) for key, val in incoming.items() if val is not None])
    if not search_params:
        raise ValueError("No valid keywords")

    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status() #<- no-op if status==200
    return resp.content, resp.encoding


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
    latlng_tmpl = "{data-latitude},{data-longitude}"
    parameters = {
        'sensor': 'false',
        'latlng': latlng_tmpl.format(**loc),
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
    apikey = '<your api key goes here>'
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
    html, encoding = fetch_search_results(
        minAsk=500, maxAsk=1000, bedrooms=2
    )
    doc = parse_source(html, encoding)
    for listing in extract_listings(doc):
        listing = add_address(listing)
        listing = add_walkscore(listing)
        pprint.pprint(listing)

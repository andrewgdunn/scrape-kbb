#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: ui.py
"""
ui
~~~~

- parse arguments
- construct the url
- test url (will make a request)
- parse html payload
- write out prices (excellent, very good, good, fair)

"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import argparse
import requests
from bs4 import BeautifulSoup

def main():

    description = """Scrape data from KBB"""

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('make', help='Make')
    parser.add_argument('model', help='Model')
    parser.add_argument('year', help='Year')
    parser.add_argument('style', help='Style')
    parser.add_argument('type', help='Price Type')
    parser.add_argument('mileage', help='Mileage')

    args = parser.parse_args()

    # Construct the URL
    # Example: http://www.kbb.com/kia/optima/2012-kia-optima/ex-sedan-4d/?pricetype=private-party&mileage=25000

    url = 'http://www.kbb.com/'
    url += args.make + '/'
    url += args.model + '/'
    url += args.year + '-' + args.make + '-' + args.model + '/'
    url += args.style + '/'

    parameters = {}
    parameters['pricetype'] = args.type
    parameters['mileage'] = args.mileage

    url_requested = requests.get(url, params=parameters)

    if url_requested.status_code == 200:
        prices = []

        soup = BeautifulSoup(url_requested.text)

        for div in soup.find_all('div', class_='value'):
            prices.append(div.text)

        print prices
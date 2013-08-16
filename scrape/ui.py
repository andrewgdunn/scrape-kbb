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
from scrape.util import construct_base_url


def main():

    description = """Scrape data from KBB"""

    parser = argparse.ArgumentParser(description=description)
    # Positional (pass them in proper order, and yes they are required)
    parser.add_argument('make', help='Make')
    parser.add_argument('model', help='Model')
    parser.add_argument('year', help='Year')
    parser.add_argument('style', help='Style')
    # Optional
    parser.add_argument('-i', '--intent', dest='intent', help='Intent')
    parser.add_argument('-p', '--pricetype', dest='pricetype', help='Price Type')
    parser.add_argument('-m', '--mileage', dest='mileage', help='Mileage')

    args = parser.parse_args()

    # Construct the base url
    url = construct_base_url(args.make, args.model, args.year, args.style)

    parameters = {}
    parameters['pricetype'] = args.intent
    parameters['mileage'] = args.mileage

    url_requested = requests.get(url, params=parameters)

    if url_requested.status_code == 200:

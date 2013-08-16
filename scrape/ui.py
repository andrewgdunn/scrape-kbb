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
__credits__ = ["Stephen Nettnin"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import argparse
from scrape.util import construct_base_url, construct_parameters
from scrape.util import url_fetch


def main():

    description = """Scrape data from KBB"""

    parser = argparse.ArgumentParser(description=description)
    # Positional (pass them in proper order, and yes they are required)
    parser.add_argument('make', help='Make')
    parser.add_argument('model', help='Model')
    parser.add_argument('year', help='Year')
    parser.add_argument('style', help='Style')
    # Optional
    optional_parameters = ['intent', 'pricetype', 'mileage']
    parser.add_argument('-i', '--intent', dest='intent', help='Intent')
    parser.add_argument('-p', '--pricetype', dest='pricetype', help='Price Type')
    parser.add_argument('-m', '--mileage', dest='mileage', help='Mileage')

    args = parser.parse_args()

    # Construct the base url
    url = construct_base_url(args.make, args.model, args.year, args.style)

    # we use the built in command 'vars' to convert the argparse.Namespace
    # to a standard python dictionary... what even is an argparse.Namespace?
    parameters = construct_parameters(vars(args), optional_parameters)

    url_fetched = url_fetch(url, parameters)

    print url_fetched

    # if url_fetched:
    #     """Now we have to:
    #      - figure out what parse method to use (based on intent and pricetype)
    #      - run said method
    #      - add an arg for output type
    #      - write output type processing
    #     """
    #     pass
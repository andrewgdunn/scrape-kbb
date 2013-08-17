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
from scrape.util import parse_new, parse_single, parse_list


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

    if url_fetched:
        """ Not super elegant, nice to make more than one comparison per
        conditional statement.

        Need to think through:
         - output formats
         - using intent also, because pricetype ins't enough:
          - - check out:
          http://www.kbb.com/kia/optima/2013-kia-optima/ex/
          http://www.kbb.com/kia/optima/2013-kia-optima/ex-sedan-4d/

          Neither of these things use an intent or pricetype and they are the same platform with the same trim level....
        """
        if not args.pricetype:
            print parse_single(url_fetched.text)
        if args.pricetype == 'cpo':
            print parse_single(url_fetched.text)
        if args.pricetype == 'retail':
            print parse_single(url_fetched.text)
        if args.pricetype == 'trade-in':
            print parse_list(url_fetched.text)
        if args.pricetype == 'private-party':
            print parse_list(url_fetched.text)

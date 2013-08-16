#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: scratch.py
"""
scratch
~~~~

for looking through the bs4 object its easier to use ipython

"""
__author__ = ["Andrew G. Dunn"]
__credits__ = ["Stephen Nettnin"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"


import argparse
# import requests
# from bs4 import BeautifulSoup

description = """Scrape data from KBB"""

parser = argparse.ArgumentParser(description=description)
# Positional (pass them in proper order, and yes they are required)
parser.add_argument('make', help='Make')
parser.add_argument('model', help='Model')
parser.add_argument('year', help='Year')
parser.add_argument('style', help='Style')
# Optional
optional_args_names = ['intent', 'pricetype', 'mileage']
parser.add_argument('-i', '--intent', dest='intent', help='Intent')
parser.add_argument('-p', '--pricetype', dest='pricetype', help='Price Type')
parser.add_argument('-m', '--mileage', dest='mileage', help='Mileage')

args = parser.parse_args('kia optima 2012 ex-sedan-4d -i buy-used -p private-party -m 25000'.split())



# example_url = 'http://www.kbb.com/kia/optima/2012-kia-optima/ex-sedan-4d/?pricetype=private-party&mileage=25000'

# url_requested = requests.get(example_url)

# if url_requested.status_code == 200:
#     prices = []

#     soup = BeautifulSoup(url_requested.text)

#     for div in soup.find_all('div', class_='value'):
#         print div.text


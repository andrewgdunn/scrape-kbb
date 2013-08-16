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


import requests
from bs4 import BeautifulSoup


example_url = 'http://www.kbb.com/kia/optima/2012-kia-optima/ex-sedan-4d/?pricetype=private-party&mileage=25000'

url_requested = requests.get(example_url)

if url_requested.status_code == 200:
    prices = []

    soup = BeautifulSoup(url_requested.text)

    for div in soup.find_all('div', class_='value'):
        print div.text
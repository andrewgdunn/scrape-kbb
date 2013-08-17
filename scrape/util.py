#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: util.py
"""
util.py
~~~~

Miscellaneous utility functions.
"""
__author__ = ["Andrew G. Dunn"]
__credits__ = ["Stephen Nettnin"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import requests
from bs4 import BeautifulSoup

def construct_base_url(make, model, year, style):
    url = 'http://www.kbb.com/'

    url += make + '/'
    url += model + '/'
    url += year + '-' + make + '-' + model + '/'
    url += style + '/'

    return url


def construct_parameters(args_dictionary, optional_parameter):    
    parameters = {}

    for param in optional_parameter:
        if args_dictionary[param]:
            parameters[param] = args_dictionary[param]

    return parameters


def url_fetch(url, parameters):
    try:
        payload = requests.get(url, params=parameters)
        if payload.status_code == 200:
            return payload
        else:
            return False
    except Exception:
        return False

def parse_new(url_payload):
    return 'taco'


def parse_single(url_payload):
    soup = BeautifulSoup(url_payload)

    div = soup.find('div', class_='value')
    return div.text.strip()


def parse_list(url_payload):
    prices = []

    soup = BeautifulSoup(url_payload)

    for div in soup.find_all('div', class_='value'):
        prices.append(div.text.strip())

    return prices

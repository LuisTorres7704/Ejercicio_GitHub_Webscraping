# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:38:52 2022

@author: lfern
"""
import requests
from bs4 import BeautifulSoup

t = requests.get("https://es.wikipedia.org/wiki/Git")
soup = BeautifulSoup(t.text, 'html.parser')
soup.find_all('p')

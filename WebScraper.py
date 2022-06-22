#!/usr/bin/env python3

"""
This code gets the prices from amazon webstore
"""

# import the required stuff
import bs4
import requests
import sys
import pyperclip

# if run from terminal, get the passed arguments
sys.argv

# if there were arguments take them as the URL, otherwise look for it on the clipboard
if len(sys.argv) > 1:
    productURL = sys.argv[1:]
else:
    productURL = pyperclip.paste()

# here we defined our function
def getAmazonPrice(URL):
    res = requests.get(URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price')
    return elems[0].text.strip(' ')

# here we print the result back to the user
print("The price is " + getAmazonPrice(productURL))

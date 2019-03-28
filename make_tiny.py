
import requests
import json
import urllib
import re
import os
from bs4 import BeautifulSoup


def make_tiny_link(hash_data,redirect_to,domain):    
    
    link = domain + redirect_to + "?he="+hash_data['email']+"&hl="+hash_data['link']

    encoded_link = urllib.parse.quote(link,safe='')

    tiny_url_endpoint = "https://tinyurl.com/create.php?source=&url=" + encoded_link + "&submit=Make+TinyURL%21&alias=" 

    r = requests.get(tiny_url_endpoint)
    print(r.status_code)

    page = str(BeautifulSoup(r.content))

    def getURL(page):
        """

        :param page: html of web page (here: Python home page) 
        :return: urls in that page 
        """
        start_link = page.find("small")
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1: end_quote]
        return url, end_quote

    urls = []
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            urls.append(url)
        else:
            break
    valid_urls = [] 
    for url in urls:

        if "https://tinyurl.com/" in url:
            valid_urls.append(url)
        

    
    valid_urls = list(set(valid_urls))


    return valid_urls[0]
        






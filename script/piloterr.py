# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 19:58:19 2025

@author: Lenovo
"""


import requests
from credential import x_api_key
import json

def website_crawler(site_url):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":site_url}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    # decode double escape "\\" and inline "\n" 
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    # decode special character 
    clean_html = clean_html.encode('latin-1').decode('utf-8')
   
    return clean_html

if __name__ == "__main__":
    # how to calll website_crawler
    product_hunt_url = "https://www.producthunt.com/leaderboard/daily/2025/11/22"
    html = website_crawler(product_hunt_url)
    

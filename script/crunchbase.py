# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 20:07:57 2025

@author: Lenovo
"""

import requests
from credential import x_api_key

def scrape_crunchbase_info(domain=None, query=None):
    url = "https://piloterr.com/api/v2/crunchbase/company/info"
    headers = {"x-api-key": x_api_key}

    querystring = {}

    if domain:
        querystring["domain"] = domain

    if query:
        querystring["query"] = query

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def get_linkedin_url(crunchbase_info):
    """ search linkein url in social_network list """
    
    networks = crunchbase_info.get("social_networks", [])

    for item in networks:
        name = item.get("name", "").lower()
        url = item.get("url", "")

        if "linkedin" in name:
            return url
    return ""

if __name__ == "__main__": 
    """
    crunchbase_info = {
    "social_networks": [
        {"url": "https://www.linkedin.com/company/producthunt", "name": "linkedin"},
        {"url": "https://www.instagram.com/producthunt", "name": "instagram"}
        ]
    }
    linkedin_url = get_linkedin_url(crunchbase_info)
    
    """
    # crunchbase_info
    #domain = "piloterr.com"
    domain = "blinkist.com"
    company_info = scrape_crunchbase_info(domain=domain)
    
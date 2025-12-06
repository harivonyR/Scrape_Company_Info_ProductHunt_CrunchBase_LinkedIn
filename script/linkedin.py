# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 20:08:07 2025

@author: Lenovo
"""

from credential import x_api_key
import requests


def scrape_linkedin_info(domain=None,company_url=None):
    
    if domain :
        url = f"https://piloterr.com/api/v2/linkedin/company/info?domain={domain}"
    
    elif company_url :
        url = f"https://piloterr.com/api/v2/linkedin/company/info?query={company_url}"
    
    else :
        return ""
    
    headers = {"x-api-key": x_api_key}
    response = requests.get(url, headers=headers)
    
    return response.json()

if __name__=="__main__" :
    readmill_domain = "readmill.com"
    linkedin_info = scrape_linkedin_info(domain=readmill_domain)
    
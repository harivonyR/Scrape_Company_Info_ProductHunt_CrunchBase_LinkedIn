# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 21:10:26 2025

@author: Lenovo
"""

def get_linkedin_url(crunchbase_info):
    """ search linkein url in social_network list """
    
    networks = crunchbase_info.get("social_networks", [])

    for item in networks:
        name = item.get("name", "").lower()
        url = item.get("url", "")

        if "linkedin" in name:
            return url
    return ""

if __name__ == "__name__" :
    crunchbase_info = {
    "social_networks": [
        {"url": "https://www.linkedin.com/company/producthunt", "name": "linkedin"},
        {"url": "https://www.instagram.com/producthunt", "name": "instagram"}
        ]
    }

    linkedin_url = get_linkedin_url(crunchbase_info)
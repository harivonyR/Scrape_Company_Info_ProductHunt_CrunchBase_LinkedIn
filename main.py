# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:52:49 2025

@author: Lenovo
"""
from script.producthunt import scrape_product_info
from script.linkedin import scrape_linkedin_info
from script.crunchbase import scrape_crunchbase_info, get_linkedin_url
from utils.url import get_domain_strict
import pandas as pd

product_launch = pd.read_csv("input/producthunt_archive_sample.csv",sep=",")

# 0- product row instance
row = product_launch.iloc[1]

# 1- Scrape ProductHunt Info
product_url = row["product_url"]

if product_url :
    producthunt_info = scrape_product_info(product_url)

# 2- lookup crunchbase_info
company_url = producthunt_info["company_url"]
domain = get_domain_strict(company_url)
crunchbase_info = scrape_crunchbase_info(domain)

# 3- lookup LinkedIn Info
linkedin_url = get_linkedin_url(crunchbase_info)
linkedin_info = scrape_linkedin_info(domain=domain)
#linkedin_info = scrape_linkedin_info(company_url=linkedin_url)
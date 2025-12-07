# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:52:49 2025

How it works : 
    - Load producthunt archive,
    - Scrape Producthunt info (title, desctiption, website, ...),
    - Scrape Crunchbase info,
    - Scrape LinkedIn info.

"""
from script.producthunt import scrape_product_info
from script.linkedin import scrape_linkedin_info
from script.crunchbase import scrape_crunchbase_info
from utils.url import get_domain_strict
import pandas as pd
import json
from tqdm import tqdm

product_launch = pd.read_csv("input/producthunt_archive_sample.csv", sep=",")

company_info = []


""" I. Loop on Product List """
for _, row in tqdm(product_launch.head(10).iterrows(), total=10, desc="Scraping"):
    entry = {}

    # 0 - Base data
    entry["product"] = row.to_dict()

    # 1 - ProductHunt
    product_url = row.get("product_url", "")
    producthunt_info = {}
    if product_url:
        producthunt_info = scrape_product_info(product_url)
    entry["product_hunt"] = producthunt_info

    # 2 - Crunchbase
    company_url = producthunt_info.get("company_url", "")
    crunchbase_info = {}
    domain = ""
    if company_url:
        domain = get_domain_strict(company_url)
        crunchbase_info = scrape_crunchbase_info(domain)
    entry["crunchbase_info"] = crunchbase_info

    # 3 - LinkedIn
    linkedin_info = {}
    if domain:
        linkedin_info = scrape_linkedin_info(domain=domain)
    entry["linkedin_info"] = linkedin_info

    company_info.append(entry)

""" II. Export json data """
with open("output/producthunt_crunchbase_linkedin_info.json", "w", encoding="utf-8") as f:
    json.dump(company_info, f, indent=4, ensure_ascii=False)

print("> Export completed !")

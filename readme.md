# Scrape Product Data & Company Info from ProductHunt, Crunchbase, and LinkedIn

## Description
This project demonstrates a **cross-platform scraping pipeline** that links products, companies, and people together.  
ProductHunt is used as the **entry point**, then enriched with company and profile data from **Crunchbase** and **LinkedIn** via the **Piloterr API**.

You can start with the prepared sample dataset:  
- [Product Hunt archive sample – CSV](https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping/blob/main/output/producthunt_archive_sample.csv)

Or generate a larger archive yourself using:  
- [GitHub – Scrape ProductHunt Archive](https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping)

## Features
- Scrape data from **ProductHunt, Crunchbase, and LinkedIn**
- Uses **Piloterr API** to simplify requests and handle bot evasion
- Safe getter utilities to handle missing or incomplete values
- Composite CSS selectors for elements without unique identifiers
- Data normalization, deduplication, and multi-format exports

## Requirements
- **Runtime**: Python 3.x
- **API key**: Piloterr API key
- **Libraries**: `requests`, `beautifulsoup4`, `pandas`, `tqdm`, `tldextract`
- **Input data**: Product list containing ProductHunt URLs  
  - Use the provided sample: [Product Hunt archive sample – CSV](https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping/blob/main/output/producthunt_archive_sample.csv)  
  - Or scrape a larger archive from: [GitHub – Scrape ProductHunt Archive](https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping)

## Installation
Step by step:

1. Clone the repository
```bash
git clone https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping
cd Producthunt_Launch_Archive_Scraping
```

2. Copy credentials template
```bash
copy credential.example.py credential.py
```

3. Open `credential.py` and paste your Piloterr API key
```python
x_api_key = "PASTE_YOUR_API_KEY_HERE"
```
> Sign up on the [Piloterr website](https://piloterr.com/register) to get free credits.

4. Install dependencies
```bash
pip install requests beautifulsoup4 pandas tldextract tqdm
```

5. Run the project
```bash
python main.py
```

## Configuration
- By default, `main.py` processes the **first 50 rows** of the product list.
- For full scraping, replace the progress bar definition:
```python
pbar = tqdm(product_launch.index)
```

## Usage
- Run as a standalone Python script
- Enrich ProductHunt product data with company information
- Output structured datasets ready for analytics, dashboards, or ML pipelines

## License
MIT

## References
- Tutorial (Colab): https://colab.research.google.com/drive/1_ChkmIjOy2ZDjMadP98OiHX2ctGAZ7E5
- ProductHunt archive list: https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping/blob/main/output/producthunt_archive_sample.csv
- ProductHunt archive scraping project: https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping

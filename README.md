# eBay Scraper

This simple Python script is an eBay scraper that can be used to get information about eBay items. The script supports getting the product name, price, reviews, shipping, and return information.

Group: Minasha Gunarathna and Chris Wang

[Writeup Link](https://docs.google.com/document/d/1rYdkB31ZbenmGjDe_nBia5T9W353hjuhragX80qiELg/edit?usp=sharing)

## How to Run
Dependencies: Python 3 with `selectorlib` and `requests` libraries installed.
To install the libraries, do `pip install selectorlib requests` in the terminal.

Download the repository and put the URLs of the items you want to scrape into the `urls.txt` file, separating them by line.
Next, run `python3 ebay.py`. The output information of the URLs (the product information) will be located in the `result.jsonl` file.

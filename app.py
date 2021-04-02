from datetime import datetime
from log import log
from src.browser.Browser import Browser
from src.Beer import Beer
from src.BrandFactory import BrandFactory
import os

def run():
    browser = Browser()
    log().info("Browser started")
    brand = BrandFactory(browser,os.environ['BRAND'])
    beer = brand.brand_selector()
    data = beer.crawl()
    best_choice = beer.select_best_price(data)
    print(best_choice)

        
if __name__ == '__main__':
    run()
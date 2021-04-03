from datetime import datetime
from log import log
from src.browser.Browser import Browser
from src.Beer import Beer
from src.BrandFactory import BrandFactory
import os

def run():
    try:
        brand_name = os.environ['BRAND'] if 'BRAND' in os.environ else 'ALL'
        browser = Browser()
        log().info("Browser started")
        brand = BrandFactory(browser,brand_name)
        beer = brand.brand_selector()
        if beer.brand == "ALL":
            data = beer.crawl_all()
            best_choices = beer.select_best_prices(data)
            print(best_choices)
        else:
            log().info(f"Going to {brand_name} url ")
            data = beer.crawl()
            log().info("Starting calculate the best choice")
            best_choice = beer.select_best_price(data)
            print(best_choice)
    
    except Exception as err:
      log().error(f"Error in method run: {type(err)} > {err}")
      raise err
        
if __name__ == '__main__':
    run()
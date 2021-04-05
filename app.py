from datetime import datetime
from log import log
from src.browser.Browser import Browser
from src.Beer import Beer
from src.BrandFactory import BrandFactory
import os

def run():
    try:
        street_name = os.environ['STREET'] if 'STREET' in os.environ else 'Rua Moura Brasil'
        street_number = os.environ['NUMBER'] if 'NUMBER' in os.environ else '60'
        neighborhood = os.environ['NEIGHBORHOOD'] if 'NEIGHBORHOOD' in os.environ else 'Laranjeiras'
        
        
        browser = Browser(street_name,street_number,neighborhood)
        
        brand_name = os.environ['BRAND'] if 'BRAND' in os.environ else 'ALL'
        brand = BrandFactory(browser,brand_name)
        beer = brand.brand_selector()
        
        if beer.brand == "ALL":
            data = beer.crawl_all()
            best_choices = beer.select_best_prices(data)
            best_choices_in_order = beer.select_best_prices_in_order(best_choices)
            log().info("The complete list of prices in order is:")
            print("\n")
            for i in (range(len(best_choices_in_order))):
                log().info(f"{i}:{best_choices_in_order[i]}")
                print("\n")
        else:
            log().info(f"Going to {brand_name} url ")
            data = beer.crawl()
            log().info("Starting calculate the best choice")
            best_choices = beer.select_best_price(data)
            best_choices_in_order = beer.select_best_prices_in_order(data)
            log().info(f"The best choice(s) is/are:")
            print("\n")
            log().info(f"{best_choices}")
            print("\n")
            log().info("The complete list of prices in order is:")
            for i in (range(len(best_choices_in_order))):
                log().info(f"{i}:{best_choices_in_order[i]}")
                print("\n")

            
    except Exception as err:
      log().error(f"Error in method run: {type(err)} > {err}")
      raise err
        
if __name__ == '__main__':
    run()
from datetime import datetime
from log import log
from src.Browser import Browser
from src.Beer import Beer
from src.BrandFactory import BrandFactory
import os

def run():
    try:

        browser = Browser(os.environ['STREET', os.environ['NUMBER'],os.environ['NEIGHBORHOOD'])
        
        brand_name = os.environ['BRAND'] if 'BRAND' in os.environ else 'ALL'
        
        brand = BrandFactory(browser,brand_name)
        
        beer = brand.brand_selector()
        
        if beer.brand == "ALL":
            log().info(f"Going to {brand_name} brands urls ")
            data = beer.crawl_all()
            log().info("Starting calculate the best choice")
            best_choices = beer.select_best_prices(data)
            best_choices_in_order = beer.select_best_prices_in_order(best_choices)
            log().info("The complete list of prices in order is:")
            print("\n")
            for i in (range(len(best_choices_in_order))):
                print(str(i+1)+"ª",best_choices_in_order[i])
                print("\n")
        else:
            log().info(f"Going to {brand_name} brand url ")
            data = beer.crawl()
            log().info("Starting calculate the best choice")
            best_choices = beer.select_best_price(data)
            best_choices_in_order = beer.select_best_prices_in_order(data)
            log().info(f"The best choice(s) is/are:")
            print("\n")
            print(best_choices)
            print("\n")
            log().info(f"The complete list of prices in order of {brand_name} is:")
            for i in (range(len(best_choices_in_order))):
                print(str(i+1)+"ª",best_choices_in_order[i])
                print("\n")
            
    except Exception as err:
      log().error(f"Error in method run: {type(err)} > {err}")
      raise err
        
if __name__ == '__main__':
    run()

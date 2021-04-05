from datetime import datetime
from log import log
from src.Browser import Browser
import re
from operator import itemgetter


class Beer:

    def __init__(self,browser,url,brand):
        self.browser = browser
        self.url = url
        self.brand = brand
    
    def get_dom(self,url,need_config):
       self.browser.goto(url,need_config)
       element = self.browser.driver.find_element_by_xpath("//*")
       return element

    def crawl(self):
        dom = self.get_dom(self.url,True)
        data = self.parse(dom,self.brand)
        return data
    
    def crawl_each(self,url,need_config,brand):
        dom = self.get_dom(url,need_config)
        data = self.parse(dom,brand)
        return data


    def crawl_all(self):
        data = []
        for url in self.url:
            if data == []:
                data.append(self.crawl_each(self.url[url],True,url))
            else:
                data.append(self.crawl_each(self.url[url],False,url))
        
        return data

        

    def transform_price(self,string_price):
        price = float(((string_price.text[-6:]).split(' ')[-1]).replace(',', '.')),
        return price[0]

    def get_volume(self,description):
        volume = int(re.findall(r'\d+', description.text)[0])
        return volume
    
    def get_price_per_liter(self,price,volume):
        if volume == 1:
            return price

        price_per_volume = (price*1000)/volume
        
        return round(price_per_volume,2)

    def parse(self,dom,brand):
        data = {}
        data_list = []
        descriptions = dom.find_elements_by_xpath("//h3[@class='css-krg860-productTitle']")
        prices = dom.find_elements_by_xpath("//div[@class='css-t89dhz-priceText']")
        
        for i in range(len(descriptions)):
            price = self.transform_price(prices[i])
            volume = self.get_volume(descriptions[i])
            data = {
                "brand": brand,
                "product_name" : descriptions[i].get_attribute("innerText"),
                "price" : price ,
                "volume" : volume,
                "price_per_liter":  self.get_price_per_liter(price,volume)
            }
            data_list.append(data)
        
        return data_list    
    

    def select_best_prices(self,data):
        best_choices = []
        for i in data:
            best_choices.extend(self.select_best_price(i))
        
        return best_choices

    def select_best_price(self,data):
        best_choices = []
        choice = {}
        list_liter_price = [x['price_per_liter'] for x in data]
        list_name = [x['product_name'] for x in data]
        list_price = [x['price'] for x in data]
        for i in range(len(list_liter_price)):
            if min(list_liter_price) == list_liter_price[i]:
                choice = {
                    "brand" : data[0]['brand'],
                    "product_name": list_name[i],
                    "price" : list_price[i],
                    "price_per_liter": list_liter_price[i]
                }
                best_choices.append(choice)
        
        return best_choices
    
    def select_best_prices_in_order(self,data):
        list_sorted = sorted(data, key=itemgetter('price_per_liter'), reverse=False)
        return list_sorted
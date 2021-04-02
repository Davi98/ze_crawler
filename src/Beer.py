from datetime import datetime
from log import log
from src.browser.Browser import Browser
import re


class Beer:

    def __init__(self,browser,url,brand):
        self.browser = browser
        self.url = url
        self.brand = brand
    
    def get_dom(self,url):
       self.browser.goto(url)
       element = self.browser.driver.find_element_by_xpath("//*")
       return element

    def crawl(self):
        dom = self.get_dom(self.url)
        data = self.parse(dom)
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

    def parse(self,dom):
        data = {}
        data_list = []
        descriptions = dom.find_elements_by_xpath("//h3[@class='css-krg860-productTitle']")
        prices = dom.find_elements_by_xpath("//div[@class='css-t89dhz-priceText']")
        
        for i in range(len(descriptions)):
            price = self.transform_price(prices[i])
            volume = self.get_volume(descriptions[i])
            data = {
                "brand": self.brand,
                "product_name" : descriptions[i].get_attribute("innerText"),
                "price" : price ,
                "volume" : volume,
                "price_per_liter":  self.get_price_per_liter(price,volume)
            }
            data_list.append(data)
        
        return data_list    
    
    def select_best_price(self,data):
        best_choice = []
        
        list_price = [x['price_per_liter'] for x in data]
        list_name = [x['product_name'] for x in data]
        for i in range(len(list_price)):
            if min(list_price) == list_price[i]:
                best_choice.append(list_name[i])
        
        return best_choice

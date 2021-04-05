import time
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import json


class Browser:

    def __init__(self,latitude,logitude):
        self.options = Options()
        self.options.set_preference('geo.prompt.testing', True)
        self.options.set_preference('geo.prompt.testing.allow', True)
        location_dict = {
        "location": {"lat": float(latitude), "lng": float(logitude)},
        "accuracy": 100.0
        }
        location_json = json.dumps(location_dict)
        location_config = f'data:application/json,{location_json}'
        self.options.set_preference('geo.provider.network.url',location_config)
        # self.options.add_argument('--headless')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Firefox(options=self.options)
        self.session_id = self.driver.session_id
        self.command_executor_url = self.driver.command_executor._url
    
    def goto(self, url,need_config):
        if need_config == True:
            self.config_location()
            if self.driver.current_url != url:
                self.driver.get(url)
        else:
            if self.driver.current_url != url:
                self.driver.get(url)

    def config_location(self):
        self.driver.get("https://www.ze.delivery/")
        time.sleep(5)
        try:
            self.driver.find_element_by_class_name('accept-cookie-container').click()
            time.sleep(1)
        except:
            pass
        self.driver.find_element_by_id('age-gate-button-yes').click()
        time.sleep(2)
        self.driver.find_element_by_id('fake-address-search-input').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('css-1jrbali-textCard').click()
        time.sleep(3)
        self.driver.find_element_by_id('user-address-map-button-request-location').click()
        time.sleep(5)
        self.driver.find_element_by_id('user-address-map-confirm-button').click()
        time.sleep(5)
        self.driver.find_element_by_id('confirm-address-modal-checkbox-without-complement').click()
        time.sleep(1)
        self.driver.find_element_by_id('confirm-address-modal-button-save-address').click()
        time.sleep(5)
        
        return True
    
    def __del__(self):
        if hasattr(self, 'driver') and self.driver is not None:
            self.driver.quit()


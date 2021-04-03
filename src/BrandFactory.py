from src.Beer import Beer


class BrandFactory():
    def __init__(self,browser,brand):
        self.browser = browser
        self.brand = brand.upper()
        self.urls = dict(BRAHMA='https://www.ze.delivery/produtos/marca/brahma',
                     SKOL='https://www.ze.delivery/produtos/marca/skol',
                     BUDWEISER='https://www.ze.delivery/produtos/marca/budweiser',
                     ANTARTICA = 'https://www.ze.delivery/produtos/marca/antarctica',
                     ORIGINAL =  'https://www.ze.delivery/produtos/marca/original',
                     STELLA = 'https://www.ze.delivery/produtos/marca/stella-artois',
                     BECKS = 'https://www.ze.delivery/produtos/marca/becks',
                     CORONA = 'https://www.ze.delivery/produtos/marca/corona',
                     BOHEMIA = 'https://www.ze.delivery/produtos/marca/bohemia',
                     COLORADO = 'https://www.ze.delivery/produtos/marca/colorado')
        

    def brand_selector(self):
        if self.brand in self.urls:
            return Beer(self.browser,self.urls.get(self.brand),self.brand)
        else:
            return Beer(self.browser,self.urls,"ALL")


            
        
        
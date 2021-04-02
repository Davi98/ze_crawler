from src.Beer import Beer


class BrandFactory():
    def __init__(self,browser,brand):
        self.browser = browser
        self.brand = brand.upper()
        

    def brand_selector(self):
        if self.brand == 'BRAHMA':
            return Beer(self.browser,"https://www.ze.delivery/produtos/marca/brahma",self.brand)
        elif self.brand == "SKOL":
            return Beer(self.browser,"https://www.ze.delivery/produtos/marca/skol",self.brand)
        elif self.brand == "BUDWEISER":
            return Beer(self.browser,"https://www.ze.delivery/produtos/marca/budweiser",self.brand)
        elif self.brand == "ANTARTICA":
            return Beer(self.browser,"https://www.ze.delivery/produtos/marca/antarctica",self.brand)
        elif self.brand == "ORIGINAL":
            return Beer(self.browser,"https://www.ze.delivery/produtos/marca/original",self.brand)
        elif self.brand == "STELLA":
            return Beer(self.browser,"https://www.ze.delivery/produtos/marca/stella-artois",self.brand)
        elif self.brand == "BECKS":
            return Beer(self.browser,f"https://www.ze.delivery/produtos/marca/becks",self.brand)
        elif self.brand == "CORONA":
            return Beer(self.browser,f"https://www.ze.delivery/produtos/marca/corona",self.brand)
        elif self.brand == "BOHEMIA":
            return Beer(self.browser,f"https://www.ze.delivery/produtos/marca/bohemia",self.brand)
        elif self.brand == "COLORADO":
            return Beer(self.browser,f"https://www.ze.delivery/produtos/marca/colorado",self.brand)

            
        
        
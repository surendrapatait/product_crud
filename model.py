class Product():

    def __init__(self,id=0,pdnm="",pdqty=0,pdpr=0,pdven=''):
        self.ProductId=int(id)
        self.ProductName=pdnm
        self.ProductQty=int(pdqty)
        self.ProductPrice=float(pdpr)
        self.ProductVendor=pdven

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)



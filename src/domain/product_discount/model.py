from src.domain.product.model import Product
from src.domain.payment_method.model import PaymentMethod



class ProductDiscount:
  def __init__(self,mode,value,product:Product,payment_method:PaymentMethod):
    self.mode = mode
    self.value = value
    self.product = product
    self.payment_method = payment_method

    print(self.product.discounts)
    print(list(filter(
        lambda discount:
            self.product.id == discount["product_id"] and
            self.payment_method.id == discount["payment_method_id"], self.product.discounts)))
        

    if len(list(filter(
        lambda discount:
            self.product.id == discount["product_id"] and
            self.payment_method.id == discount["payment_method_id"], self.product.discounts))) == 0:
        self.product.add_discount({"product_id":self.product.id, 'payment_method_id':self.payment_method.id})
        
        

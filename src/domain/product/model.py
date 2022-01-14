
from typing import List
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.product_discount.model import ProductDiscount


class Product:
  def __init__(self, description, price, technical_details, image, visible,category:Category,supplier:Supplier):
    self.description = description  
    self.price = price
    self.technical_details = technical_details
    self.image = image
    self.visible = visible
    self.category = category
    self.supplier = supplier
    self.discounts : List[ProductDiscount] = []
  
  def __str__(self) -> str:
      return f'{self.description},{self.price},{self.technical_details},{self.image},{self.visible}'
    
  def add_discount(self,discount):
      self.discounts.append(discount)
      


      

class Product:
  def __init__(self, description, price, technical_details, image, visible):
    self.description = description  
    self.price = price
    self.technical_details = technical_details
    self.image = image
    self.visible = visible
    self.discounts = []
  
  def __str__(self) -> str:
      return f'{self.description},{self.price},{self.technical_details},{self.image},{self.visible}'
    
  def add_discount(self,discount):
      self.discounts.append(discount)
      


      
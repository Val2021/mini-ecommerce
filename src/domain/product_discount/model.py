from src.domain.payment_method.model import PaymentMethod



class ProductDiscount:
  def __init__(self,mode,value,payment_method:PaymentMethod):
    self.mode = mode
    self.value = value
    self.payment_method = payment_method



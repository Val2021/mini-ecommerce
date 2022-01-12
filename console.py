from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.product_discount_repository import ProductDiscountRepository
from src.domain.product.model import Product
from src.domain.coupon.model import Coupon
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

# repository = ProductRepository(db)
# product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True)

# repository = CouponRepository(db)
# coupon = Coupon(code="1wse3",expire_at=datetime.now(),limit="4",type="11.1",value="10,9")


# repository.get()
# repository.add(coupon)

# print(coupon.id)
# print(coupon.code)

# repository = SupplierRepository(db)
# supplier = Supplier(name="Tesla")


# repository.get()
# repository.add(supplier)

# print(supplier.id)
# print(supplier.name)

# repository = PaymentMethodRepository(db)
# paymentmethod = PaymentMethod(name="visa",enabled=False)


# repository.get()
# repository.add(paymentmethod)

# print(paymentmethod.id)
# print(paymentmethod.name)

# product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True)
class FakeProduct():
    def __init__(self) -> None:
        self.id=1
        self.description='descricao 2' 
        self.price=10
        self.technical_details='detalhes tecnicos'
        self.image=''
        self.visible=True
        self.discounts = [{"product_id":1, 'payment_method_id':1}]
        

    def __str__(self) -> str:
      return f'{self.description},{self.price},{self.technical_details},{self.image},{self.visible}'
    
    def add_discount(self,discount):
        self.discounts.append(discount)

product = FakeProduct()

# payment_method = PaymentMethod(name='visa',enabled=False)

class FakePaymentMethod():
    def __init__(self) -> None:
        self.id = 1
        self.name='visa'
        self.enabled=False

payment_method=FakePaymentMethod()

# repository = ProductDiscountRepository(db)
productdiscount = ProductDiscount(mode="visa",value="20",product=product,payment_method=payment_method)
productdiscount = ProductDiscount(mode="visa",value="20",product=product,payment_method=payment_method)


# repository.get()
# repository.add(productdiscount)

print(productdiscount.id)
print(productdiscount.product)
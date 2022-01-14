from datetime import datetime
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.customer_repository import CustomerRepository
from src.adapter.repositories.product_discount_repository import ProductDiscountRepository
from src.adapter.repositories.address_repository import AddressRepository
from src.domain.product.model import Product
from src.domain.coupon.model import Coupon
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.address.model import Address
from src.domain.customer.model import Customer
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.adapter.database import Session
from src.adapter.orm import start_mapper
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.category_service import create_category
from src.services.customer_service import create_customer,create_address




start_mapper()

db = Session()

uow = SqlAlchemyUnitOfWork(db)

customer = create_customer(first_name="Maria",last_name="Lima",phone_number="0101010101",genre="F",document_id="02020202",birth_date=datetime.now(),uow=uow)


address = create_address(address="Rua 1", city="Rio", state = "Rio", number = "1", zipcode="01010", neighbourhood="Copacabana", primary=True, customer_id=1, uow=uow)


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

# # product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True)
# class FakeProduct():
#     def __init__(self) -> None:
#         self.id=3
#         self.description='descricao 2' 
#         self.price=10
#         self.technical_details='detalhes tecnicos'
#         self.image=''
#         self.visible=True
#         self.discounts = [{"product_id":3, 'payment_method_id':3}]
        

#     def __str__(self) -> str:
#       return f'{self.description},{self.price},{self.technical_details},{self.image},{self.visible}'
    
#     def add_discount(self,discount):
#         self.discounts.append(discount)

# product = FakeProduct()

# # payment_method = PaymentMethod(name='visa',enabled=False)

# class FakePaymentMethod():
#     def __init__(self) -> None:
#         self.id = 3
#         self.name='visa'
#         self.enabled=False

# payment_method=FakePaymentMethod()

# # repository = ProductDiscountRepository(db)
# productdiscount = ProductDiscount(mode="pix",value="21",product=product,payment_method=payment_method)
# productdiscount = ProductDiscount(mode="pix",value="21",product=product,payment_method=payment_method)

# # repository.get()
# # repository.add(productdiscount)

# print(productdiscount.id)
# print(productdiscount.product)


# customer_repository = CustomerRepository(db)
# address_repository = AddressRepository(db)

# customer = Customer(
#     first_name="kaique",
#     last_name="moreira",
#     phone_number="11912345678",
#     genre="M",
#     document_id="45579312345",
#     birth_date=None,
# )

# customer.add_address(Address(
#     address="Rua tal",
#     city="Aruja",
#     state="SP",
#     number="139",
#     zipcode="074000",
#     neighbourhood="137",
#     primary=True,
# ))
# customer.add_address(Address(
#     address="Rua sei la",
#     city="Aruja",
#     state="SP",
#     number="139",
#     zipcode="074000",
#     neighbourhood="137",
#     primary=True,
# ))
# for i in customer.address:
#     print(i.address)
#     print(i.primary)
# customer_repository.add(customer)


#########Usando uow #############

# uow = SqlAlchemyUnitOfWork(db)

# create_category('Categoria 1', uow)




# with uow:
#   pm = PaymentMethod(name='pix', enabled=True, id=1)
#   uow.payment_method_repository.add(pm)


#   c = Category(name='eletronico')
#   uow.category_repository.add(c)
#   s = Supplier(name='HP')
#   uow.supplier_repository.add(s)


#   p = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True, category=c, supplier=s)
#   pd = ProductDiscount(mode='value', value=100, payment_method=pm)
#   p.add_discount(pd)

#   uow.product_repository.add(p)

#   print(len(p.discounts))

#   pm2 = PaymentMethod(name='boleto', enabled=True, id=2)
#   uow.payment_method_repository.add(pm2)

#   # pd2 = ProductDiscount(mode='percetage', value=100, payment_method=pm2)
#   # p.add_discount(pd2)


# payment_method_repository = PaymentMethodRepository(db, PaymentMethod)
# category_repository = CategoryRepository(db, Category)
# supplier_repository = SupplierRepository(db, Supplier)
# product_repository = ProductRepository(db, Product)


# ================= 
# Populando o banco de dados





# Adicionando um novo desconto

# p = db.query(Product).filter_by(id=1).first()

# # pm = db.query(PaymentMethod).filter_by(id=1).first()
# pm = PaymentMethod('cartão de crédito', enabled=True, id=3)

# pd = ProductDiscount(mode='value', value=100, payment_method=pm)

# print(len(p.discounts))


# p.add_discount(pd)

# print(p.id)
# db.commit()
# db.close()


# Buscando um desconto no banco de dados

# pd = db.query(ProductDiscount).filter_by(id=1).first()

# print(pd.value)
# print(pd.payment_method.name)

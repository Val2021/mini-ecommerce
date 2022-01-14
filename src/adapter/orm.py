from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String,DateTime,BOOLEAN,Date
from src.domain.address.model import Address
from src.domain.customer.model import Customer
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.coupon.model import Coupon
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier



metadata = Base.metadata

table_category = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(20)),
)


table_supplier = Table(
    'suppliers',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(20)),
)


table_product = Table(
  'products', 
  metadata, 
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('description', String(100)),
  Column('technical_details', String(255)),
  Column('price', Float(10, 2)),
  Column('visible', Boolean),
  Column('category_id', ForeignKey('categories.id')),
  Column('supplier_id', ForeignKey('suppliers.id'))
)



table_paymentmethod = Table(
  'paymentmethods', 
  metadata, 
  Column('id',Integer, primary_key=True,autoincrement=True),
  Column('name',String(45)),
  Column('enabled',Boolean),
)


table_coupon = Table(
  'coupons', 
  metadata, 
  Column('id',Integer, primary_key=True),
  Column('code',String(10)),
  Column('expire_at', DateTime),
  Column('limit',Integer),
  Column('type',String(15)),
  Column('value',Float(10,2)),
)

table_productdiscount = Table(
  'productdiscounts', 
  metadata, 
  Column('id',Integer, primary_key=True),
  Column('mode',String(45)),
  Column('value', Float(10,2)),
  Column('product_id',ForeignKey('products.id')),
  Column('payment_method_id',ForeignKey('paymentmethods.id')),
  )

table_customer = Table(
  'customers', 
  metadata,
  Column("id",Integer, primary_key=True),
  Column("first_name",String(45)),
  Column("last_name",String(45)),
  Column("phone_number",String(15)),
  Column("genre",String(45)),
  Column("document_id",String(45)),
  Column("birth_date",Date)
    )


table_address = Table(
  'addresses', 
   metadata,
  Column("id",Integer, primary_key=True),
  Column('address',String(255)),
  Column('city',String(45)),
  Column('state',String(45)),
  Column('number',String(10)),
  Column('zipcode',String(6)),
  Column('neighbourhood',String(45)),
  Column('primary',Boolean),
  Column("customer_id", ForeignKey("customers.id")),
)

def start_mapper():
    category_mapper = mapper(Category, table_category)
    supplier_mapper = mapper(Supplier, table_supplier)
    payment_method_mapper = mapper(PaymentMethod,table_paymentmethod)
    address_mapper = mapper(Address, table_address)

    product_discount_mapper = mapper(
        ProductDiscount,
        table_productdiscount,
        properties={
            "payment_method": relationship(payment_method_mapper),
        },
    )

    mapper(
        Product,
        table_product,
        properties={
            "category": relationship(category_mapper),
            "supplier": relationship(supplier_mapper),
            "discounts": relationship(product_discount_mapper),
        },
    )

    mapper(Coupon, table_coupon)
    mapper(Customer, table_customer, properties={"address": relationship(address_mapper)})
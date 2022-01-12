from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String,DateTime,BOOLEAN
from src.domain.payment_method.model import PaymentMethod
from src.domain.product_discount.model import ProductDiscount
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.coupon.model import Coupon
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier



metadata = Base.metadata

table_product = Table(
  'products', 
  metadata, 
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('description', String(100)),
  Column('technical_details', String(255)),
  Column('price', Float(10, 2)),
  Column('visible', Boolean),
)


table_category = Table(
  'categories', 
  metadata, 
  Column('id',Integer, primary_key=True,autoincrement=True),
  Column('name',String(45))
)

table_supplier = Table(
  'suppliers', 
  metadata, 
  Column('id',Integer, primary_key=True,autoincrement=True),
  Column('name',String(45))
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

def start_mapper():

  product_mapper = mapper(Product, table_product)
  paymentmethod_mapper = mapper(PaymentMethod, table_paymentmethod)

  # mapper(Product, table_product)
  # mapper(PaymentMethod, table_paymentmethod)
  mapper(Category, table_category)
  mapper(Supplier, table_supplier)
  mapper(Coupon, table_coupon)
  mapper(ProductDiscount, table_productdiscount, properties={
    'product':relationship(product_mapper),
    'payment_method':relationship(paymentmethod_mapper)

  })


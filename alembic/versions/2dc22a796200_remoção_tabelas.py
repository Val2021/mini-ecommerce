"""Remoção Tabelas

Revision ID: 2dc22a796200
Revises: 5f80ddad8398
Create Date: 2022-01-14 12:34:51.154023

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2dc22a796200'
down_revision = '5f80ddad8398'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('addresses')
    op.drop_table('productdiscounts')
    op.drop_table('suppliers')
    op.drop_table('products')
    op.drop_table('categories')
    op.drop_table('customers')
    op.drop_table('coupons')
    op.drop_table('paymentmethods')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paymentmethods',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('paymentmethods_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('enabled', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='paymentmethods_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('coupons',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('code', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('expire_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('limit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('value', sa.REAL(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='coupons_pkey')
    )
    op.create_table('customers',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('customers_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('genre', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('document_id', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='customers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='categories_pkey')
    )
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('products_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('technical_details', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('price', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('visible', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='products_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('suppliers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='suppliers_pkey')
    )
    op.create_table('productdiscounts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mode', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('value', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('payment_method_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['payment_method_id'], ['paymentmethods.id'], name='productdiscounts_payment_method_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='productdiscounts_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='productdiscounts_pkey')
    )
    op.create_table('addresses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('address', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('number', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('zipcode', sa.VARCHAR(length=6), autoincrement=False, nullable=True),
    sa.Column('neighbourhood', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('primary', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='addresses_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='addresses_pkey')
    )
    # ### end Alembic commands ###
